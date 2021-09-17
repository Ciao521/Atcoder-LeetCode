from itertools import permutations
s, k = input().split()
k = int(k)
s = list(s)
se = set()
for p in permutations(s, len(s)):
    se.add("".join(p))
print(sorted(list(se))[k - 1])