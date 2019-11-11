895. Maximum Frequency Stack

Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:

Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].


from collections import Counter,defaultdict
class FreqStack:

    def __init__(self):
        self.freq=Counter()
        self.map_of_stacks=defaultdict(list)
        self.max_freq=0

    def push(self, x: int) -> None:
        self.freq[x]+=1
        self.max_freq=max(self.max_freq,self.freq[x])
        self.map_of_stacks[self.freq[x]].append(x)


    def pop(self) -> int:
        val=self.map_of_stacks[self.max_freq].pop()
        if self.map_of_stacks[self.max_freq]==[]:
            self.max_freq-=1
        self.freq[val]-=1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
