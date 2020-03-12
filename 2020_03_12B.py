'''
这道题就是在找是否链表是一个环，找出循环部分的开头

//弗洛伊德环
//注意fast走的路是slow的二倍，
// 1->3->4->5
//       |  |
//       7<-6  会在6遇到，1->4两个指针都会走1遍，4->6,fast会走两遍,slow走1遍，所以4->6这里fast是slow的二倍已经很明显了,
//剩下的路途，fast也要是slow的二倍，那么只能是fast的6->4 + 1->3 是slow的1->3的2倍，所以6->4应该等于1->3，所以只要让slow再走那么多就好了
//可以想象是一个环状的管子，向里面赛丝带


给定一个有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

执行用时 :84 ms, 在所有 Python 提交中击败了7.69% 的用户
内存消耗 :19.1 MB, 在所有 Python 提交中击败了100.00%的用户
'''


class Solution(object):
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        final = head
        a0 = head
        a1 = head
        i0 = 0
        i1 = 0
        while head != None:
            print(head.val)
            a0 = a0.next
            i0 = i0 + 1
            if a1 != None and a1.next != None:
                a1 = a1.next.next
                i1 = i1 + 2
            else:
                return None
            if a1 == a0:
                '''
                print(a1.val, a0.val)
                '''
                a1 = final
                
                while a1 != a0:
                    a1 = a1.next
                    a0 = a0.next
                return a1


        return head
