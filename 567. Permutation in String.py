from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}
        left = 0
        if len(s1) > len(s2): return False
        for s in s1:
            times = countS1.get(s, 0) + 1
            countS1.update({s: times})
        for i in range(0, len(s1)):
            times = countS2.get(s2[i], 0) + 1
            countS2.update({s2[i]: times})
        for right in range(len(s1), len(s2)):
            if countS2 == countS1:
                return True
            else:
                times = countS2.get(s2[right], 0) + 1
                countS2.update({s2[right]: times})
                countS2[s2[left]] = countS2[s2[left]] - 1
                if countS2[s2[left]] == 0:
                    countS2.pop(s2[left])
                left = left + 1
        return countS2 == countS1



s = Solution()
print(s.checkInclusion('adc','dcda'))
# "ky"
# "ainwkckifykxlribaypk"
