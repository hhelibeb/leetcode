from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif A[i][0] > B[j][1]:
                j += 1
            else:
                result.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] < B[j][1]:
                    i = i + 1
                else:
                    j = j + 1

        return result


s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,24]]))