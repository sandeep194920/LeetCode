import math


class Solution:
    def findPages(self, A, N, M):
        # M -> Number of students
        # N -> Number of Books
        # A -> Books array

        # Array is sorted, so we take start as smallest pages as book 1, A[0]
        # and we take the highest pages as addition of all remaining books

        # Edge case -> Number of books should always be => than number of students
        if N < M:
            return -1

        start = max(A)  # I initially thought this must be the smallest element, but I was wrong.
        # start must be maximum because
        end = sum(A)
        min_pages = 0

        # for i in range(len(A) - 1):
        #     start += A[i]

        while start <= end:
            max_pages = math.floor(start + (end - start) / 2)
            if self.isValid(A, max_pages, M):
                min_pages = max_pages
                end = max_pages - 1
            else:
                start = max_pages + 1

        return min_pages

    def isValid(self, books, max_pages, max_students) -> bool:
        cur_student = 1
        pages = 0

        for i in range(len(books)):
            pages = pages + books[i]

            if pages > max_pages:
                cur_student += 1
                pages = books[i]

                if cur_student > max_students:
                    return False

        return True


# result = Solution().findPages([12, 34, 67, 90], 4, 2)
result = Solution().findPages([13, 31, 37, 45, 46, 54, 55, 63, 73, 84, 85], 11, 9)

print(result)
