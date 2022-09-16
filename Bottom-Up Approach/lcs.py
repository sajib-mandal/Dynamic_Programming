def lcs(str1, str2):
    dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[0][0]


print(lcs("abcde", "ace"))
