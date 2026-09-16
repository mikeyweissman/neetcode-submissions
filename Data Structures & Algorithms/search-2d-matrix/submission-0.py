class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        startCol = 0
        endCol = len(matrix[0]) - 1
        startRow = 0
        endRow = len(matrix) - 1
        
    
        while startRow <= endRow and startCol<=endCol:
            
            midRow = (startRow +endRow) //2
            

            if target >=matrix[midRow][0] and target<=matrix[midRow][endCol]:
                while startCol<=endCol:
                    midCol = (startCol + endCol) //2

                    if matrix[midRow][midCol] == target: 
                        return True
                    elif matrix[midRow][midCol]>target:
                        endCol = midCol - 1
                    else:
                        startCol = midCol + 1


            elif target>matrix[midRow][endCol]:
                startRow = midRow + 1
            else:
                endRow = midRow - 1

        return False
            

        