class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dic = {
        ')': '(',
        ']': '[',    
        '}': '{'
        }
        

        for i in s:
            if i in ')]}':
                if not stack or dic[i] != stack[-1] :
                    return False
                else:
                    stack.pop()

            else:
                if i in '([{':
                    stack.append(i)
        
        return not stack 


