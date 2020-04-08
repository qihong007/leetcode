class Solution(object):

    def dfs(self, t1, t2):
        # t2 is over
        if t2 == None:
            return True
        # t2 is not over and t1 is over
        elif t2 != None and t1 == None:
            return False
        # not equal
        elif t2.val != t1.val:
            return False
        # equal, then search left and right
        else:
            return self.dfs(t1.left, t2.left) and self.dfs(t1.right, t2.right)  # 注意这里是and

    def checkSubTree(self, t1, t2):
        if t1 == None:
            return False
        if t2 == None:
            return True
        # find the root of t2 in t1
        return self.dfs(t1, t2) or self.checkSubTree(t1.left , t2) or self.checkSubTree(t1.right, t2)
