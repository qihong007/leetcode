'''
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]

执行用时 :116 ms, 在所有 Python 提交中击败了60.87% 的用户
内存消耗 :19.3 MB, 在所有 Python 提交中击败了100.00%的用户

'''

class Solution(object):
    #本题用了sorted函数，感觉有点作弊。。。
    def smallestK(self, arr, k):

        
        newarr = sorted(arr)
        print(newarr)
        final = []
        for i in range(0, k):
            final.append(newarr[i])
        return final
