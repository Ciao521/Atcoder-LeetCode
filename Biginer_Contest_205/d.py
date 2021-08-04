'''
4 3
3 5 6 7
2
5
3

それ以外の入力を出力する　4つ条件があり，それに対して3つの順位を結果プリントする．
この場合
1,2,4,8,9,10...
の生成され
2番目と5番目と3番目に当たる2,9,4が順に出力される．
探索して解く.
'''

import bisect

def solve():
    n,q = map(int,input().split())
    a = list(map(int, input().split()))
    c = [a[i] - (i +1) for i in range(n)]
    k = [int(input()) for i in range(q)]
    ret = []
    for j in range(q):
        ind = bisect.bisect_left(c, k[j])
        ret.append(k[j] + ind)
    print(*ret,sep='\n')

if __name__=='__main__':
    solve()