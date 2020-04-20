'''
在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 6, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。

示例:

输入: [5, 3, 1, 2, 3]
输出: [5, 1, 3, 2, 3]

提示：

    nums.length <= 10000


执行用时 :48 ms, 在所有 Python 提交中击败了41.38% 的用户
内存消耗 :13.6 MB, 在所有 Python 提交中击败了100.00%的用户

'''
#思路先把数列排序，然后截取一半一半，分为big和small，big的最小比small的最大还大，然后重新弄一个数组，big和small的数互相穿插
#但是代码有点丑陋
class Solution(object):
    def wiggleSort(self, nums):
        result = sorted(nums)
        big = []
        small = []
        for i in range(len(nums)/2, len(nums)):
            big.append(result[i])
        for i in range(0, len(nums)/2):
            small.append(result[i])
        final = []
        for i in range(0, len(big)):
            final.append(big[i])
            if i < len(small):
                final.append(small[i])
        for i in range(0, len(nums)):
            nums[i] = final[i]
        print(nums)
