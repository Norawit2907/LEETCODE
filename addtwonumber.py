# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        list1 = []
        while h1 != None:
            list1.append(h1.val)
            h1 = h1.next

        h2 = l2
        list2 = []
        while h2 != None:
            list2.append(h2.val)
            h2 = h2.next

        num1, num2 = 0, 0
        for ci, i in enumerate(list1):
            num1 += i * pow(10, ci)
        for ci, i in enumerate(list2):
            num2 += i * pow(10, ci)

        num3 = str(num1 + num2)
        l3 = []
        for i in num3[::-1]:
            l3.append(ListNode(i))
        for i in range(len(l3)-1):
            l3[i].next = l3[i+1]
        return(l3[0])
       
    
# list1 = []
# h1 = None
# for i in [2,4,3]:
#     list1.append(ListNode(i))
# for i in range(len(list1)-1):
#     list1[i].next = list1[i+1]
# h1 = list1[0]

# list2 = []
# for i in [5,6,4]:
#     list2.append(ListNode(i))
# for i in range(len(list2)-1):
#     list2[i].next = list2[i+1]
# h2 = list2[0]

# sol = Solution()
# print(sol.addTwoNumbers(h1, h2))

