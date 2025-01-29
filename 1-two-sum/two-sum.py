class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]  # Return a list instead of a set
            else:
                map[num] = i

# Example usage
a = Solution()
num = [1, 2, 3, 4]
target = 7
print(a.twoSum(num, target))  # Output should be [2, 3]