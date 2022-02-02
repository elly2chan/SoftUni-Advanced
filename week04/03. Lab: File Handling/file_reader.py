file = open('numbers.txt')

nums_sum = 0
for num in file:
    nums_sum += int(num)

print(nums_sum)