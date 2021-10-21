# https://leetcode.com/problems/longest-palindromic-substring/submissions/

# https://www.youtube.com/watch?v=XYQecbcd6_c

def longestPalindrome(self, s: str) -> str:
    n = len(s)

    res = ''

    for i in range(n):
        l, r = i, i

        while l >= 0 and r < n and s[l] == s[r]:
            res = s[l:r + 1] if (r + 1 - l) > len(res) else res
            l -= 1
            r += 1

        l = i
        r = i + 1

        while l >= 0 and r < n and s[l] == s[r]:
            res = s[l:r + 1] if (r + 1 - l) > len(res) else res
            l -= 1
            r += 1

    return res

#  DP
#  https://www.youtube.com/watch?v=UflHuQj6MVA

def longestPalindrome1(self, s: str) -> str:
    n = len(s)

    dp = [[False for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = True

    res = s[0]

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            res = s[i:i + 2]

    k = 3
    while k <= n:
        for i in range(n + 1 - k):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                res = s[i:j + 1] if (j + 1 - i) > len(res) else res
        k += 1
    return res


