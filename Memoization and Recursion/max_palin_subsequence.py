"""
Write a function, max_palin_subsequence, that takes in a string as an argument.
The function should return the length of the longest subsequence of the string
that is also a palindrome.
A subsequence of a string can be created by deleting any characters of the string,
while maintaining the relative order of characters.

For example, given:
"luwxult"
Deleting 'x' and 't' would give the subsequence:
"luwul"
The string "lowul" is a palindrome because it is the same forwards and backwards.
"""

# recursive without memoization

def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string) - 1)

def _max_palin_subsequence(string, i, j):

    if i == j:
        return 1
    if i > j:
        return 0

    if string[i] == string[j]:
        return 2 + _max_palin_subsequence(string, i + 1, j - 1)
    else:
        left = _max_palin_subsequence(string, i + 1, j)
        right = _max_palin_subsequence(string, i, j - 1)
        return max(left, right)


print(max_palin_subsequence("luwxult"))  # -> 5
print(max_palin_subsequence("xyzaxxzy"))  # -> 6
print(max_palin_subsequence("lol"))  # -> 3
print(max_palin_subsequence("boabcdefop"))  # -> 3
print(max_palin_subsequence("z"))  # -> 1


# recursive with memoization

def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, i, j, memo):

    key = (i, j)
    if key in memo:
        return memo[key]

    if i == j:
        return 1
    if i > j:
        return 0

    if string[i] == string[j]:
        memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
    else:
        left = _max_palin_subsequence(string, i + 1, j, memo)
        right = _max_palin_subsequence(string, i, j - 1, memo)
        memo[key] = max(left, right)
    return memo[key]


print(max_palin_subsequence("luwxult"))  # -> 5
print(max_palin_subsequence("xyzaxxzy"))  # -> 6
print(max_palin_subsequence("lol"))  # -> 3
print(max_palin_subsequence("boabcdefop"))  # -> 3
print(max_palin_subsequence("z"))  # -> 1
print(max_palin_subsequence("chartreusepugvicefree"))  # -> 7
print(max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty"))  # -> 15
print(max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe"))  # -> 31
