#string comperssion III

word = "abccde"
lenght = len(word)
comp = []
same = 1
for i, n in enumerate(word):
    if same < 9:
        if i < lenght - 1 and n == word[i+1]:
            same += 1
        else:
            comp.append(str(same)+n)
            same = 1
    else:

print(''.join(comp))