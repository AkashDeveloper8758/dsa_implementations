

from typing import List

# 2528. Maximize the Minimum Powered City : https://leetcode.com/contest/biweekly-contest-95/problems/maximize-the-minimum-powered-city/
class Solution:
    def isGood(self,stations,r,k,power):
        n= len(stations)
        extraAllocations = [0] * n
        windowPower = sum(stations[:r])
        for i in range(n):
            if i+r < n:
                windowPower += stations[i+r]
            if windowPower < power:
                diff = power - windowPower
                if diff > k:
                    return False
                extraAllocations[min(n-1,i+r)] += diff
                k -= diff
                windowPower = power
            if i-r >= 0:
                windowPower -= stations[i-r] + extraAllocations[i-r]
        return True


    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        high = sum(stations) + k
        low = 0
        ans = 0
        while low <= high:
            m = (low + high)//2
            if self.isGood(stations,r,k,m):
                ans = m
                low = m + 1
            else:
                high = m-1
        return ans
