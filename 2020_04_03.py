'''
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


执行用时 :
20 ms, 在所有 Python 提交中击败了71.05%的用户
内存消耗 :12.8 MB, 在所有 Python 提交中击败了100.00%的用户

收获：了解了关于[]的新用法

'''
'''
python 列表相加可以有两种方法实现：

1 利用操作符+
比如：

a = [1,2,3]
b = [4,5,6]
c = a+b
c的结果：[1,2,3,4,5,6]

2 利用extend
比如：

a = [1,2,3]
b = [4,5,6]
a.extend(b)
a的结果：[1,2,3,4,5,6]

结果是一样的，但是+号生成的是一个新的对象，而extend则是在原地的修改a对象。

另外注意：列表的append方法，是往列表中添加新元素

比如：

a = [1,2,3]

a.append(4) #后面跟的是元素类型

a的结果为：[1,2,3,4]

'''

class Solution(object):
    def subsets(self, nums):
        result = []
        node = []
        result.append(node)
        for i in nums:
            length = len(result)
            index = 0
            while index < length:
                newnode = result[index] + [i]
                result.append(newnode)
                index = index + 1
        return result
