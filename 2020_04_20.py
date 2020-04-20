'''
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求值的顺序保持不变，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

注意：本题相对原题稍作改动

 

示例：

输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]

执行用时 :160 ms, 在所有 Python 提交中击败了14.29% 的用户
内存消耗 :36.6 MB, 在所有 Python 提交中击败了100.00%的用户

'''


class Solution(object):
    def travel(self, root, result):
        if root == None:
            return
        self.travel(root.left, result)
        print(root.val)
        result.append(root.val)
        self.travel(root.right, result)

    def convertBiNode(self, root):
        if root == None:
            return None
        result = []
        #中序遍历，从小到大
        self.travel(root, result)
        #创建新的树
        newnode = TreeNode(result[0])
        final = newnode
        i = 1
        while i < len(result):
            newnode.right = TreeNode(result[i])
            newnode = newnode.right
            i = i + 1
        return final

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
