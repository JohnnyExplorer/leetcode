'''We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.
The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000
'''


import time

import math
start = time.time()
def distributeCandies( candies: int, num_people: int) -> list:

    output = [0]*num_people
    i = 1
    while candies >= i:
        print('i ',i)
        print('(i-1)%num_people ', (i-1)%num_people)
        output[(i-1)%num_people] += i
        print('output[(i-1)%num_people] += i ', output[(i-1)%num_people])
        candies -= i
        print('candies ',candies)
        i += 1
    output[(i-1)%num_people] += candies
    print('output[(i-1)%num_people] += candies ', output[(i-1)%num_people] )
    return output

        
def distributeCandiesv2( candies: int, num_people: int) -> list:
       rtn = [0] * num_people
       count = 0
       while candies >= 0 :
               for x in range(0,num_people):
                       count += 1
                       give = count if candies > count else candies
                       candies -= count
                       rtn[x] += give
                       if candies <= 0:
                               break
       return rtn

def distributeCandiesv3( candies: int, num_people: int) -> list:
    n, k = candies, num_people
    print('n ', n)
    print('k ', k)
    pos = math.floor((-1 + math.sqrt(1 + 8 * n))/2)
    print('pos ', pos)
   
    multi = math.ceil(pos / float(k))
    print('multi ', multi)
    rest = n - (1 + pos) * pos // 2
    print('res ', rest)
    pos = (pos + k - 1) % k
    print('pos ', pos)
    
    rst = []
    for i in range(k):
        if i <= pos:
            rst.append(multi * (i + 1) + multi * (multi - 1) * k // 2)
        else:
            if multi > 1:
                rst.append((multi - 1) * (i + 1) + (multi - 1) * (multi - 2) * k // 2)
            else:
                rst.append(0)
    
    rst[(pos + 1) % k] += rest
    return rst


def distributeCandiesv4( candies: int, num_people: int) -> list:
    arr = [0] * num_people
    rounds = 0
    while candies > 0:
        candies4WholeRound = int((num_people * (num_people + 1))/2   +  (num_people *num_people)*rounds)
        if candies >= candies4WholeRound:
            candies -= candies4WholeRound
            rounds += 1
        else: # distribute the candies to each person until candies run out-- last round
            for i in range(num_people):
                if candies >= num_people * rounds + i + 1:
                    arr[i] += num_people * rounds + i + 1
                    candies -= num_people * rounds + i + 1
                else:
                    arr[i] += candies
                    candies = 0

   # Now distribute the whole rounds of candies
    for i in range(num_people):
        arr[i] += int((i+1)*rounds + num_people * rounds * (rounds - 1)/2)
        
    return(arr)


candies = 7
num_people = 4
a = [1,2,3,1]


candies = 10e9
num_people = 1000
#a = [5,2,3]


print('candies ', candies)
print('num_people ', num_people)
rtn = distributeCandiesv4(candies,num_people)


print('rtn',rtn)
print('a ' , a)

print('sum ' , sum(rtn))
end = time.time()
print('end ', end - start)
