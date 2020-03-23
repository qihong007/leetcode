'''
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

说明:

    A.length == n + m

执行用时 :24 ms, 在所有 Python 提交中击败了54.76% 的用户
内存消耗 :11.7 MB, 在所有 Python 提交中击败了100.00%的用户

'''
#这道题的意义在于用了三层for循环
#https://leetcode-cn.com/problems/sorted-merge-lcci/solution/he-bing-pai-xu-shu-zu-dong-tu-by-zi-you-ru-feng-9/
#可以参考上述合并排序算法，感觉很妙
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        
        if m == 0:
            for i in range(0, n):
                A[i] = B[i]
            return
        
        for i in range(0, n):
            for j in range(i, m+i):
                if B[i] >= A[m+i-1]:
                    A[m+i] = B[i]
                    break
                if B[i] < A[j]:
                    for k in range(m+i, j, -1):
                        A[k] = A[k-1]
                    A[j] = B[i]
                    break
