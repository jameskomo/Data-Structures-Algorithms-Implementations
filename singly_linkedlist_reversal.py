"""
Singly Linked List Definition
"""
class ListNone:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
class ReverseLinkedList:
    def reverse(self, head):
        prev, current = None, head

        while current:
            # locate next node to move to
            next=current.next

            # reverse direction of the pointer
            current.next=prev
            prev=current
            current=next
        return prev
new_list=ReverseLinkedList.reverse([2,5,6,7],2)
