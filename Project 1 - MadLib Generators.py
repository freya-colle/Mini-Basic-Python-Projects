"""
Project 1 - MADLAB GENERATOR
Apply string concatenation ( how to put string together)
"""

first_name = input("First name: ") #string variable
print("Hello! My name is " + first_name)

print("Hello! My name is {}".format(first_name))

print(f"Hello! My name is {first_name}")
age=input("Age: ")
major=input("Major: ")
subject=input("Subject: ")
adj=input("ADJ: ")
job=input("Job: ")

print(f"Hi! Nice to meet you. My name is {first_name}. I am {age} years old. \
My major is {major}. I have just started learning {subject} and I find it really {adj}.\
I want to become {job} in the future.")
