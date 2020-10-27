"""
Understand:
Example 1 (just one node):
    3

min-depth = 1 (3)

Example 2 (one subtree is shorter, this is already given in the problem):
    3
   / \
  9  20
    /  \
   15   7

min-depth = 2 (3->9)

Example 1 (a degenerate tree):
    3
     \
     20
      \
      7

min-depth = 3 (3->20->7)

Plan:
You can use DFS and output the minimum depth or use BFS which is better on average
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = [(root, 1)]
        while len(queue) > 0:
            curr = queue.pop(0)
            currNode, currLevel = curr[0], curr[1]
            if currNode.left == None and currNode.right == None:
                return currLevel
            if currNode.left != None:
                queue.append((currNode.left, currLevel + 1))
            if currNode.right != None:
                queue.append((currNode.right, currLevel + 1))
        return -1
