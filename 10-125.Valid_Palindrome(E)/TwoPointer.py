# we will solve this using two pointer approach

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            while left_ptr < right_ptr and not self.is_alphanumeric(s[left_ptr]):
                left_ptr += 1

            while right_ptr > left_ptr and not self.is_alphanumeric(s[right_ptr]):
                right_ptr -= 1

            if s[left_ptr].lower() != s[right_ptr].lower():
                return False

            left_ptr += 1
            right_ptr -= 1

        return True

    @staticmethod
    def is_alphanumeric(c):
        # check if c is between a to z, or A-Z or 0-9
        return ord("a") <= ord(c) <= ord("z") \
            or ord("A") <= ord(c) <= ord("Z") \
            or ord('0') <= ord(c) <= ord('9')


result = Solution()
print(result.isPalindrome("A man, a plan, a canal: Panama"))
