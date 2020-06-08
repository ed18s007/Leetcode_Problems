# Find the duplicate num
def find_duplicate(inp_list):
	n = len(inp_list)
	sum_total = (n-1)*(n)/2
	sum_list = 0
	for i in inp_list:
		sum_list += i
	return sum_list - sum_total

print(find_duplicate([1,3,4,2,2]))
print(find_duplicate([3,1,3,4,2]))