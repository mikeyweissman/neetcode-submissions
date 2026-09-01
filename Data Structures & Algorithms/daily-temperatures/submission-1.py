class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i,t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                dif = i - stackI
                res[stackI] = dif
            
            stack.append([t,i])
        
        return res