def function(a, b, c):
    print(a, b, c)


function(a=5, c=7, b=6)
function(5, 7, 6)
function(5, b=6, c=7)
function(a=5, b=6, c=7)


def calculate_sum_of_two_numbers(a, b):
    return a + b


def is_str(a):
    if type(a) == str:
        return True
    return False


list_of_names = ['Anna', 'Alex', 'Oleg']


def is_name(name):
    if name in list_of_names:
        return True
    return False
