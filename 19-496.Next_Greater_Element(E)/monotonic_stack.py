from typing import List

"""
-  Here let's first find output for all the elements of array in nums2 (using monotonic stack approach).
- Then we would somehow have to get output for elements only in nums1. to achieve this
we first create hashmap such that we will remember each element's index in nums2 in hashmap.

i.e, iterate through nums2 and create hm values such that each element of num2 index is in hm.

**Details**

Step 1: First let's create hmap from nums2

nums2 = [1,3,4,2]
hm = {
    1 : 0,
    3 : 1,
    4 : 2,
    2 : 3
}

Step 2 - Populate nums2_output array using monotonic stack method for all elements of nums2
nums2 =  [1,3,4,2]
nums2_output = [3,4,-1,-1]

Step 3 - We will traverse nums1 and populate final_output by using hmap prepared in step1
nums1 =  [4,1,2]
for every element of nums1, check hmap and get the position and get the value from nums2_output for that position
output = [-1, 3, -1]
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # step 1 - Create a hashmap
        hmap = {value: key for key, value in enumerate(nums2)}

        # step 2 - Populate nums2_output using monotonic stack (decreasing) method

        m_stack = [nums2[-1]]  # since the first element in the stack is always the last number of nums2 - we are
        # iterating from end
        nums2_output = [-1]  # -1 for last element as there are no elements that are next to last element
        for i in range(len(nums2) - 2, -1, -1):
            current = nums2[i] # [6,5,4,3,2,1,7]

            if m_stack[-1] > current:
                nums2_output.insert(0, m_stack[-1])
                m_stack.append(current)
            else:
                while len(m_stack) != 0:
                    if m_stack[-1] < current:
                        m_stack.pop()
                    else:
                        nums2_output.insert(0, m_stack[-1])
                        m_stack.append(current)
                        break
                else:
                    nums2_output.insert(0, -1)
                    m_stack.append(current)

        print(nums2_output)
        print(m_stack)

        # Step 3 - Traverse nums1 and populate final output using hmap

        final_output = []
        for num in nums1:
            if num in hmap:
                index = hmap[num]
                final_output.append(nums2_output[index])

        return final_output

#
# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# result = Solution().nextGreaterElement(nums1, nums2)
# print(result)

nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
result = Solution().nextGreaterElement(nums1, nums2)
print(result)