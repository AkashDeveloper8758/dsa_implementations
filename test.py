from typing import List

class Solution:
    def isGood(self,stations,r,minPowerRequired, k):
        n = len(stations)
        windowPower = sum(stations[:r])  # init windowPower to store power of 0th city (minus stations[r])
        additions = [0] * n
        for i in range(n):
            if i + r < n:  # now, windowPower stores sum of power stations from [i-r..i+r], it also means it's the power of city `ith`
                windowPower += stations[i + r]

            if windowPower < minPowerRequired:
                needed = minPowerRequired - windowPower
                if needed > k:  # Not enough additional stations to plant
                    return False
                # Plant the additional stations on the farthest city in the range to cover as many cities as possible
                additions[min(n - 1, i + r)] += needed
                windowPower = minPowerRequired
                k -= needed

            if i - r >= 0:  # out of window range
                windowPower -= stations[i - r] + additions[i - r]

        return True
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        left = 0
        right = sum(stations) + k  # The answer = `right`, when `r = n`, all value of stations are the same!
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if self.isGood(stations,r,mid, k):
                ans = mid  # This is the maximum possible minimum power so far
                left = mid + 1  # Search for a larger value in the right side
            else:
                right = mid - 1  # Decrease minPowerRequired to need fewer additional power stations
        return ans

sol = Solution()
arr = [4,4,4,4]
res = sol.maxPower(arr,0,3)
print('res : ',res)


