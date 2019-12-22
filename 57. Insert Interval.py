from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(0, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(list(newInterval))
                result += intervals[i:]
                return result
            elif newInterval[0] > intervals[i][1]:
                result.append(list(intervals[i]))
            else:
                newInterval = self.merge(newInterval, intervals[i])
        if newInterval: result.append(newInterval)
        return result

    def merge(self, in1: List[int], in2: List[int]) -> List[int]:
        return [min(in1[0], in2[0]), max(in1[1], in2[1])]


s = Solution()
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))