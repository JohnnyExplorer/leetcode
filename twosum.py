def twoSum(nums,target: int):

#    for key,num in enumerate(nums):
#        left = target - num
#        tester = nums[:]
#        del(tester[key])
#        if left in tester:
#            second = nums.index(left)
#            return (key,second)
    known = {}
    for i, num in enumerate(nums):
        print('i',i,'num',num,sep=' ')
        if num in known:
            return [known[num], i]
        else:
            known[target - num] = i 
        print('known ', known)  

nums = [3,3]
value = 6
rtn = twoSum(nums,value)
print('rtn ' , rtn)
