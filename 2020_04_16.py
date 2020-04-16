'''
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

注意：本题相对原题稍作改动

 

示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。

示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。

示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。


执行用时 :20 ms, 在所有 Python 提交中击败了71.50% 的用户
内存消耗 :12.7 MB, 在所有 Python 提交中击败了100.00%的用户

'''

class Solution(object):
    #逆向动态规划，从后往前，最后一个数为n，则累加时间为array[n];倒数第二个数为n-1，则累加时间为array[n]
    #倒数第三个数为n-2，则累加时间为array[n-2]+dp[n-2个往前推最大的一个值]
    def massage(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = []
        result = 0
        for i in range(0, len(nums)):
            dp.append(0)   

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                dp[i] = nums[i]
             
            elif i == len(nums)-2:
                dp[i] = nums[i]
               
            else:
                maxnum = 0
                index = i
                
                while index+2 < len(nums):                   
                    if dp[index+2] > maxnum:
                        maxnum = dp[index+2]
                    index = index + 1
                
                dp[i] = maxnum + nums[i]
                
            if dp[i] > result:
                result = dp[i]
        
        return result
