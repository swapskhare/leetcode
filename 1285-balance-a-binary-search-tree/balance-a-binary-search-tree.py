# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sortarr = []
        self.inorderTraverse(root)
        return self.sortedtoBST(0,len(self.sortarr)-1)

    def inorderTraverse(self, root:TreeNode) -> None:
        if not root:
            return
        self.inorderTraverse(root.left)
        self.sortarr.append(root)
        self.inorderTraverse(root.right)

    def sortedtoBST(self, start: int, end:int) -> TreeNode:
        if start > end:
            return None
        mid = (start + end)//2
        root = self.sortarr[mid]
        root.left = self.sortedtoBST(start, mid-1)
        root.right = self.sortedtoBST(mid+1, end)
        return root