from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dictory = {}
        j = 0
        for i in inorder:
            dictory[i] = j
            j = j + 1
        return self.buildTreeHelper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, dictory)

    def buildTreeHelper(self, preorder, pstart, pend, inorder, istart, iend, dictory):
        if pend < pstart:
            return None
        root = TreeNode(preorder[pstart])
        rootIndexInOrder = dictory.get(root.val)
        leftLength = rootIndexInOrder - istart
        root.left = self.buildTreeHelper(preorder, pstart + 1, pstart + leftLength, inorder, istart, rootIndexInOrder - 1, dictory)
        root.right = self.buildTreeHelper(preorder, pstart + leftLength + 1, pend, inorder, rootIndexInOrder + 1, iend, dictory)
        return root

