# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self,head):
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        #Find middle
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #Reverse second half
        second=self.reverseLL(slow.next)
        #Cut the first half
        slow.next=None
        #Merge alternatively
        first=head
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2




