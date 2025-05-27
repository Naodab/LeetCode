class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = [1, 5, 10, 50, 100, 500, 1000]
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        result = 0
        prev_value = 0
        for char in s:
            index = roman.index(char)
            value = values[index]
            if prev_value < value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))