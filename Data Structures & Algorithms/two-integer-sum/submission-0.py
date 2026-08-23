class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index = {}

        for i,x in enumerate(nums):
            needed = target - x
            if needed in index:
                return [index[needed],i]
                
            else:
                index[x] = i
        
        return []