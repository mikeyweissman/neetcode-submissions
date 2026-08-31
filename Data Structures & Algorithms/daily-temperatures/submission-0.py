class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = []
        res = [0] * len(temperatures)


        for i,t in enumerate(temperatures):

            if not stack:
                stack.append([t,i])

            else:
                if t <= stack[-1][0]:
                    stack.append([t,i])
                else:
                    
                    count = 0
                    while(True):
                        if stack and t > stack[-1][0]:
                            prevT = stack[-1][0]
                            prevI = stack[-1][1]
                            res[prevI] = i - prevI
                            stack.pop()
                        else:
                            stack.append([t,i])
                            break

        return res
                        

        
