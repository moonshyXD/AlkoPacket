class Solution(object):
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s = set(nums)
        d = dict()
        for i in s:
            d[i] = nums.count(i)

        sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_d[i][0])

        return result
