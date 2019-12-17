from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0:
            return
        if tomatoSlices > cheeseSlices * 4 or tomatoSlices < cheeseSlices * 2:
            return
        jumbo = 0
        smallRight = tomatoSlices / 2
        smallLeft  = 0
        cheeseTemp = jumbo + smallRight
        if cheeseTemp == cheeseSlices:
            return ([int(jumbo), int(smallRight)])
        while True:
            smallMid = smallRight - int((smallRight-smallLeft )/4) * 2
            jumbo = int((tomatoSlices - smallMid*2)/4)
            cheeseTemp = jumbo + smallMid
            if cheeseTemp == cheeseSlices and ( 4 * jumbo + 2 * smallMid ) == tomatoSlices:
                return([int(jumbo), int(smallMid)])
            if smallRight < 0:
                return
            if cheeseTemp > cheeseSlices:
                smallRight = smallMid - 1
            if cheeseTemp < cheeseSlices:
                smallLeft  = smallMid + 1
            if cheeseTemp == cheeseSlices:
                smallRight = smallMid - 1
S = Solution()

print( S.numOfBurgers(4,16))
print(28087*4+841652*2)
