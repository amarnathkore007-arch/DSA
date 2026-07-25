class Solution:
    def unionArray(self, nums1, nums2):
        i = 0
        j = 0
        union = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                if len(union) == 0 or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
            else:
                if len(union) == 0 or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j += 1

        while i < len(nums1):
            if len(union) == 0 or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1

        while j < len(nums2):
            if len(union) == 0 or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1

        return union


# Call function
obj = Solution()

nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 3, 5]

result = obj.unionArray(nums1, nums2)
print(result)