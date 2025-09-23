class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place and returns the new length.
        
        Since the array is sorted, we can use a two-pointer approach: slow (k) tracks unique elements,
        fast (i) scans ahead. We only advance k when a new unique element is found.
        """
        if not nums:
            return 0  # Edge case: empty array
        
        k = 1  # Start from 1 since the first element is always unique
        
        # Iterate from the second element onward
        for i in range(1, len(nums)):
            # If current element differs from the previous unique one, place it at k
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        # k is the count of unique elements
        return k