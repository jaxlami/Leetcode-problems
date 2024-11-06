nums = [1,2,1]
hash = {}

for i in range(len(nums)):
    hash.add([nums[i]])


for i in range(len(nums)-1):
    for j in range(len(nums) - 1):
        hash.add([nums[l],nums[j]])



print(hash)