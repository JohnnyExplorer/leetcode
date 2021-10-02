#Given an array of integers nums.
#
#A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#
#Return the number of good pairs.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,1,1,3]
#Output: 4
#Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#Example 2:
#
#Input: nums = [1,1,1,1]
#Output: 6
#Explanation: Each pair in the array are good.
#Example 3:
#
#Input: nums = [1,2,3]
#Output: 0
# 
#
#Constraints:
#
#1 <= nums.length <= 100
#1 <= nums[i] <= 100



def numIdenticalPairs( nums: list ) -> int:
    d = {}
    c = 0
    for key,num in enumerate(nums):
        if num in d:
            c = c + len(d[num]) 
        else :
            d[num] = []
        d[num].append(key)
    return c



q = [1,2,3,1,1,3]
a = 4

#q = [1,1,1,1]
#a = 6
#
#q = [1,2,3]
#a =  0
#
#q = [1,2,3,1,1,3]
#a = 4


r = numIdenticalPairs(q)
print('problem',q)
print('rtn',r)
print('awnser',a)
