def get_factorial(num):
    factorial = 1
    for i in range (1,num):
        if num-i > 0:
            factorial = factorial*(num-i)
    factorial = factorial*num
    return factorial

def sum_odd_numbers(num):
    total = 0
    i = 1
    while i <= num:
        if i % 2 != 0:
            total += i
        i += 1
    return total