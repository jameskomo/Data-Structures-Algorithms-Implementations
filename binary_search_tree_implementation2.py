class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree():
    def __init__(self,root):
        self.root=Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type=="preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type=="inorder":
            return self.inorder_print(tree.root, "")
        if traversal_type=="postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type" +str(traversal_type)+ "is not supported")
            return False

    def preorder_print(self, start, traversal):# start is the node that will be updated on every recursive call and traversal is the string to be printed on string
         """"Root->Left->Right"""
         
         #if node given is None
         if start:
             traversal+=(str(start.value)+"-")
             traversal=self.preorder_print(start.left, traversal)
             traversal=self.preorder_print(start.right, traversal)           
         return traversal
    def inorder_print(self, start, traversal):# start is the node that will be updated on every recursive call and traversal is the string to be printed on string
         """"Left->Root->Right"""
         
         #if node given is None
         if start:
             traversal=self.preorder_print(start.left, traversal)
             traversal+=(str(start.value)+"-")
             traversal=self.preorder_print(start.right, traversal)           
         return traversal

    def postorder_print(self, start, traversal):# start is the node that will be updated on every recursive call and traversal is the string to be printed on string
         """"Right->Root->Left"""
         
         #if node given is None
         if start:
             traversal=self.preorder_print(start.right, traversal) 
             traversal+=(str(start.value)+"-")
             traversal=self.preorder_print(start.left, traversal)        
         return traversal


#      1
#    /   \
#   2     3
#  / \   /  \
# 4   5  6   7
# POPULATING TREE WITH DATA
tree=BinaryTree(1) #Initial value of root node
tree.root.left=Node(2) #First left child value
tree.root.right=Node(3) #First right child value
tree.root.left.left=Node(4) #Second root-left-left child value
tree.root.left.right=Node(5) #Second root-left-right child value
tree.root.right.left=Node(6) #Second root-right-left child value
tree.root.right.right=Node(7) #Second root-right-left child value

print("******PREORDER******")
print(tree.print_tree("preorder"))
print("******INORDER******")
print(tree.print_tree("inorder"))
print("******POSTORDER******")
print(tree.print_tree("postorder"))

