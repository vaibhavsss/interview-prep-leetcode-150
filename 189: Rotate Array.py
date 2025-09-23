class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.
        
        Approach: Reverse the entire array, then reverse first k elements, then reverse the rest.
        Normalize k to avoid redundant rotations (k > n).
        """
        n = len(nums)
        k = k % n  # Normalize k to handle cases where k >= n
        if k == 0:
            return  # No rotation needed
        
        # Helper function to reverse elements in range [start, end]
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse entire array
        reverse(0, n - 1)
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        # Step 3: Reverse remaining elements
        reverse(k, n - 1)