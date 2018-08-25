# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: List
        :type l2: List
        :rtype: List
        """
        valuel1 = 0
        for ele1 in l1:
            valuel1 = valuel1 + ele1*(10**l1.index(ele1))
        valuel2 = 0
        for ele2 in l2:
            valuel2 = valuel2 + ele2*(10**l2.index(ele2))
        value = valuel1 + valuel2       
        lenght=len(str(value))  
    
        L = []
        for x in range(0,lenght):
            L.append(str(value)[-(x+1)])
        L = [int(y) for y in L]
        return L

so = Solution().addTwoNumbers([2,4,3],[5,6,4])
print(so)