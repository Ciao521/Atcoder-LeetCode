#! /usr/bin/python3
N, K = [int(s) for s in input().split()]
a_s = [int(s) for s in input().split()]
sorted_a = sorted(a_s)
# 0 1 2
border = sorted_a[K%N]
base = K//N
for a in a_s:
    if a < border:
        print(base+1)
    else:
        print(base)
