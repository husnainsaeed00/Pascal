

class Solution:
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            row = [1]  # First element of each row is always 1
            if i > 0:
                prev_row = triangle[i - 1]
                for j in range(1, i):
                    row.append(prev_row[j - 1] + prev_row[j])
                row.append(1)  # Last element of each row is always 1
            triangle.append(row)
        return triangle

# Example usage:
sol = Solution()
print(sol.generate(5))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

print(sol.generate(1))
# Output: [[1]]
