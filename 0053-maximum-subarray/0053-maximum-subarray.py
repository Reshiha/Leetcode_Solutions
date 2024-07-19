class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            temp = curSum + nums[i]
            if temp<nums[i]:
                curSum = nums[i]
            else:
                curSum = temp
            if maxSum<curSum:
                maxSum = curSum
        return maxSum
        