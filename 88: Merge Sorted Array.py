class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        This function merges two sorted arrays nums1 and nums2 into nums1.
        nums1 has enough space at the end to hold all elements from nums2.
        We use a two-pointer approach starting from the end to avoid overwriting elements.
        """
        # Initialize pointers: i for nums1's valid elements, j for nums2, k for the end of nums1
        i = m - 1  # Last index of initial elements in nums1
        j = n - 1  # Last index of nums2
        k = m + n - 1  # Last index of the merged array in nums1
        
        # Merge from the end until we've exhausted nums2
        while j >= 0:
            # If nums1's current element is larger, place it at k
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            # Otherwise, place nums2's element at k
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1  # Move to the next position in the merged array