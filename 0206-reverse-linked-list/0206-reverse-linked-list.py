# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        Curr=head
        while Curr is not None:
            nextNode=Curr.next
            Curr.next=prev
            prev=Curr
            Curr=nextNode
        return prev     
        