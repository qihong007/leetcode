'''
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
返回 false 。

示例3：
      1
     / \
    2   2
   / \   \
  3   3   2
 / \       \
4   4       2
返回 false 。左子树不平衡，就是2-2-2这一边


执行用时 :72 ms, 在所有 Python 提交中击败了19.64% 的用户
内存消耗 :16.5 MB, 在所有 Python 提交中击败了100.00%的用户

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#一开始没考虑特殊情况，如子树不平衡
class Solution(object):
    def getdepth(self, node, dic):
        if node == None:
            return 0
        num = 0
        left = self.getdepth(node.left, dic)
        right = self.getdepth(node.right, dic)
        if left > right:
            num = left
        else:
            num = right
        if abs(left-right)>1:
            dic[0] = False
        return num+1

    def isBalanced(self, root):
        if root == None:
            return True
        dic = []
        index = True
        dic.append(index)

        result = self.getdepth(root, dic)

        if dic[0] == False:
            return False
        else:
            return True
