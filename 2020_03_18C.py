'''
实现一个函数，检查一棵二叉树是否为二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true

示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

执行用时 :36 ms, 在所有 Python 提交中击败了77.50% 的用户
内存消耗 :16.8 MB, 在所有 Python 提交中击败了100.00%的用户
'''

#思路：二叉搜索树的中序遍历结果必然是一个递增数列，且不会有重复的节点值
#难点二：怎么检测是一个递增数列？先检查i+1是否大于i,再检查排序后的数列（从小到大）是否与原来的一样

class Solution(object):
    def zhongxu(self, node, dic):
        if node == None:
            return
        self.zhongxu(node.left, dic)
        dic.append(node.val)
        self.zhongxu(node.right, dic)

    def isValidBST(self, root):
        if root == None:
            return True
        
        dic = []
        self.zhongxu(root, dic)

        num = len(dic)
        
        for i in range(0, num-1):
            if dic[i] >= dic[i+1]:
                return False
        
        newdic = sorted(dic)
        if newdic != dic:
            return False
       
        return True
