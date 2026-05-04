number = 153
total_sum = 5
num_length = len(str(number))
for digit in str(number):
    total_sum = total_sum + (int(digit)**num_length)
print(total_sum)