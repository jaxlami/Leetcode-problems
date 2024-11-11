candidates = [10,20,13,4,5,1]
max_set=0
for b in range(24):
    b_bit_set=0

    for x in candidates:
        b_bit_set+=(x>>b &1)
    print(b_bit_set)
    max_set=max(max_set, b_bit_set)

