#include<stdio.h>
int searchInsert(int* nums, int numsSize, int target);
int main()
{
    int a[]={1,3,5};
    printf("%d",searchInsert(a,3,2));
    return 0;
}
int searchInsert(int* nums, int numsSize, int target){
    int left=0;
    int right=numsSize;
    int middle;
    while (left<right)
    {
        middle = (right+left)/2;
        if (target>nums[middle])
        {
            left = middle+1;
        }
        else if (target<nums[middle])
        {
            right = middle;
        }
        else
            return middle;
    }
    return right;
}
    