

s = "aaabaaaa"
"""
new_s = ''
for i, n in enumerate(s):
    if len(new_s) > 1 and s[i-2] == s[i-1] == n:
        continue
    else:
        new_s += n
"""

new_s = ''
for n in s:
    if len(new_s) > 1 and new_s[-2] == new_s[-1] == n:
        continue
    else:
        new_s += n

print(new_s)