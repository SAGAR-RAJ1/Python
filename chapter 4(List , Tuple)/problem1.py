# 1. Write a program to store three fruits in a list entered by the user.

fruit=[];

print("Enter the name of three fruits")

for i in range(3):
    a=input(f"Enter the name of the {i+1} fruit : ");
    fruit.append(a);


for i in fruit:
    print(i);