class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

        roman_numeral = []
        for value, symbol in zip(reversed(values), reversed(symbols)):
            while num >= value:
                roman_numeral.append(symbol)
                num -= value
        return ''.join(roman_numeral)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(1994))  # Output: "MCMXCIV"
    print(solution.intToRoman(58))    # Output: "LVIII"
    print(solution.intToRoman(4))     # Output: "IV"
    print(solution.intToRoman(9))     # Output: "IX"
    print(solution.intToRoman(44))    # Output: "XLIV"