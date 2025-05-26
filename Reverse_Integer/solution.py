class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            digit = x % 10
            x //= 10
            if self.result > (2**31 - 1) // 10 or (self.result == (2**31 - 1) // 10 and digit > 7):
                return 0
            self.result = self.result * 10 + digit
        return self.result * sign
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))  # Output: 321
    print(solution.reverse(-123)) # Output: -321
    print(solution.reverse(120))   # Output: 21
    print(solution.reverse(0))     # Output: 0
    print(solution.reverse(1534236469)) # Output: 0 (overflow case)