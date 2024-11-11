nums = [1, 2, 1, 3]
temp = []
res = []

for i in nums:
    if i not in temp:
        temp.append(i)
    elif i in temp:
        res.append(i)
print(res)

ansr = 0

for i in res:
    ansr = ansr ^ i
print(ansr)