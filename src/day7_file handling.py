import csv

with open("data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

try:
    
    with open("missing.text",'r') as file:
        content=file.read()
        print(content)

except FileNotFoundError:
    print("maaz ye file exist nahi hai thank u")
    
# task1
    
name = input("What is your name? ")
goal = input("What is your Daily Goal? ")

with open("journal.txt", "a") as file:
    file.write(f"{name}: {goal}\n")


#task 2

import csv

with open("student.csv","r") as file:
    reader=csv.DictReader(file)
    
    print("students who have passed:")
    for row in reader:
        if row ["Status"]=="Pass":
            print(row["Name"])
    
#task 3
filename = input("Enter a filename ")

try:
    with open(filename, "r") as file:
        contents = file.read()
        print("File contents:")
        print(contents)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")