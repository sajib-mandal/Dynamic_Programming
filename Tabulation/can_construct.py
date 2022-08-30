def can_construct(target: str, words: list) -> bool:
    table = [False for i in range(len(target)+1)]
    table[0] = True
    for i in range(len(target)):
        if table[i] is not False:
            for word in words:
                # if the word matches the characters starting at position i
                         #[start: end]
                if target[i:i+len(word)] == word:
                    table[i + len(word)] = True
    return table[len(target)]

print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # True
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # True
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #True
