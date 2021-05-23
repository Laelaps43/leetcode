# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        m = 0
        while cur is not None:
            cur = cur.next
            m += 1
        n = m - n
        cur = head
        if n == 0:
            head = cur.next
        else:
            z = 0
            p = None
            while z != n:
                z += 1
                p = cur
                cur = cur.next
            p.next = cur.next
        return head