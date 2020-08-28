def isValid(s: str) -> bool:
    '''
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    '''
    pairs = {'(':')', '[':']', '{':'}'}
    stack = []

    for character in s:
        if character in pairs.keys():
            stack.append(character)
        elif len(stack) !=0 and pairs.get(stack[-1]) == character:
            stack.pop()
        else: 
            return False

    return len(stack) == 0

print(isValid("((()))"))




        