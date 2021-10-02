'''Given an array nums. We define a running sum of an array 
    as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''

class Solution:
    def runningSum(self, nums ):
        for k in range(1,len(nums)):
            nums[k] = nums[k-1] + nums[k]
        return nums



s = Solution()

q = [1,2,3,4]
a = [1,3,6,10]
print('q',q)
rtn =s.runningSum(q)
print('rtn',rtn,'a',a,sep="\n")

q= [1,1,1,1,1]
a =[1,2,3,4,5]

print('q',q)
rtn =s.runningSum(q)
print('rtn',rtn,'a',a,sep="\n")

q= [3,1,2,10,1]
a =[3,4,6,16,17]
print('q',q)
rtn =s.runningSum(q)
print('rtn',rtn,'a',a,sep="\n")
