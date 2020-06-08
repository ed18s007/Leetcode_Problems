# 1013. Partition Array Into Three Parts With Equal Sum
def equal_sum(inp_arr):
	n = len(inp_arr)
	print("n",n)
	left = inp_arr[0]
	middle = 0
	right = inp_arr[n-1]
	for i in range(1,n-1,1):
		print(i)
		middle += inp_arr[i]
	if(left==middle==right):
		return True

	print(left,middle, right)

inp =  [0,2,1,-6,6,-7,9,1,2,0,1]
equal_sum(inp)