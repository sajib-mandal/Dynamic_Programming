# recursive top-down

# Function that matches the input string with a given wildcard pattern
def isMatch(word, pattern, n, m, lookup):
 
    # If both the input string and pattern reach their end,
    # return true
    if m < 0 and n < 0:
        return True
 
    # If only the pattern reaches its end, return false
    elif m < 0:
        return False
 
    # If only the input string reaches its end, return true
    # if the remaining characters in the pattern are all '*'
    elif n < 0:
        for i in range(m + 1):
            if pattern[i] != '*':
                return False
        return True
 
    # If the subproblem is encountered for the first time
    if not lookup[n][m]:
        if pattern[m] == '*':
            # 1. '*' matches with current characters in the input string.
            # Here, we will move to the next character in the string.
 
            # 2. Ignore '*' and move to the next character in the pattern
            lookup[n][m] = isMatch(word, pattern, n - 1, m, lookup) or \
                        isMatch(word, pattern, n, m - 1, lookup)
        else:
            # If the current character is not a wildcard character, it
            # should match the current character in the input string
            if pattern[m] != '?' and pattern[m] != word[n]:
                lookup[n][m] = False
            # check if pattern[0…m-1] matches word[0…n-1]
            else:
                lookup[n][m] = isMatch(word, pattern, n - 1, m - 1, lookup)
 
    return lookup[n][m]
 
 
# Wildcard Pattern Matching Implementation in Python
if __name__ == '__main__':
 
    word = 'xyxzzxy'
    pattern = 'x***x?'
 
    # create a DP lookup table
    lookup = [[False for x in range(len(pattern) + 1)] for y in range(len(word) + 1)]
 
    if isMatch(word, pattern, len(word) - 1, len(pattern) - 1, lookup):
        print('Match')
    else:
        print('No Match')
        
        
        
        
        
    # tabulation bottom-up
   
  
  # Function that matches an input string with a given wildcard pattern
def isMatch(word, pattern):
 
    # get length of string and wildcard pattern
    n = len(word)
    m = len(pattern)
 
    # create a DP lookup table
    T = [[False for x in range(m + 1)] for y in range(n + 1)]
 
    # if both pattern and string are empty: match
    T[0][0] = True
 
    # handle empty string case (i == 0)
    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            T[0][j] = T[0][j - 1]
 
    # build a matrix in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j - 1] == '*':
                T[i][j] = T[i - 1][j] or T[i][j - 1]
            elif pattern[j - 1] == '?' or word[i - 1] == pattern[j - 1]:
                T[i][j] = T[i - 1][j - 1]
 
    # last cell stores the answer
    return T[n][m]
 
 
# Wildcard Pattern Matching Implementation in Python
if __name__ == '__main__':
 
    word = 'xyxzzxy'
    pattern = 'x***x?'
 
    if isMatch(word, pattern):
        print('Match')
    else:
        print('No Match')
