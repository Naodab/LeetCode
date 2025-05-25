class Solution(object):
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ""

        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]
    
if __name__ == "__main__":
    solution = Solution()
    test_string = "babad"
    print("Longest Palindromic Substring of '{}': {}".format(test_string, solution.longestPalindrome(test_string)))
    test_string2 = "cbbd"
    print("Longest Palindromic Substring of '{}': {}".format(test_string2, solution.longestPalindrome(test_string2)))
        