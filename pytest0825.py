import random

hello = input("What is your name")
print(f"hello {hello}")

stu = ['a', 'b', 'c']
print(random.choice(stu))

name = 'My name is %s' % 'Cathy'
print("Name: ", name)

name2 = 'My name is {0}'.format("Cathy")
print("NAME: ", name2)