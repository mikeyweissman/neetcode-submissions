class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(len(intervals)):
            if i+1 <= len(intervals)-1 and end>=intervals[i+1][0]:
                if end < intervals[i+1][1]:
                    end = intervals[i+1][1]
            

            else:
                res.append([start,end])

                if i+1 > len(intervals)-1:
                    break

                else:
                
                    start = intervals[i+1][0]
                    end = intervals[i+1][1]

        
        return res