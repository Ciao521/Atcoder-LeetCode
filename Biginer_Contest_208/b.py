p = int(input())
coin = [1]*11

for i in range(1, 11):
    coin[i] = coin[i-1] * i

ans = 0
for j in range(10, 0, -1):
    if p < coin[j]:
        continue
    ans += (p//coin[j])
    p %= coin[j]
print(ans)
