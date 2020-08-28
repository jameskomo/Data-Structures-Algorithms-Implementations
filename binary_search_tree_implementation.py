# Python program to for tree traversals -Preorder, Inorder and Postorder

# A class that represents an individual node in a 
# Binary Tree 

class Node:
    def __init__(self, key):
        self.right=None
        self.left=None
        self.data=key 
    
def preorder(root):
    if root:
        # First print the data of node 
        print(root.data, end=" ")
        # Then recur on left child 
        preorder(root.left)
        # Then recur on right child 
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
    

def postorder(root):
    if root:
        postorder(root.right)
        print(root.data, end=" ")
        postorder(root.left)



root = Node(1) 
root.left	 = Node(2) 
root.right	 = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)

#      1
#      / \
#    2   3
#    /\    \
#   4  5

print("PREORDER")
preorder(root)
print("\n")
print("INORDER\n")
inorder(root)
print("\n")
print("POSTORDER\n")
postorder(root)
print("\n")
# print (f"Preorder traversal of binary tree is", {preorder(root)})
# print (f"Inorder traversal of binary tree is", {inorder(root)})
# print (f"Postorder traversal of binary tree is", {postorder(root)})

# SPACE COMPLEXITY
# Auxiliary Space : If we don’t consider size of stack for function calls then O(1) 
# otherwise O(n).

# TIME COMPLEXITY
# Time Complexity: O(n)