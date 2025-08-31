# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        
        def is_mirror(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            
            return l.val == r.val and is_mirror(l.left, r.right) and is_mirror(l.right, r.left)
        return is_mirror(root.left, root.right)