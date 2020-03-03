class Solution(object):
    def oneEditAway(self, first, second):
        if first == second:
            return True
        if abs(len(first)-len(second))>1:
            return False
        x = -1
        y = -1
        if len(first) == len(second):
            for i in range(0, len(first)):
                if first[i] != second[i]:
                    x = i
            for j in range(len(second)-1, -1, -1):
                if first[j] != second[j]:
                    y = j
            if x != y:
                return False
            else:
                return True

        else:
            index = []
            listnum = 0
            if len(first)-len(second)>0:
                listnum = len(second)
            else:
                listnum = len(first)
            for i in range(0, listnum):
                if first[i] != second[i]:
                    x0.append(i)
            if len(x0) < 1:
                return True
            if x0[0] == 0:
                if len(first) > len(second):
                    if (first[1:] == second[0:]) :
                        return True
                if len(first) < len(second):
                    if (second[1:] == first[0:]) :
                        return True
                return False
            i = x0[0]
            if len(first) > len(second):
                if (first[0:i] == second[0:i]) & (first[i+1: len(first)-1] == second[i: len(second)-1]):
                    return True
            if len(first) < len(second):
                if (first[0:i] == second[0:i]) & (second[i+1: len(second)-1] == first[i: len(first)-1]):
                    return True
        return False

        """
        :type first: str
        :type second: str
        :rtype: bool
        """
