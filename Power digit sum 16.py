#Power digit sum 16

num = 2**1000
sum = 0
print(num)

for c in str(num):
    sum += int(c)

print(sum)