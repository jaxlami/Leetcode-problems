roman_numers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

inputs = 'MCMXCIV'
inp = []
result = 0
for i in inputs:
    inp.append(roman_numers[i])
print(inp)



for current, nekst in zip(inp,inp[1:]+[None]):

    print( "current:",current,"nekst: ",nekst)

    if current == nekst:
        result += current
        print("equal")
    elif nekst == None or current > nekst:
        result += current
        print('greater')
    else:
        result -= current
        print('less then')

print(result)