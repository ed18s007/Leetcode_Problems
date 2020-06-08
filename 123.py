# 123. Best Time to Buy and Sell Stock III
def max_profit(inp_arr):
	n = len(inp_arr)
	max_right = inp_arr[-1]
	max_idx = n-1
	max_profit_idx = n-1
	max_profit = 0
	left_sum, right_sum = 0, 0
	profit_arr, idx_arr = [],[]
	for i in range(n-1,-1,-1):
		if inp_arr[i]>=max_right:
			max_right = inp_arr[i]
			max_idx = i
		profit = max_right-inp_arr[i]
		if profit>=max_profit:
			max_profit = profit
			max_profit_idx = i
		profit_arr.insert(0,profit)
		idx_arr.insert(0,max_idx)

	print("inp_arr",inp_arr)
	print("profit_arr",profit_arr)
	print("idx_arr",idx_arr)
	print("max_profit_idx",max_profit_idx)
	print("max_profit",max_profit)
	for i in range(idx_arr[max_profit_idx], n):
		right_sum = max(right_sum, profit_arr[i])
	for j in range(max_profit_idx-1,-1,-1):
		if idx_arr[j]<max_profit_idx:
			left_sum = max(left_sum, profit_arr[j])
	print(max_profit, left_sum, right_sum)

arr = [3,3,5,0,0,3,1,4]
pro = [1,2,3,4,5]
idx = [7,6,4,3,1]
# max_profit(arr)
# max_profit(pro)
# max_profit(idx)
# max_profit([2,1,4])
# max_profit([6,1,3,2,4,7])
def max_profit_2(inp_arr):
	n = len(inp_arr)
	max_rt_ls = [0]*n
	max_rt_ls[n-1] = inp_arr[n-1]
	for i in range(n-2,-1,-1):
		max_rt_ls[i] = max(max_rt_ls[i+1],inp_arr[i])

	print(max_rt_ls)
	minsofar = min(inp_arr[0],inp_arr[1])
	profit = max(0,inp_arr[1]-inp_arr[0])
	res = profit
	for j in range(2,n,1):
		if j<n-1:
			curr_profit = max(0,max_rt_ls[i+1]-inp_arr[j])
		else:
			curr_profit = 0
		net_profit = curr_profit + profit		
		res = max(res,net_profit)
		
		profit = max(profit, inp_arr[j]-minsofar)
		minsofar = min(minsofar,  inp_arr[j])
	print(max(res,profit))	

max_profit_2(arr)
max_profit_2(pro)
max_profit_2(idx)
max_profit_2([2,1,4])
max_profit_2([6,1,3,2,4,7])
