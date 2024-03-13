"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.

Constraints:
The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000

Input: head = [1,2,3,-3,-2]
Output: [1]
"""

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            curr = head
            list = []
            while curr is not None:
                if curr.val != 0:
                    list.append(curr.val)
                curr = curr.next

            if len(list) >=2:
                n = 0
                while n < len(list) - 1:
                    sum = list[n]
                    index = n
                    for i in range(n+1, len(list)):
                        sum += list[i]
                        index += 1
                        if sum == 0:
                            list = list[: n] + list[index + 1:]
                            n = 0
                            index = 0
                            break
                    if index == len(list) - 1:
                        n += 1

            if list:
                head = ListNode(list[0]) 
                curr = head  
                if len(list) > 1:            
                    for l in list[1:]:
                        curr.next = ListNode(l)
                        curr = curr.next
                return head
            return None
          
