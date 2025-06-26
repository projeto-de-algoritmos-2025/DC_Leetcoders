from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        enum = list(enumerate(nums))

        def merge_sort(start, end):
            if end - start <= 1:
                return enum[start:end]

            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)

            merged = []
            i = j = 0
            count_right_smaller = 0

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    result[left[i][0]] += count_right_smaller
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count_right_smaller += 1
                    j += 1

            while i < len(left):
                result[left[i][0]] += count_right_smaller
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            enum[start:end] = merged
            return merged

        merge_sort(0, n)
        return result
