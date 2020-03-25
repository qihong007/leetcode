'''
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]

示例2:

 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

执行用时 :76 ms, 在所有 Python 提交中击败了67.35% 的用户
内存消耗 :23.8 MB, 在所有 Python 提交中击败了100.00%的用户
'''


class Solution(object):
    def removeDuplicateNodes(self, head):
        
        if not head:
            return head
        dic = set()
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            if cur.next.val not in dic:
                dic.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next
        return dummy.next
        
