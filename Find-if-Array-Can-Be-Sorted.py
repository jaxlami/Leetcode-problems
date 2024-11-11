nums = [8,4,2,30,15]

for k in range(len(nums)-1):
    for i in range(len(nums)-1):
        j = i + 1
        if bin(nums[i]).count("1") == bin(nums[j]).count("1") and nums[i] > nums [j]:

            print(bin(nums[i]).count("1"))
            temp = nums[i]

            nums[i] = nums[j]
            nums[j] = temp


falies = 0
for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        falies += 1
print(nums)

if falies > 0:
    print("False")
else:
    print(True)

