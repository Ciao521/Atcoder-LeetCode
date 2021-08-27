def log2(n):
    for i in range(n):
        target =2**i
        if target<=n and(2**(i+1))>n:
            return i

a =int (input())
print(log2(a))
