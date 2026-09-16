# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 
        # i
        #[1, 2]
        curr = head
        prev = head
        i = 0
        size = 0
        while curr:
            size += 1
            curr = curr.next
        curr = head
        n = size - n
        print(n, size)
        while curr:
            if i == n:
                if size == 1:
                    head = None
                elif prev == curr:
                    head = head.next
                else:
                    prev.next = curr.next
            prev = curr
            curr = curr.next
            i += 1
        return head
            