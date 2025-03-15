# 2. Write a program to accept marks of 6 students and display them in a sorted manner..

students=[];

print("Enter the marks of 6 students");

for i in range(6):
    a=int(input(f"Enter the marks of the {i+1} student : "));
    students.append(a);

students.sort();

# for student_mark in students:
#     print(student_mark);

print(students);