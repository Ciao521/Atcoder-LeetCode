'''
1以上 N以下の整数からなる長さ N
の数列が与えられます。

Aの並び替えによって得られるかどうか判定してください。
 '''
N = int(input())
A = list(map(int,input().split()))

print('Yes'if len(set(A))==N else 'No')

'''
list は[]と同じ構造
map とは，同じ型でつふけるパターン
'''
