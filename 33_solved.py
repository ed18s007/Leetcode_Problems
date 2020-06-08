def search(nums, target) -> int:
    n = len(nums)
    if n<1:
        return -1
    if n==1:
        return 0 if target==nums[0] else -1
    key = nums[0]
    low = 0
    high = n-1
    if target==key:
        return 0
    if key<nums[n-1]:
        min_idx = 0
    else:
        while low<high:
            mid = low+(high-low)//2
            if(nums[mid]<key):
                high = mid
            else:
                low = mid+1
        if nums[low]<key:
            min_idx = low 
    # print("min_idx",min_idx)
    if target>key:
        low = 0
        print("n",low,high)
        high = min_idx-1 if min_idx>0 else n-1
        while low<high:
            # mid defn
            mid = low + (high-low)//2
            if (nums[mid]>=target):
                high = mid 
            else:
                low = mid + 1 
        # Sanity check
        return high if (nums[high]==target) else -1
    else:
        low = min_idx
        high = n-1
        print("here",low,high)
        while low<high:
            # mid defn
            mid = low + (high-low)//2
            if (nums[mid]>=target):
                high = mid 
            else:
                low = mid + 1 
        # Sanity check
        return low if (nums[low]==target) else -1

print(search([1,3],2))