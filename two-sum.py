

nums = [3,4,6,4,-1,-4]
target = 10
array={}
for i,n in enumerate(nums):
    diff = target - n
    if diff in array:
         print(array[diff],i)
    array[n]=i
