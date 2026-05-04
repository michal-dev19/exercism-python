# input_base = 8
# digits = 101010
# output_base = 3

# str_digit = str(digits)
# print(str_digit)

# amount_of_digits = len(str_digit)
# print(amount_of_digits)

# list_of_digits = list(str_digit)

# for digit in range(amount_of_digits):
#     list_of_digits[digit] = int(list_of_digits[digit])

# in_digit_sum = 0
# iterator = amount_of_digits - 1
# for digit in list_of_digits:
#     in_digit_sum += (digit * (input_base**iterator))
#     iterator -= 1
# print(in_digit_sum)

# print((33288 - (33288 % 10000)) // 10000)

print(33288 % 3)