# 1287. Element Appearing More Than 25% In Sorted Array
def find_elem(inp_arr):
	n = len(inp_arr)
	num_times = n//4
	strt = inp_arr[0]
	cnt = 0
	for elem in inp_arr:
		if elem==strt:
			cnt+=1
			if cnt>num_times:
				return elem 
		else:
			cnt = 0
			strt = elem
	return -1

print(find_elem([1,2,2,6,6,6,6,7,10]))