class Solution(object):
    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[right] = nums[right], nums[i]
        return i

    def findKthLargest(self, nums, k):
        n = len(nums)
        target = n - k

        left, right = 0, n - 1
        while True:
            p = self.partition(nums, left, right)
            if p == target:
                return nums[p]
            elif p < target:
                left = p + 1
            else:
                right = p - 1
