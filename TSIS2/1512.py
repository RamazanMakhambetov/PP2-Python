class Solution(object):
    def numIdenticalPairs(self, nums):
        nums, cnt = [], 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    cnt += 1
        
        return cnt