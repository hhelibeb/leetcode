from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = [1,2,3,4,5,6,7,8,9]
        result = []
        self.dfsSeqDigits(nums, 0, [], result, low, high)
        result.sort()
        return result

    def dfsSeqDigits(self, nums: List[int], start, temp: List[int], result: List[int], low, high):
        if temp:
            number = int(''.join(str(i) for i in temp))
            if number >= low and number <= high:
                result.append(number)
        for i in range(start, len(nums)):
            if temp:
                if i > start and (nums[i] - temp[-1]) != 1:
                  continue
            temp.append(nums[i])
            self.dfsSeqDigits(nums, i+1, temp, result, low, high)
            temp.pop()


s = Solution()
print(s.sequentialDigits(10,9999))
