'''
Problem Statement
Take two numbers from user
Calculate Sum, Difference, Product and Division
Display each results.
'''
greet = "Hello"
name = input("Your name please: ")
print("Hello", name, "we are going to ask your to enter two numbers")
first_num = int(input("Please enter frist number: "))
second_num = int(input("Please enter second number: "))

print("The sum of the numbers is", (first_num + second_num))
print("The difference of the number is", (first_num - second_num))
print("The product of the number is", (first_num * second_num))
print("The division of the number is", (first_num / second_num))