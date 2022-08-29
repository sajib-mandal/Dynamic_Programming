# recursive without memoization
def can_construct(target: str, word_bank: list) -> bool:
    if target == '':
        return True
    for i in word_bank:
        if target.startswith(i):
            suffix = target[len(i):]
            if can_construct(suffix, word_bank):
                return True

    return False


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # True
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # True
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #True


# recursive with memoization

def can_construct(target: str, word_bank: list, memo) -> bool:
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for i in word_bank:
        if target.startswith(i):
            suffix = target[len(i):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], memo={}))  # True
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={}))  # False
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], memo={}))  # True
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], memo={})) # False
