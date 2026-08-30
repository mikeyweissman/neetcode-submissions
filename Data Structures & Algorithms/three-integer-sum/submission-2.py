class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()

        for i in range(len(nums)):     
            l = i+1
            r = len(nums) - 1

            while(l < r):
                if(-nums[i] == nums[l] + nums[r]):
                    res.add((nums[i],nums[r],nums[l]))
                    l += 1
                    r -= 1
                elif (-nums[i] > nums[l] + nums[r]):
                    l += 1
                else:
                    r -= 1
        
        return [list(x) for x in res]
