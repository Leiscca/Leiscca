from typing import List, Optional

# find dup num from an int arr
class Solution:
    def find_dup(self, arr: List[int]) -> int:
        t = arr[0]
        h = arr[0]
        print(f"tortoise: {t}, hare: {h}")

        t = arr[t]
        h = arr[arr[h]]
        while(t != h):
            print(f"tortoise: {t}, hare: {h}")
            t = arr[t]
            h = arr[arr[h]]
            print(f"tortoise: {t}, hare: {h}")

        # phase 2: find the dup
        t = arr[0]
        while(t != h):
            t = arr[t]
            h = arr[h]
        return t

s = Solution()
arr = [1, 3, 4, 2, 3, 2]
print(f"dup: {s.find_dup(arr)}")