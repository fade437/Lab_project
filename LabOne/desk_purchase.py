''''
A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of
students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integeres: the number of students in eac of the three class a,b and c respectively.

'''

num_class_A = int(input("Enter the number of students in class A"))
num_class_B = int(input("Enter the number of students in class B"))
num_class_C = int(input("Enter the number of students in class C"))

num_desk_A = (num_class_A//2)
num_desk_B = (num_class_B//2)
num_desk_C = (num_class_C//2)

remain_class_A = (num_class_A%2)
remain_class_B = (num_class_B%2)
remain_class_C = (num_class_C%2)

total_desk = num_desk_A+num_desk_B+num_desk_C+remain_class_A+remain_class_B+remain_class_C
print(f"The number of desk that should be purchased is {total_desk}")

