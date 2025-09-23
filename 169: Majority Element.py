class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in nums (appears more than n/2 times).
        
        We use Boyer-Moore Voting Algorithm: maintain a candidate and a count.
        Increment count when matching candidate, decrement otherwise. Reset candidate when count hits zero.
        This works because the majority element will dominate in the end.
        """
        candidate = None  # Potential majority element
        count = 0  # Vote counter
        
        # Single pass to find the candidate
        for num in nums:
            if count == 0:
                candidate = num  # New candidate when count resets
            # Vote up if matches, down otherwise
            count += (1 if num == candidate else -1)
        
        # Since a majority is guaranteed, candidate is the answer
        return candidate