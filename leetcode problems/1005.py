# 1005. Maximize Sum Of Array After K Negations
#
# Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)
#
# Return the largest possible sum of the array after modifying it in this way.
#
# Example 1:
#
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].
# Example 2:
#
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
# Example 3:
#
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
#

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        i=0
        while i <K:
            min_element=min(A)
            min_element_index=A.index(min_element)
            A[min_element_index]*=-1
            i+=1
        return sum(A)
