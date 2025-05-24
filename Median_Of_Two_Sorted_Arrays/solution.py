class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = 0
        y = 0
        m = len(nums1)
        n = len(nums2)
        merged = []
        while x < m and y < n:
            if nums1[x] < nums2[y]:
                merged.append(nums1[x])
                x += 1
            else:
                merged.append(nums2[y])
                y += 1

        while x < m:
            merged.append(nums1[x])
            x += 1
        
        while y < n:
            merged.append(nums2[y])
            y += 1

        total_length = m + n
        mid = total_length // 2
        if total_length % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return merged[mid]

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2, 5]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2)) # Output: 2.5