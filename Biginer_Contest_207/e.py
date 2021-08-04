MOD = 10**9+7

N = int(input())
A = list(map(int,input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for k in range(1,N+1):
    dp_sum_rem = [0]*k
    dp_sum_rem[0] = dp[k-1][0]
    Asum_rem = 0
    for x in range(1,N+1):
        Asum_rem += A[x-1] % k
        Asum_rem %= k
        
        dp[k][x] = dp_sum_rem[Asum_rem]
        dp_sum_rem[Asum_rem] += dp[k-1][x]
        dp_sum_rem[Asum_rem] %= MOD
        
print(sum(dp[i+1][N] for i in range(N)) % MOD)