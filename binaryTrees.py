# class Node:
#     left=None
#     right=None
#     def __init__(self,data,left,right) -> None:
#         self.data=data
#         self.left=left
#         self.right=right
#     def __repr__(self) -> str:
#         return f'node:{Node.data}->left:{Node.left}->right:{Node.right}'



def printLs(node):
    if node==None:return
    if (node.right==None and node.left==None):
        print(node.data)
    if(node.left!=None):
        printLs(node.left)
    if(node.right!=None):
        printLs(node.right)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeaves(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        print(node.data)
    printLeaves(node.left)
    printLeaves(node.right)

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Leaf nodes of the binary tree:")
printLs(root)
