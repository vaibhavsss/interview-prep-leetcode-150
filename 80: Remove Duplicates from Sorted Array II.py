class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array allowing at most two occurrences per element,
        modifies in-place, and returns the new length.
        
        We use a counter for occurrences and a write pointer (k). For each element,
        we allow up to 2 copies by checking the count before writing.
        """
        if len(nums) <= 2:
            return len(nums)  # Edge case: arrays with 0, 1, or 2 elements are already valid
        
        k = 2  # Start with the first two elements assumed valid
        
        # Iterate from the third element onward
        for i in range(2, len(nums)):
            # Write to k only if the current isn't equal to the two before it (allowing exactly two duplicates)
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        
        # k is the new length with at most two duplicates
        return k