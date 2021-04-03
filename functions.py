def calculate_sum_of_two_numbers(a, b):
    return int(a) + int(b)


sum_ = 0
number_index = 0
list_of_numbers = input("Enter numbers: ").split(',')
while number_index < len(list_of_numbers):
    sum_ = calculate_sum_of_two_numbers(
        a=list_of_numbers[number_index],
        b=sum_
    )
    number_index += 1
print(sum_)
