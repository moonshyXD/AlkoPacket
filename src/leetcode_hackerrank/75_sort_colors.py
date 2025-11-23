class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = nums.count(0)
        w = nums.count(1)
        s = nums.count(2)
        for i in range(len(nums)):
            if i < k:
                nums[i] = 0
            elif i < k + w:
                nums[i] = 1
            elif i < k + w + s:
                nums[i] = 2
