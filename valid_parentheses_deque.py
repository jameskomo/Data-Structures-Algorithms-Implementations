from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_pairs={'(':')', '[':']', '{':'}'}
        queue=deque()
        for character in s:
            if character in parentheses_pairs:
                queue.append(character)
            elif len(queue) !=0 and parentheses_pairs.get(queue[-1]) == character:
                queue.pop() 
            else:
                return False
        return len(queue)==0
        