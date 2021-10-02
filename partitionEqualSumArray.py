#Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

''' Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
Accepted '''


def canPartition( nums) -> bool:
    totalSum = sum(nums)
    print('totalSum ' , totalSum)
    # if totalSum is odd,it cannot be partitioned into equal sum subset
    if totalSum % 2 != 0 :
            return False
    subSetSum = totalSum // 2
    print('subSetSum ' , subSetSum)
    n =  len(nums)

    memo = [None] * (subSetSum + 1)
    memo[0] = True
    count = 0
    for i in reversed(range(1,len(memo))):
        for num in nums :
            print('--nums', num)
        
            print('num ', num , ' i' , i)
            compliment = i - num

            if compliment < 0 :
                continue
            if memo[i] :
                continue
            print('compliment ', compliment)

            if not memo[i] :
                memo[i] = (i == num) or (memo[compliment])
            print('calc rtn ', (i == num) or (i == compliment + num))
            print('memo after ' , memo)
            count += 1
            if memo[subSetSum] == True :
                print('done count', count)
                return True
    print('done count', count)
    return False








input = [14,9,8,4,3,2] # valid
input = [23,5,2,23,11,32,66,88,35,23] # valid
#input = [1,5,11,5] # valid
#input = [2,2,3,5] # invalid
result = canPartition(input)
output = True

print('input' ,input, 'result', result, 'expected', output, sep = ' : ')
#Explanation: The array can be partitioned as [1, 5, 5] and [11].
        