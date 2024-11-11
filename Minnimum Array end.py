n = 3
x = 4
res = x

for _ in range(n):
    res += 1
    res = res | x

print("Final Answer:", res)






"""k = True
u = []
while k:
    for i in range(100):
        if i & i+1 & i+2 == x:
            u.append([i,i+2,i+2])
            k = False
            break


print(max((u)))
"""