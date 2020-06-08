# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# FFFFFFFFFTTTTTTTTTT
# Last F
def binary_search(inp_arr, target):
	n = len(inp_arr)
	low = 0
	high = n-1
	while(low < high):
		# mid def
		mid = low + (high-low+1)//2
		# Decision
		if(inp_arr[mid]>target):
			high = mid-1
		else:
			low=mid 
	# Sanity Check
	return low if (inp_arr[low] <= target) else -1
nums = [5,7,7,8,8,10]
target = 8


print(binary_search(nums, target))
# FFFFFFFFFFTTTTTTTTTTT
# First T
def binary_search(inp_arr,target):
	n = len(inp_arr)
	low = 0
	high = n-1
	while low<high:
		# mid defn
		mid = low + (high-low)//2
		if (inp_arr[mid]>=target):
			high = mid 
		else:
			low = mid + 1 
	# Sanity check
	return high if (inp_arr[high]>=target) else -1
nums = [5,7,7,8,8,10]
target = 8
print(binary_search(nums, target))

# TTTTTTTTTTFFFFFFFFF
# Last T
def binary_search(inp_arr, target):
	n = len(inp_arr)
	low = 0
	high = n-1
	while low<high:
		# decision
		print("here low high",low,high)
		mid = low + (high-low+1)//2
		print("mid",mid)
		if inp_arr[mid] <= target:
			low = mid 
		else:
			high = mid-1
	# Sanity Check

	return low if inp_arr[low] <= target else -1

nums = [5,7,7,8,8,10]
target = 8
print(binary_search(nums, target))

# TTTTTTTTTTTTFFFFFFFFFFFFFFFFF
# First F
def binary_search(inp_arr, target):
	n = len(inp_arr)
	low = 0
	high = n-1
	while low<high:
		mid = low + (high-low)//2
		if(inp_arr[mid]<=target):
			low = mid + 1
		else:
			high = mid
	return low if inp_arr[low]>target else -1

nums = [5,7,7,8,8,10]
target = 8
print(binary_search(nums, target))