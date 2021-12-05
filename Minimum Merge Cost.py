import sys
def mergenumbers(numbers):
    n=len(numbers)
    if n==0:
        return 0
    prefixsum=[0]*(n+1)
    for i in range(1,n+1):
        prefixsum[i]=prefixsum[i-1]+numbers[i-1]
    dp = [[0 for i in range(n+1)]for j in range(n+1)]         #For memorisation
    for i in range(1,n+1):
        dp[i][i] = 0
    for p in range(2,n+1):
        for i in range(1,n-p+2):
            j = i+p-1
            sum = prefixsum[j]-prefixsum[i-1]
            dp[i][j]=sys.maxsize
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],sum+dp[i][k] +
                               dp[k + 1][j])
    return dp[1][n]


arr1 = [ 1,2,3,4 ]
 
# Function call
print(mergenumbers(arr1)) #Answer is 19

    