"""
Not doing a bruteforce code for this as it is similar to above 2 problems 21 and 22.
We will come back and code if necessary
"""


class Solution:
    def search(self, pat, txt):

        i, j = 0, 0
        count, anagram_count = 0, 0
        pat_map = {}  # to store pattern char count {a:3, b:1} in 'aaba'

        for char in pat:
            pat_map[char] = pat_map.get(char, 0) + 1

        # count is number of keys in pat_map. We will use this for
        # optimization purpose as explained below the code
        count = len(pat_map)

        while j < len(txt):
            # accumulate the results (when window size is hit below to
            # pat length we will deal with this result)
            if txt[j] in pat_map:
                pat_map[txt[j]] -= 1
                if pat_map[txt[j]] == 0:
                    count -= 1

            # window size not reached yet, so we just increment j
            if j-i+1 < len(pat):
                j += 1

            # window size reached, so we can do some calculation
            elif j-i+1 == len(pat):
                if count == 0:
                    anagram_count += 1

                # we have to now reverse the calculations we did for ith position before sliding the window
                if txt[i] in pat_map:
                    pat_map[txt[i]] += 1
                    if pat_map[txt[i]] == 1:
                        count += 1
                # at this point we have successfully reverted the
                # calculations for ith position we had done in acc phase, so now we can slide our window further

                i += 1
                j += 1

        return anagram_count


# result = Solution().search(pat='aaba', txt='aabaabaa') # you should get 4
result = Solution().search(pat='for', txt='forxxorfxdofr')  # you should get 3
print(result)



"""
Why do we use count?

pat_map = {a:3, b:1}, count = 2 # 2 because there are 2 keys in pat_map

Let's say I have this pat_map that I created during accumulator phase (first block of code in while (j < arr.length).
I now need to use this in block where window size is reached. At that time, the task would be 
to check if each key is 0, and then if that is the case, add 1 to the result saying we found anagram.
So we could optimize this check and maintain a count variable. Whenever a key becomes 0, we decrement the count 
in accumulator phase. 

By doing this, when the window size is reached, we don't have to traverse entire pat_map to check if all keys
are 0. Instead we could just check if count == 0 which would mean all keys are 0.     
"""