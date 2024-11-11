nums = [-1,0,5]

target = 5
M = int(len(nums) / 2)
#print(nums[M])
l = 0
r = len(nums)-1
for i in range(len(nums)):

    if nums[M] > target:
        r = M
        M = int((r + l) / 2)
   #     print("to large")
    elif nums[M] < target:
        l = M
        M = int((r + l) / 2)
        print(M)
    elif nums[M] == target:
        print("equal")
    if int((r + l) / 2) == 1:
        print("-1")

print(4+(8-4)/2)