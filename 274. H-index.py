class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #using count sort
        # and last index as bucket for numbers greater than it.
        #To remember that h index is always less than or equal to number of papers.
        #If it is greater than number of papers then it is not possible to have h index as that number.
        v = len(citations)
        pcount=[0] * (v+1)

        for c in citations:
            pcount[min(v, c)]+=1

        h = v
        papers = pcount[v]

        while papers<h:
            h-=1
            papers += pcount[h]

        return h

        #Time complexity : O(n)
        #Space Complexity : O(n)