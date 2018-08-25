class Solution(object):
    def twoSum(self, nums, target):
        for index,ele in enumerate(nums):
            ans = target - ele
            check_list = nums[:index] + nums[index+1:]
            print(check_list)
            if ans in check_list and (ele+ans)== target:
                return [index,nums.index(ans,index+1)]
            else:
                ans = 0
            return 0



y = Solution().twoSum([3,2,4],6)
print(y)


