# class Solution(object):
#     def numberToWords(self,nums, target):
#         list_index = []
#         for one in nums:
#             one_index = nums.index(one)
#             a = target - one
#             if a in nums[one_index+1:]:
#                 list_index.append(one_index)
#                 another = nums.index(a, one_index+1)
#                 print([one_index,another])
#                 break
#
#
# nums = [-1,-2,-3,-4,-5]
# target = -8
# a = Solution()
# a.numberToWords(nums, target)



def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                continue
            else:
                j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2
                break
    if j>0:
        return [i,j]
    else:
        return []
nums = [3,3]
target = 6
print(twoSum(nums,target))



# class Solution:
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#
#         return []
#
# nums = [-1,-2,-3,-4,-5]
# target = -8
# a = Solution()
# print(a.twoSum(nums, target))



# class Solution:
#     def twoSum(self, nums, target):
#         hashtable = dict()
#         for i, num in enumerate(nums):
#             if -5 in hashtable:
#                 return [hashtable[target - num], i]
#             hashtable[nums[i]] = i
#             print(hashtable)
#         return []
#
# nums = [-1,-2,-3,-4,-5]
# target = -8
# a = Solution()
# a.twoSum(nums, target)


