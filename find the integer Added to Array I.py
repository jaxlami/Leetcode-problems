nums1 = [2,6,4]
nums2 = [9,7,5]
res = []

for i, ii in zip(nums1,nums2):
    res.append(i-ii)
print(res)
ress = 0
for i in res:
    ress += i
ress = -ress
print(ress/len(nums1))