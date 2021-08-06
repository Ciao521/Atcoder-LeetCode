N,X =map(int,input().split())
arr = [int(x) for x in input().split()]
if sum(arr)-N/2<=X:
    print("Yes")
else:
    print("No")