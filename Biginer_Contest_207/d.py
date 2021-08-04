
import math
import cmath


def move_to_center_of_gravity(s):
    """
    重心に移動させる
    """
    cg = sum(s) / N
    return [p - cg for p in s]


def solve(s, t):
    """
    S の点 s に T の点 t を重ね合わせたとき、
    S と T は一致するか？
    assert abs(s) > eps and abs(t) > eps
    """
    theta = cmath.phase(s) - cmath.phase(t)
    rotator = cmath.rect(1, theta)
    T2 = []
    for t in T:
        t2 = t * rotator
        T2.append(t2)
    ok = True
    for s in S:
        if all(abs(t - s) > eps for t in T2):
            ok = False
            break
    return ok


def main():
    global N, S, T, eps
    N = int(input())
    S = []
    for _ in range(N):
        a, b = list(map(int, input().split()))
        S.append(complex(a, b))
    T = []
    for _ in range(N):
        c, d = list(map(int, input().split()))
        T.append(complex(c, d))

    if N == 1:
        print("Yes")
        return

    assert N >= 2

    S = move_to_center_of_gravity(S)
    T = move_to_center_of_gravity(T)

    eps = 1e-8
    s0 = None
    for s in S:
        if abs(s) > eps:
            s0 = s
            break
    assert s0 is not None

    for t in T:
        if abs(t) > eps and solve(s0, t):
            print("Yes")
            return

    print("No")


main()
