# 1. CREATING NODE CLASS
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
# CREATING LINKED LIST CLASS
class LinkedList:
    def __init__(self):
        self.head=None #Initially points to none

    # FUNCTION FOR PRINTING LISTS
    def print_list(self):
        current_node=self.head
        while current_node:#While current node is not None
            print(current_node.data)
            current_node=current_node.next #Hop to next node

    # INSERTING INTO LINKED LIST AT END POSITION

    def append(self, data):#insert node with data
        new_node=Node(data) #create new node object
        if self.head is None: #check is a node in list
            self.head=new_node
            return
         #if new list if not empty and there is other nodes in list
         #TRAVERSING THROUGH NODES TO INSERT AT CERTAIN POINT
        last_node=self.head 
        while last_node.next: #While next pointer is not null
            last_node=last_node.next #update last_node to point to the next node
        #WHILE LAST_NODE.NEXT IS NULL (END OF LIST)
        last_node.next   =new_node #Appends new node to end of list
    
    # INSERTING INTO LINKED LIST AT FIRST/FRONT POSITION

    def prepend(self, data):#insert node with data
        new_node=Node(data) #create new node object
        new_node.next=self.head #If a new node is inserted at the first position the current head becomes the second node in position
        self.head=new_node #Head of list becomes node inserted in first position

    #INSERTING AFTER A GIVEN NODE   
    def insert_after_node(self, previous_node, data):
        if not previous_node:
            print("Previous Node is not in the list")
            return
        new_node=Node(data)
        new_node.next=previous_node.next 
        previous_node.next=new_node
# Creating Linked List Object
llist=LinkedList()

# Inserting into Linked List using Defined Append function
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

# Adding to Front Position using Prepend
llist.prepend("E")

# Insert Node after a Given Node
llist.insert_after_node(llist.head.next, "J") #llist.head.next Specifies that we want to insert after B(head{A}.next{B})
#//E-A-J-D-C-D


llist.print_list()