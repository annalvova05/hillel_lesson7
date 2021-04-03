def max_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def max_of_two_numbers(a, b):
    if a > b:
        return a
    return b


# print(max_of_two_numbers(a=max_of_two_numbers(a=max_of_two_numbers(a=-1, b=2), b=3), b=8))

def calculate_sum(numbers):
    sum_ = 0
    for i in numbers:
        sum_ += i
    return sum_


def multiply(numbers):
    sum_ = 1
    for i in numbers:
        sum_ *= i
    return sum_


def reverse_string(some_string):
    # return some_string[::-1]
    result_string = ''
    index = len(some_string) - 1
    while -1 < index < len(some_string):
        result_string += some_string[index]
        index -= 1
    return result_string


def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


def check_range(number):
    # if number in range(3, 25):
    #     return True
    if 3 < number < 25:
        return True
    return False


print(calculate_sum([1, 2, 3, 4, 5, 6, 7]))
print(multiply([1, 2, 3, 4, 5, 6, 7]))
print(reverse_string(some_string='abcdefg'))
print(factorial(number=5))
print(check_range(number=5))
