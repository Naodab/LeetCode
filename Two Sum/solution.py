class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        historial = {}
        result = []

        for i in range(len(nums)):
            objective = target - nums[i]
            if objective not in historial:
                historial[nums[i]] = objective
            else:
                result.append(nums.index(objective))
                result.append(i)

        return result
                
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(s.twoSum([3, 2, 4], 6))        # Output: [1, 2]
    print(s.twoSum([3, 3], 6))           # Output: [0, 1]
    print(s.twoSum([1, 2, 3], 5))        # Output: [1, 2]