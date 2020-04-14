'''
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例：

输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}

提示：

    0 < shorter <= longer
    0 <= k <= 100000

执行用时：72 ms
内存消耗：19.6 MB

'''

class Solution(object):

    def divingBoard(self, shorter, longer, k):
        result = []
        #特殊情况，k=0，shorter=longer
        if k == 0:
            return result
        if shorter == longer:
            result.append(shorter*k)
            return result
        #统计
        for i in range(k, -1, -1):
            shortersum = i * shorter
            longersum = (k-i) * longer
            total = shortersum + longersum
            result.append(total)
        
        #去重
        final = []
        final.append(result[0])

        for i in range(1,len(result)):
            if result[i] != result[i-1]:
                final.append(result[i])

        return final
