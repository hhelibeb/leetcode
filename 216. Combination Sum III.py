from typing import List

class Solution:
    __k = 0
    __n = 0
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.__k = k
        self.__n = n
        result = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if k > 9:
            return
        self.dfsCombination(nums, 0, 0, [], result)
        return result

    def dfsCombination(self, nums: List[int], start, sum, temp: List[int], result: List[int]):
        if len(temp) == self.__k and sum == self.__n:
            result.append(list(temp))
        for i in range(start, len(nums)):
            temp.append(nums[i])
            sum = sum + nums[i]
            self.dfsCombination(nums, i+1, sum, temp, result)
            sum = sum - nums[i]
            temp.pop()


s = Solution()
print(s.combinationSum3(3, 15))
