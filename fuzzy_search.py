def edit_distance(s1, s2):
    # Levenshtein distance DP implementation
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # Deletion
                                   dp[i][j-1],    # Insertion
                                   dp[i-1][j-1])  # Replacement
    return dp[m][n]

def fuzzy_search(query, candidates, max_dist=2):
    # Return candidates within max_dist edit distance from query
    result = []
    for word in candidates:
        dist = edit_distance(query, word)
        if dist <= max_dist:
            result.append((word, dist))
    # Sort by distance and then alphabetically
    result.sort(key=lambda x: (x[1], x[0]))
    return [word for word, dist in result]
