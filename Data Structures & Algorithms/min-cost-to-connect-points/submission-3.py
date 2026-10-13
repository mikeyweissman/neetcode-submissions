class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        des = []
        cut = {0}
        res = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):

                distance = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                des.append([distance,i,j])

        des.sort()


        while len(cut) < n:
            nextDist = float('inf')
            nextElem = None
            for element in des:
                if (element[1] not in cut or element[2] not in cut) and (element[1] in cut or element[2] in cut):
                    if element[0] <nextDist:
                        nextDist = element[0]
                        nextElem = element
                        break

            
            cut.add(nextElem[1])
            cut.add(nextElem[2])
            res += nextDist
        

        return res
            
                
            

        
        return res