from functools import reduce

nums = [0,1,1,3]
maximumBit = 2

# find the XOR (^) in the nums.
# find a away to to do this quary n number of times
out = 0
M = len(nums)
while M < 0:
    for i in nums:
        out ^= M
    M -= 1

print(out)







"""
mxK = [0,0]
for i in range((2**maximumBit)):
    if int(xzored ^ i) > mxK[1]:
        print(i)
        mxK[0] = i
        mxK[1] = xzored ^ i

print(mxK)
"""