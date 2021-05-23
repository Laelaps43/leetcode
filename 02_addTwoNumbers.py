# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = 0
        rehead = ListNode()
        while l1 or l2 or s:
            sum1 = 0
            if l1:
                sum1 = int(l1.val)
                l1 = l1.next
            if l2:
                sum1 = int(l2.val) + sum1
                l2 = l2.next
            s,y = divmod(sum1+s,10)
            node = ListNode(y)
            if rehead.next is None:
                rehead.next = node
            else:
                cur = rehead.next
                while cur.next is not None:
                    cur = cur.next
                cur.next = node
        return rehead.next
'''
while 可以通过0或者是1来判断是否是继续进行循环，如果只是判断l1 or l2,那么最后一次
有可能添加不到链表中去，所以我们在要进行判断是否要进行到最后一次循环了
'''









































