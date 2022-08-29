# recursion without memoization

def all_construct(target: str, word_bank: list) -> list:
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [el[:] for el in suffix_ways]
            [el.insert(0, word) for el in target_ways]
            result.extend(target_ways)
    return result


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'bord']))
print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))


# recursion with memoization

def all_construct(target: str, word_bank: list, memo={}) -> list:
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = [el[:] for el in suffix_ways]
            [el.insert(0, word) for el in target_ways]
            result.extend(target_ways)
    memo[target] = result
    return result


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={}))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], memo={}))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'bord'], memo={}))
print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], memo={}))
