"""nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
divisibles = 0
for i, n in enumerate(nums1):
    for j, h in enumerate(nums2):
        if n % (h*k) == 0:
            divisibles += 1

print(divisibles)"""
nums1 = [1,10,11]
nums2 = [2,2,2]
k = 5
divisibles = 0
nums2hash = {}
for i,n in enumerate(nums2):
    if (n*k) not in nums2hash:
        nums2hash[n*k]=0
    nums2hash[n*k]+=1
for i in nums1:
    for j in nums2hash:
        if i % j == 0:
            divisibles += nums2hash[j]
print(divisibles, nums2hash)