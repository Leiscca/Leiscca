from typing import List

class Solution:
    def maxSub(self, arr: List[int]) -> int:
        ret = arr[0]
        sum = arr[0]

        l = len(arr)
        for idx in range(1, l):
            if sum < 0:
                sum = arr[idx]
            else:
                sum += arr[idx]
            ret = max(ret, sum)
        return ret
    
s = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"{s.maxSub(arr)}")