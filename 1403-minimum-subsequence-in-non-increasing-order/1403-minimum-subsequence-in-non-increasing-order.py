class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        ans = []
        total = sum(nums)
        subsequence_sum = 0
        for num in nums:
            subsequence_sum += num
            ans.append(num)
            if subsequence_sum > total - subsequence_sum:
                break
        return ans