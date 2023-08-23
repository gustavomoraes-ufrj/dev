# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root):
    if not root: #Base Case
        return root
    self.invertTree(root.left) #Call the left substree
    self.invertTree(root.right)  #Call the right substree
    # Swap the nodes
    root.left, root.right = root.right, root.left
    return root # Return the root      

root = TreeNode(2,1,3)

print(root.val)
print(root.left)
print(root.right)
