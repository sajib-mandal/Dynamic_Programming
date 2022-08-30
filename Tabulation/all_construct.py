def all_construct(target: str, words: list) -> list:
    table = [[] for i in range(len(target)+1)]
    table[0] = [[]]
    for i in range(len(target)):
        for word in words:
            if word == target[i:(i+len(word))]:
                for el in table[i]:
                    temp = el[:]
                    temp.append(word)
                    table[i+len(word)].append(temp[:])
    return table[len(target)]


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'bord']))
print(all_construct('aaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
