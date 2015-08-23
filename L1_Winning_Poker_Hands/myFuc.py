__author__ = 'ZHIXU'

import random

myList = []
for i in xrange(10):
    myList.append(random.randrange(20))

print(myList)

class Solution:
    def __init__(self, lst):
        self.lst = lst
        self.counter = 0

    def findEven(self):
        self.helper(list(self.lst))

    def helper(self, lst):
        if len(lst) == 0:
            return self.counter
        num = lst.pop(0)
        if not num % 2:
            self.counter += 1
        return self.helper(lst)


if __name__ == '__main__':
    sol = Solution(myList)
    sol.findEven()
    print(sol.counter)