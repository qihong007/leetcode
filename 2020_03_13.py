'''
如果感觉有启发，欢迎点赞，让我知道题解帮助到了大家😊。
Method1:暴力法

对于链表A中的每个节点，都对链表B进行遍历，判断是否有相同的节点
code

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *cur1=headA;
        while(cur1)
        {
            ListNode *cur2=headB;
            while(cur2)
            {
                if(cur1==cur2)
                    return cur1;
                cur2=cur2->next;
            }
            cur1=cur1->next;
        }
        return nullptr;
    }
};

Method2:使用set

使用set存链表A中的节点，然后遍历链表B，检查set中是否有相同的节点
code

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode*> s;
        while(headA)
        {
            s.insert(headA);
            headA=headA->next;
        }
        while(headB)
        {
            if(s.find(headB)!=s.end())
                return headB;
            headB=headB->next;
        }
        return nullptr;
    }
};

Method3:双指针

使用两个指针分别指向headA和headB，当一个指针先到达末尾时，就让它指向另一个指针的头部，如果相遇的话就是交点；否则的话两个指针都走了两个链表的长度，返回null。
code

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *curA=headA,*curB=headB;
        while(curA != curB)
        {
            if(curA==NULL)
                curA=headB;
            else
                curA=curA->next;
            if(curB==NULL)
                curB=headA;
            else
                curB=curB->next;
        }
        return curA;
    }
};

作者：jesse-42

给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。

示例 1：

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。


这里借鉴了方法三
执行用时 :316 ms, 在所有 Python 提交中击败了5.66% 的用户
内存消耗 :42.7 MB, 在所有 Python 提交中击败了100.00%的用户
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a1 = headA
        a2 = headB
        result = headA
        while a1 != None and a2 != None:
            if a1 == a2:
                return a2
            a2 = a2.next
            a1 = a1.next
            if a1 == None and a2 != None:
                a1 = headB
            if a2 == None and a1 != None:
                a2 = headA
        return None
