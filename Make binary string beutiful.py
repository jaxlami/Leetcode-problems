"""s = "100101"
slist = list(s)
slist = [int(item) for item in slist]
slen = int(len(s)/2)
fix = []
for i, n in enumerate(slist):
    if i == 0:
        fix.append(n)
        continue
    if i < slen and i < slen:
        if n != slist[i-1]:
            fix.append(slist[i-1])
    elif i > slen -1 :
        if slist[slen] == 0:
            fix.append(0)
        elif slist[slen] == 1:
            fix.append((1))


print(fix)
print(slen,slist)"""

"""s = "11000111"
slist = [int(item) for item in s]
slist.sort()
slen = int(len(slist)-1)
ones = 0


for i in slist:
    if i == 1:
        ones += 1

for i in slist:

    l = 0
    r = slen
    if slist[l] == slist[r]:
        print("the same")
    elif slen == 1:
        print("one")
    elif ones == (slen+1)/2:
        print("its two")


print(slist)"""

"""s = "11000111"
slist = [int(item) for item in s]
changes = 0
l = 0
r = 1

for i in slist:
    if slist[l] == slist[r]:
        r += 1
        l += 1
    elif slist[l] != slist[r]:
        l += 1
        r += 1
        if slist[l] == slist[r]:
            r += 1
            l += 1
        elif slist[l] != slist[r]:
            changes += 1"""
s = "100100"

changes = 0

for i in range(0,len(s),2):
    print(i)
    if s[i] != s[i+1]:
        changes += 1
print(changes)

