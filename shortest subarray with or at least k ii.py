nums = [1,2,32,21]
k = 55
l = 0
r = l + 1
for i in nums:
    if i >= k:
        print(i)
while r < len(nums):
    for i in range(len(nums) - 1):
        res = 0

        if nums[l] | nums[l+1 <r] == k:
            print(True)
            print ((l + r) + 1)
        else:
            r += 1
        if r == len(nums):
            l += 1
            r = l + 1
