class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:
		bucket = []
		carryover = 0
		for key in range(len(l1)) :
			sumof =l1[key] + l2[key] + carryover
			carryover = 0
			if sumof < 10 :
				bucket.append(sumof)
			else :
				carryover = 1
				bucket.append(sumof - 10)
		return bucket[::-1]

l1 =[2,4,3]
l2 =[5,6,4]
rtn = addTwoNumbers(l1,l2)
print('rtn ', rtn)
awnser = [7,0,8]
print('awnser ', awnser)