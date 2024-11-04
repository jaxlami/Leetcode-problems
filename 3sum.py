nums = [0,0,0,0,0]
def threeSum():
    answ=[]
    nums.sort()
    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
            continue
        

        b,c = i + 1,len(nums)-1
        while b < c:
            curSum = a + nums[b] + nums[c]
            if curSum > 0:
                c -= 1
            elif curSum < 0:
                b += 1
            else:
                answ.append([a,nums[b],nums[c]])
                b += 1
                while nums[b] == nums[b-1] and b < c:
                    print('b:',b,' c: ',c)
                    b +=1
    return answ

answ = threeSum()
print(answ)