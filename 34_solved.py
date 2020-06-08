def frst_last_srch(nums, target):
	n = len(nums)
	low = 0
	high = n-1
	ls = []
	if(n<1):
		return [-1,-1]
	else:
		while low<high:
			mid =low+(high-low)//2
			if(nums[mid]>=target):
				high = mid
			else:
				low = mid+1
		if(nums[high]==target):
			ls.append(high)
		else:
			ls.append(-1)
		
		low = 0
		high = n-1
		while  low<high:
			mid = low+(high-low+1)//2
			if(nums[mid]>target):
				high = mid-1
			else:
				low = mid 
		if(nums[low]==target):
			ls.append(low)
		else:
			ls.append(-1)
		return ls 

# FFFFFFFFFFTTTTTTTTT
# Last F
def bin_srch_F(nums, target):
	n= len(nums)
	low = 0
	high = n-1
	if(n<1):
		return -1
	else:
		while low<high:
			mid = low+(high-low+1)//2
			if(nums[mid]>target):
				high = mid-1
			else:
				low = mid
		return low if nums[low]==target else -1

# FFFFFFFFFTTTTTTT
# First T
def bin_srch(nums, target):
	n = len(nums)
	low = 0
	high = n-1
	if(n<1):
		return -1
	else:
		while low<high:

			mid = low+(high-low)//2
			if(nums[mid]>=target):
				high = mid 
			else:
				low = mid+1
		return low if nums[low]==target else -1



# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 0))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 1))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 2))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 3))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 4))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 5))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 6))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 7))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 8))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 9))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], 10))
# print(frst_last_srch([0,1,2,3,4,5,6,7,8,9], -1))

print(frst_last_srch([0,1], 0))
print(frst_last_srch([0,1], 1))
print(frst_last_srch([0,1], -1))
print(frst_last_srch([0], 0))
print(frst_last_srch([0], 1))
print(frst_last_srch([0], -1))
