from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0;
        elif (root.right != None):
            recur = self.countNodes(root.right);
            pow = int(recur / 2) + 1
            return 2**pow + recur;
        elif (root.left != None):
            return 2;
        else:
            return 1;


sol = Solution();
four = TreeNode(4, None, None);
two = TreeNode(2, four, None);
three = TreeNode(3, None, None);
one = TreeNode(1, two, three);
print(sol.countNodes(one));