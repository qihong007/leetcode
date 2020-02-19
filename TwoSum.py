'''
input
in[2,7,11,15]
9
'''

'''
code
'''

class Solution(object):
    def twoSum(self, nums, target):
       
        for index_1 in range(0, len(nums)-1):
            if index_1 >= len(nums)-1:
                return null
            for index_2 in range(index_1+1, len(nums)):
                if nums[index_1]+nums[index_2] == target:
                    List = []
                    List.append(index_1)
                    List.append(index_2)
                    return List
        return null

'''
执行用时 :3988 ms, 在所有 Python 提交中击败了12.66% 的用户
内存消耗 :12.6 MB, 在所有 Python 提交中击败了57.43%的用户
'''
