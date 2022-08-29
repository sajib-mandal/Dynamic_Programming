# recursive without memoization

def count_construct(target: str, word_bank: list) -> int:
    if target == '':
        return 1
    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            num_ways_for_rest = count_construct(suffix, word_bank)
            total_count += num_ways_for_rest

    return total_count


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))


# recursion with memoization

def count_construct(target: str, word_bank: list, memo={}) -> int:
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            num_ways_for_rest = count_construct(suffix, word_bank, memo)
            total_count += num_ways_for_rest
    memo[target] = total_count
    return total_count


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={}))  # 2
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], memo={}))  # 1
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={}))  # 0
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], memo={}))  # 4
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], memo={}))
