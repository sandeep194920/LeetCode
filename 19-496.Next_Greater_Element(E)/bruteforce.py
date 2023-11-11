from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1 for e in nums1]
        hmap = {val: key for key, val in enumerate(nums1)}
        for i in range(len(nums2)):
            if nums2[i] in hmap:
                j = i + 1
                while j < len(nums2):
                    if nums2[j] > nums2[i]:
                        output[hmap[nums2[i]]] = nums2[j]
                        break
                    j = j+1
        return output


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
result = Solution().nextGreaterElement(nums1, nums2)
print(result)
