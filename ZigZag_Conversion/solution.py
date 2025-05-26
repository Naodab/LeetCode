class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = [''] * numRows
        while s:
            for i in range(numRows):
                if s:
                    print(s[0])
                    result[i] += s[0]
                    s = s[1:]
            for i in range(numRows - 2, 0, -1):
                if s:
                    result[i] += s[0]
                    s = s[1:]
        return ''.join(result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))