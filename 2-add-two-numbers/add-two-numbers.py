# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      main = ListNode()
      ans=main
      carry=0
      while l1!=None or l2!=None or carry:
        sum = carry
        if l1!=None:
            sum+=l1.val
            l1=l1.next
        if l2!=None:
            sum+=l2.val
            l2=l2.next
        
        carry = sum//10

        ans.next = ListNode(sum%10)
        ans=ans.next

      return main.next
            
                


        