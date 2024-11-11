
strs = ["flower","flow","flight"]
answr = ""

for i in range(len(strs[0])):
    for s in strs:
        while i != len(s):
            if i == len(s) or s[i] != strs[0][i]:
                break
        answr += strs[0][i]


print(answr)






"""    
    for j, w in enumerate(str[i]):
    
        timp.append(w)
        #if temp.count(w) == len(str):
         #   answr.append(w)
"""