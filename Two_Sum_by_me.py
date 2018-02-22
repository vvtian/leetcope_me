# _*_ coding: utf-8 _*_
#by me! haha
class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            for j in nums[nums.index(i)+1:]:
                if i + j == target:
                    so = [nums.index(i),nums.index(j,nums.index(i)+1)]
                    return so


            

y = Solution().twoSum([3, 3],6)
print(y)

        