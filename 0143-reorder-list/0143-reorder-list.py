# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the middle of the list 
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse the second half 
        second = slow.next #4
        prev = slow.next = None
        while second:
            tmp = second.next #5
            second.next = prev  #nONE
            prev = second #4
            second = tmp #5
        #merge 2 halfs
        first,second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
            
            
            
        
        
        
        