def decode_message( s: str, p: str) -> bool:

# write your code here
    # Initialize DP table with False values
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    # Empty pattern matches empty string
    dp[0][0] = True

    # Handle cases where pattern starts with '*' and matches empty prefix of s
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                # '*' can either match nothing (dp[i][j-1]) or match one character (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                # '?' matches one character, or characters match directly
                dp[i][j] = dp[i - 1][j - 1]

    # The answer is whether the entire message and pattern match
    return dp[len(s)][len(p)]

  
        return False
