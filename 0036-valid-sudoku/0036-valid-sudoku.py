class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                box_index = (i //3 ) * 3 + (j // 3)

                if num in row[i] or num in col[j] or num in boxes[box_index]:
                    return False

                
                row[i].add(num)
                col[j].add(num)
                boxes[box_index].add(num)


        return True
