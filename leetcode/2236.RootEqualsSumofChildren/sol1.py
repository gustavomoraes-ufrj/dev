# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root):
    # As per the def of binary tree node, we can compare the root value \
    # with the TreeNode function, the root.left.val retrieves value of left node \
    # the root.right.val retrieves value of right node. '==' compares two values
    if root.val == root.left + root.right:  
        return True
    else:
        return False

root1 = TreeNode(3,2,2)    
print(checkTree(root1))
