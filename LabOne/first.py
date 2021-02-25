# Write a program that takes three numbers and prints their sum. Every number is given on a separate line.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
sum  =num1+num2+num3
print("The sum is ",sum)


name = input("Enter your name:")
age = int(input("Enter age:"))

print("Hello my name is " + name + "and I am " + str(age) + " years old")
print("Hello my name is", name, "and I am", age, "years old")
print("Hello my name is %s and I am %d years old" % (name,age))
print("Hello my name is {} and I am {} years old".format(name, age))
print(f"Hello my name is {name} and I am {age} years old")