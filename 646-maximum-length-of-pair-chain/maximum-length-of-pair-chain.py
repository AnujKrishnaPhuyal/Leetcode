class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])  # Sort by ending value
        curr_end = float('-inf')
        chain_length = 0

        for pair in pairs:
            if pair[0] > curr_end:  # If current pair can be chained
                chain_length += 1
                curr_end = pair[1]  # Update last selected pair's end
                
        return chain_length
