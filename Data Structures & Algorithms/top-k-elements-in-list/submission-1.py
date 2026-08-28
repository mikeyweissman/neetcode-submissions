class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        top = [[] for i in range(len(nums))]
        res = [] 

        for x in nums:
            count[x] = count.get(x,0) + 1
            
        for key in count:
            index = count[key] - 1
            top[index].append(key)

        for i in range(len(nums)-1,-1,-1):
            for j in range(len(top[i])):
                res.append(top[i][j])
                if len(res) == k:
                    return res



        