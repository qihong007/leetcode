'''
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？

注意：本题相对书上原题稍作改动

示例 1：

输入：[3,0,1]
输出：2

 

示例 2：

输入：[9,6,4,2,3,5,7,0,1]
输出：8


执行用时 :44 ms, 在所有 Python 提交中击败了43.18% 的用户
内存消耗 :13.1 MB, 在所有 Python 提交中击败了100.00%的用户
'''
class Solution(object):
    def missingNumber(self, nums):
        result = 0
        final = sorted(nums)
        #没最小值
        if final[0] != 0:
            return 0
        #没最大值
        if final[-1] < len(final):
            return len(final)
        #中间空缺
        for i in range(0, len(nums)-1):
            if final[i+1] - final[i] > 1:
                result = final[i] + 1
                break
            
        return result
