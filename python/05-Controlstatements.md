#Syntax
```
if condition:
  do this
else:
  do this
```

```
a=1
if a>5:
  print('a is big')
else:
  print('a is small')

a=1
if(a>5) :
  print('a is big')
else :
  print('a is small')

```
# Write a program to check the number is even
#Pizza Order program

#small pizza = 100
#medium pizza = 200
#large pizza = 300
#pepperoni for small pizza = 30
#pepperone for mediam pizza = 50
#.....         large pizza = 70
#extra cheeze for any size pissa = 20

```
number = int(input("Enter the number: ")
if(number%2==0):
  print("even number")
else:
  print("odd number")
```
#Write a code for this requirement
- Pizza Order program
- small pizza = 100
- medium pizza = 200
- large pizza = 300
- pepperoni for small pizza = 30
- pepperone for mediam pizza = 50
- .....         large pizza = 70
- extra cheeze for any size pissa = 20

```
size = input("Please enter pizza size s/m/l: ")

bill = 0
if(size=='S' or size=='s'):
    bill+=100
    print(f"Small pizza is {bill} rupees.")
elif(size=='M' or size=='m'):
    bill+=200
    print(f"Medium pizza is {bill} rupees.")
else:
    bill+=300
    print(f"Large pizza is {bill} rupees.")

add_pepperoni = input("Add pepperoni y/n? ")

if(add_pepperoni=='Y' or add_pepperoni=='y'):
    if (size == 'S' or size=='s'):
        bill+=20
        print(f"Small pizza added with pepperoni is {bill} rupees.")
    else:
        bill+=50
        print(f"Your pizza added with pepperoni is {bill} rupees.")
add_cheese = input("Add cheese y/n? ")
if(add_cheese=='Y' or add_cheese=='y'):
    bill+=20
    print(f"Your pizza added with cheese {bill} rupees.")
else:
    print(f"Your pizza without cheese is {bill} rupees.")
```





