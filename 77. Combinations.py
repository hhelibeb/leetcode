class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        all = []
        result = []
        for i in range(1, n+1):
            all += [i]
        self.dfsCombine(all, k, 0, [], result)
        return result
    def dfsCombine(self, nums: List[int], k, start, temp: List, result: List[List[int]]):
        if len(temp) == k:
            result += [list(temp)]
        for i in range(start, len(nums)):
            temp += [nums[i]]
            if len(temp) > k:
                temp.pop()
                continue
            self.dfsCombine(nums, k, i+1, temp, result)
            temp.pop()



s = Solution()
print(s.combine(4,2))
