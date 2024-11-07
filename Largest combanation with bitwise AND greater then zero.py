nums = [16,17,71,62,12,24,14]
steps = []
steps.append(nums[0])

for i in range(len(nums)-1):
    if steps[i]&nums[i+1] != 0:
        steps.append(nums[i]&nums[i+1])

print(steps)

