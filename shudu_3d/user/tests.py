import os
import uuid


from typing import List


from django.test import TestCase


# Create your tests here.
# count = 0
# class Solution:
#
#
#
#     def climbStairs(self, n: int) -> int:
#         global count
#         if n==0 or n==1:
#             count+=1
#             return 0
#         sum=self.climbStairs(n-1)+self.climbStairs(n-2)
#         return count
# so=Solution()
# on=so.climbStairs(3)
# print(on)
# time
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         count = 0
#         let = 0
#         flag=True
#         while flag:
#             lenght = len(nums)
#             if let> lenght or lenght<=1:#0,1
#                 nums.sort()
#                 flag=False
#                 continue
#             repeat = nums[count]#0,0
#             if repeat in nums[count + 1:]:
#                 num = nums[count + 1:].count(repeat)# 1
#                 for i in range(num):
#                     nums.remove(repeat)#[011122334]
#
#             else:
#
#                 count += 1
#             let += 1
#         return nums
#
#
# so = Solution()
# a = so.removeDuplicates([1,2])
# print(a)
#
# c=[]
# c.sort()
# print(c)
# a=str(uuid.uuid4())
# ne=a.split('-')
# new=''.join(ne)
# print(a,type(a),f'dsad{a}',ne,new)
# file = open(f'../static/pro/1.pcd', 'wb')
# file.close()
# print(os.path.exists('../static/pro/'))
# uuid4=str(uuid.uuid4())
#
# new_uuid4=''.join(uuid4.split('-'))
# file = open(os.path.join(f'../static/pro/',f'{new_uuid4}_1.pcd'), 'wb')
# file.close()
from itertools import count
from collections import Counter
# a= {'a':3}
# print(a.values())
# for i in a.values()

# a=list(a)
# print(a)
# # print(a.count('3'))
#
# print(Counter(a))