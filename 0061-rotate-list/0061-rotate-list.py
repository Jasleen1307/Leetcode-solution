# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
    if head is None or head.next is None:
        return head

    temp = head
    count = 0

    while temp is not None:
        count += 1
        temp = temp.next

    k = k % count

    if k == 0:
        return head

    temp = head

    for i in range(count - k - 1):
        temp = temp.next

    newHead = temp.next
    temp.next = None

    curr = newHead
    while curr.next is not None:
        curr = curr.next

    curr.next = head

    return newHead