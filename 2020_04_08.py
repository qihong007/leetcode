'''
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。

示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4

提示:

    words的长度在[1, 1000000]之间



执行用时 :20 ms, 在所有 Python 提交中击败了84.13% 的用户
内存消耗 :13.2 MB, 在所有 Python 提交中击败了100.00%的用户
'''


class Solution(object):
    def findString(self, words, s):
        for i in range(0, len(words)):
            if words[i] == s:
                return i
        return -1
