class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize hash sets for rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Traverse the board
        for i in range(9):  # Rows
            for j in range(9):  # Columns
                num = board[i][j]

                # Skip empty cells
                if num == '.':
                    continue

                # Calculate sub-box index
                box_index = (i // 3) * 3 + (j // 3)

                # Check if number already exists
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False  # Duplicate found

                # Add number to the respective sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True  # No duplicates found
