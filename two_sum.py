class Solution:
    def twoSum(self, nums: list[int], target: int) ->list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return []

nums = [2,7,11,15]
target = 9

so = Solution()
ret = so.twoSum(nums, target)
print(ret)
