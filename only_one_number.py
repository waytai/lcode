#########################################################################
#-*- coding:utf-8 -*-
# File Name: hello.py
# Author: wayne
# mail: @163.com
# Created Time: 2015年08月17日 星期一 16时40分53秒
#########################################################################
#!/bin/python


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
            
nums = [4,1,2,1,2,4,5]
So = Solution()
ret = So.singleNumber(nums)
print(ret)