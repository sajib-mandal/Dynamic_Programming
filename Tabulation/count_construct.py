def count_construct(target: str, word_bank: list) -> int:
    table = [0 for i in range(len(target) + 1)]
    table[0] = 1
    for i in range(len(target)):
        if table[i] is not None:    # no need this line
            for word in word_bank:
                if target[i:i+len(word)] == word:
                    table[i + len(word)] += table[i]
    return table[len(target)]


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  # 0
