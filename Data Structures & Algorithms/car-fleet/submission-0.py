class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        arrivalT = [0]* len(position)

        for i in range(len(position)):
            arrivalT[i] = (target - position[i]) / speed[i]
            

        comp = sorted(zip(position,speed,arrivalT))
        
        stack = []

        for p,s,t in comp:

            while stack and stack[-1][2] <= t:
                stack.pop()
            
            stack.append([p,s,t])
        
        return len(stack)



