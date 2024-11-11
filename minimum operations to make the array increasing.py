"""nums = [1,5,2,4,1]
highest = 0
op = 0
try:
    nums[1]
except IndexError:
    print("0")

for i in range(len(nums)):
    if nums[i] > highest:
        highest = nums[i]
    elif highest == nums[i]:
        highest += 1
        op += 1
    elif highest > nums[i]:
        op += (highest - nums[i]) + 1
        highest = (highest - nums[i]) + (nums[i] + 1)
print(op)"""

nums = [1,5,2,4,1]
operation = 0

for i in range(len(nums) - 1):
    if nums[i + 1] <= nums[i]:
        operation += (nums[i] - nums[i + 1] + 1)
        nums[i + 1] = nums[i] + 1


print(operation)