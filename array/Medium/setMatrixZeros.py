class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Variable to track if the first column should be zero
        col0 = 1

        # Step 1: Use first row and first column as markers
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0

            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0      # Mark the row
                    matrix[0][j] = 0      # Mark the column

        # Step 2: Update the matrix using the markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle the first row
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 4: Handle the first column
        if col0 == 0:
            for i in range(rows):
                matrix[i][0] = 0


# ---------------- Driver Code ----------------

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print("Original Matrix:")
for row in matrix:
    print(row)

sol = Solution()
sol.setZeroes(matrix)

print("\nMatrix after setting zeroes:")
for row in matrix:
    print(row)