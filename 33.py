def bin_srch_rot(inp_arr, target):
	n = len(inp_arr)
	low = 0
	target = n-1
	item = inp_arr[0]
	if target>item:
		