class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        temp = x
        reversed_num = 0
        while temp > 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
        return x == reversed_num
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(122221))