from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        temp = []
        if intervals:
            temp += intervals[0]
        if len(intervals) == 1:
            result = intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] <= temp[1]:
                temp[1] = max(intervals[i][1], temp[1])
            else:
                result.append(list(temp))
                temp = intervals[i]
            if i == len(intervals) - 1:
                result.append(list(temp))
        return result
