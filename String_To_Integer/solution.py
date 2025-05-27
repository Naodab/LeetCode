class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s.strip()
        result = 0
        sign = 1
        for i in range(len(s)):
            if s[i] == '-' and i == 0:
                sign = -1
            elif s[i] == '+' and i == 0:
                sign = 1
            elif s[i].isdigit():
                digit = int(s[i])
                print(digit)
                result = result * 10 + digit
                if result > (2**31 - 1):
                    return 2**31 - 1 if sign == 1 else -2**31
            else:
                break
        return result * sign

if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("2147483646"))