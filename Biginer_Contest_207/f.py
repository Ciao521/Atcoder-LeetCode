import os
import sys

import numpy as np


def solve(inp):
    def simple_convolution(aaa, bbb, MOD):
        n = len(aaa)
        m = len(bbb)
        result = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                result[i + j] = (result[i + j] + aaa[i] * bbb[j]) % MOD
        return result

    n = inp[0]
    int_list = [n]
    int_list.pop()
    links = [int_list.copy() for _ in range(n)]
    for i in range(n - 1):
        u = inp[2 * i + 1] - 1
        v = inp[2 * i + 2] - 1
        links[u].append(v)
        links[v].append(u)

    dp0 = [int_list.copy() for _ in range(n)]
    dp1 = [int_list.copy() for _ in range(n)]
    dp2 = [int_list.copy() for _ in range(n)]
    MOD = 10 ** 9 + 7
    status = np.zeros(n, np.int8)
    q = [0]
    while q:
        v = q[-1]
        if status[v] == 0:
            status[v] = 1
            for u in links[v]:
                if status[u] == 0:
                    q.append(u)
        else:
            q.pop()
            status[v] = 2

            cdp01 = [1]  # 子のDPの0,1をあわせてたたみ込んだもの
            cdp012 = [1]  # 子のDPの0,1,2をあわせてたたみ込んだもの
            cdp0_12 = [1]  # 子のDPの0をシフトした上で1,2とあわせてたたみこんだもの

            for u in links[v]:
                if status[u] != 2:
                    continue
                tdp01 = [0] * max(len(dp0[u]), len(dp1[u]))
                tdp012 = [0] * max(len(dp0[u]), len(dp1[u]), len(dp2[u]))
                tdp0_12 = [0] * max(len(dp0[u]) + 1, len(dp1[u]), len(dp2[u]))
                for i, t in enumerate(dp0[u]):
                    tdp01[i] += t
                    tdp012[i] += t
                    tdp0_12[i + 1] += t
                for i, t in enumerate(dp1[u]):
                    tdp01[i] += t
                    tdp012[i] += t
                    tdp0_12[i] += t
                for i, t in enumerate(dp2[u]):
                    tdp012[i] += t
                    tdp0_12[i] += t
                for i in range(len(tdp01)):
                    tdp01[i] %= MOD
                for i in range(len(tdp012)):
                    tdp012[i] %= MOD
                for i in range(len(tdp0_12)):
                    tdp0_12[i] %= MOD
                cdp01 = simple_convolution(cdp01, tdp01, MOD)
                cdp012 = simple_convolution(cdp012, tdp012, MOD)
                cdp0_12 = simple_convolution(cdp0_12, tdp0_12, MOD)

            for i in range(len(cdp01)):
                cdp012[i] = (cdp012[i] - cdp01[i]) % MOD
            cdp012.insert(0, 0)
            cdp0_12.insert(0, 0)

            while cdp01 and cdp01[-1] == 0:
                cdp01.pop()
            while cdp012 and cdp012[-1] == 0:
                cdp012.pop()
            while cdp0_12 and cdp0_12[-1] == 0:
                cdp0_12.pop()

            dp0[v] = cdp01
            dp1[v] = cdp012
            dp2[v] = cdp0_12

    ans = np.zeros(n + 1, np.int64)
    for i, t in enumerate(dp0[0]):
        ans[i] += t
    for i, t in enumerate(dp1[0]):
        ans[i] += t
    for i, t in enumerate(dp2[0]):
        ans[i] += t

    return ans % MOD


SIGNATURE = '(i8[:],)'
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', SIGNATURE)(solve)
    cc.compile()
    exit()

if os.name == 'posix':
    # noinspection PyUnresolvedReferences
    from my_module import solve
else:
    from numba import njit

    solve = njit(SIGNATURE, cache=True)(solve)
    print('compiled', file=sys.stderr)

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solve(inp)
print('\n'.join(map(str, ans)))
