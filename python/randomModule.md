# Random number generator
# Need to import the module first and invoke its functions
```
import random as r
l = [1,2,3,4,5,6,7,9]
print(r.randint(1,3)) #=> returns integer including 1 and 3
print(r.randrange(1,3)) #=> generates an integer number and 3 is not included
print(r.random())  #=> It generates a floating number from <=0.0 to <=1.0 but 1.0 is not included
print(r.choice(l))  #=> supply list object & it will choose a number from the list
print(r.uniform(1,4)) #=> it generates a uniform floating number
r.shuffle(l)  #=> pass the list object and it will shuffle the elements
print(l)
```

# Case generate a random number between 0,1 and print head or tail based on the outcome
```
import random as r
side = r.randint(0,1)
print(side)
print(type(side))
if side==0:
    print('Tails')
else:
    print('Heads')
```

# Enter names of the people, pick one randomly to pay the bill
```
import random as r
name_list = []
people = int(input("how many names you want to enter? "))
for i in range(people):
    name = input(f"Enter you name {i+1}: ")
    name_list.append(name)
print(f"{r.choice(name_list)} has to pay the bill")

#Writing same program using split function
import random as r
names = input("Please enter all your names: ")
list = names.split(" ")
print(list)
```

# Writing same program using split function
# Using split function on string we can create a list object
```
import random as r
names = input("Please enter all your names with comma separation: ")
if "," in names:
 list = names.split(",")
 print(list)
 print(len(list))
 print(f"{list[r.randint(0,2)]} will pay the bill.")
else:
    print("Enter the names with comma separation")
print(list[0:3])
```
# Writing same program using split function
# Using split function on string we can create a list object
```
import random as r
names = input("Please enter all your names with comma separation: ")
names_list = names.split(",")
length = len(names_list)
rand_choice = r.randint(0,length-1)
print(f"{names_list[rand_choice]} will pay the bill")
```
