class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
          return False 

        num_rows , num_cols = len(matrix) , len(matrix[0])

        left , right = 0 ,num_rows * num_cols - 1 

        while left <= right:
          mid = (left+right) // 2 
          row_index = mid // num_cols 
          col_index = mid % num_cols

          mid_value = matrix[row_index][col_index]

          if mid_value == target:
            return True 

          elif mid_value < target:
            left = mid + 1 
          else:
            right = mid - 1 


        return False 