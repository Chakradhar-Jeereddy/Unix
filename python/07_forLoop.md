# Loop is an action of repeating same thing again and again.
# For loop iterates a sequence and perform an operation
# Three types of loops (for loop,,for else loop, while loop and nested loop)
# To avoid manually doing same thing again and again
```
- Syntax
for <iterator> in <squence>:
   statement(<iterator>)
```
# For loops use cases
```
name = 'Jenny'
for i in name:
  print(i)

numbers = [2,3,5,-2,10]
list = []
for i in numbers:
    square = i ** 2
    list.append(square)
print(list)

name = 'Jenny'
for i in name:
  print(i)

names = ['Jenny','Ram','Shyam']
for name in names:
  if name=='Jenny':
     print(f"Hi {name}")
  else:
    print(name)
```
#For else loop
#Else is executed only after for loop is completed.
```
Example
list = [1,2,3,4,5]
print(len(list))
for i in list:
    print(i)
    if i == 4:
        break
else:
    print('Successfully Completed')

#output - 1,2,3,4

list = [1,2,3,4,5]
print(len(list))
for i in list:
    print(i)
    break
else:
    print('Successfully Completed')
#output - 5

list = [1,2,3,4,5]
print(len(list))
for i in list:
    print(i)
else:
    print('Successfully Completed')
#output - 1,2,3,4,5,successfully competed
```

# program to calculate average height from a list of heights
# cannot use the functions sum() and len(), the output should be whole number
# Use the input(), split(),range() functions
# Average is sum()/count
```
height = input("Enter the height with space: ")
list = (height.split())
count = 0
for h in list:
    count+=1
print(count)
total = 0
for i in range(count):
  list[i]=float(list[i])

total = 0
for i in list:
    total+=i
avg = total/count
print(avg)
```
# Program to find maximum number from a list of numbers
```
number = input("Enter numbers with space: ")
numbers = number.split()
count=0
for i in numbers:
    count=count+1
print(count)

for i in range(count):
    numbers[i]=int(numbers[i])
max_number = numbers[0]
for num in numbers:
    if num > max_number:
       max_number=num
print(f"max number is {max_number}")
```
