'''
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8

执行用时：28 ms
内存消耗：12.9 MB

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        #思路：我们先找到第一个大于等于x的节点，将后面小于x的节点移动过来
        if head == None:
            return None
        pre_head = ListNode(-1)
        pre_head.next = head
        pre = pre_head
        cur = head
        while cur and cur.val < x:
            pre = cur 
            cur = cur.next
        if cur == None:
            return pre_head.next
        #cur是要连接的节点，pre是前一个节点
        right = cur.next
        left = cur
        while right:
            if right.val < x:
                left.next = right.next
                right.next = cur
                pre.next = right
                pre = right
                right = left.next
            else:
                left = right
                right = right.next
        return pre_head.next


        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
