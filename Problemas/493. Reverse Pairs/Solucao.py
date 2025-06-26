class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(start: int, end: int) -> int:
            if end - start <= 1:
                return 0

            meio = (start + end) // 2
            count = merge_sort(start, meio) + merge_sort(meio, end)

            # Contando os pares reversos
            j = meio
            for i in range(start, meio):
                while j < end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - meio

            # Merge das duas partes
            temp = []
            i, j = start, meio
            while i < meio and j < end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i < meio:
                temp.append(nums[i])
                i += 1
            while j < end:
                temp.append(nums[j])
                j += 1

            nums[start:end] = temp
            return count

        return merge_sort(0, len(nums))
