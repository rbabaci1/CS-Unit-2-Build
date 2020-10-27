"""
Understand:
input: 16
output: 4

input: 8
output: 2 (actually 2.82)

input: 1
output: 1

Plan:
Use binary search to keep halving search space
Keep track of nearest solution found (in else case)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        min, max = 0, x
        res = 0
        while min <= max:
            mid = int((min + max) / 2)
            squared = mid * mid
            if squared == x:
                return int(mid)
            elif squared > x:
                max = mid - 1
            else:
                min = mid + 1
                res = mid
        return int(res)

class Solution:
    def mySqrtBruteForce(self, x: int) -> int:
        for i in range(0, x + 1):
            squared = i * i
            if squared == x:
                return i
            elif squared > x:
                return i - 1
        return -1
