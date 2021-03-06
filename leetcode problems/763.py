763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.



class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic={}
        for i,j in enumerate(S):
        dic[j]=i
        answer=[]
        anchor=0
        j=0
        for i,k in enumerate(S):
            j=max(j,dic[k])
            if i==j:
                answer.append(i-anchor+1)
                anchor=i+1
        return answer
