'''
3つの数字をよみとって，2つの数字を足し算し最も合計を出力する．

EX)3 6 5
6+5=11
11を出力する．
'''
arr = [int(x) for x in input().split()]
arr.sort()
print(arr[2]+arr[1])