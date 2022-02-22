ans =""
S1=input()
S2=input()
S3=input()
C =list(map(int, list(input())))
for i in range(len(C)):
    if C[i]==1:
        ans+=S1
    elif C[i]==2:
        ans+=S2
    elif C[i]==3:
        ans+=S3

print(ans)