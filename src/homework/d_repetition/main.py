import repetition
from repetition import get_factorial
from repetition import sum_odd_numbers

print("Homework 3 Menu\n1- Factorial\n2- Sum Odd Numbers\n3- Exit")

user_selection = 0

while user_selection < 1 or user_selection > 3:
    user_selection = int(input("\nPlease make a number selection from the above: "))

if user_selection == 1:
    user_factorial_num = int(input("Please enter a number between 1-9: "))
    while user_factorial_num < 1 and user_factorial_num > 9:
         user_factorial_num = int(input("Please enter a number between 1-9: "))
    print("The factorial of ", user_factorial_num, " is ", get_factorial(user_factorial_num))

elif user_selection == 2:
    user_odd_sum_num = int(input("Please enter a number between 1-99: "))
    while user_odd_sum_num < 1 and user_odd_sum_num > 99:
         user_odd_sum_num = int(input("Please enter a number between 1-99: "))
    print("The sum of all odd numbers up to ", user_odd_sum_num, " is ", sum_odd_numbers(user_odd_sum_num))

else:
    print("Thank You!\nThis program will now exit.")
    exit