class Solution:
    def searchInsert(nums, target):
        left=0
        right=len(nums)-1
        while(left<=right):
            middle = (right+left)//2
            print(middle)
            if(target>nums[middle]):
                left = middle+1
            elif(target<nums[middle]):
                right = middle-1
            else:
                return middle
        return right
p = Solution
p.searchInsert([1,23,4,5],4)
