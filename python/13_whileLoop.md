# while loop
- Used when we don't know how many times the task should be repeated
- Use sentinal value to terminate the loop
```
count = 0
while count<5:
    count=count+1
    print(count)
else:
    print("condition not statisfied")
- Else statement is executed only when condition is not satisfied.
- If the loop is terminated or if we use break statement, the else block is not executed.
```
- Force loop termination using break
```
count = 0
while count<5:
    count=count+1
    print(count)
    if count==1:
        break
else:
    print("Else block will not excute, out from loop after the break")
```
- which one will be printed in below statement
```
count = 1
while count<1:
    count=count+1
    print(count)
else:
    print("Else block")
print("out side the look")
```
-sentinal value
```
number = int(input("Enter a number(-1 to quit)"))
while number!=-1:
    print(number)
    number = int(input("Enter a number(-1 to quit)"))
else:
    print("in else block")
print("out from loop")

count = 0
while True:
    print(count)
    count+=1
    if count==5: break
else:
    print("in else block")
print("else block")
```

```
total=0
number=int(input("enter a number(0 to quit):"))
while number!=0:
    total+=number
    number = int(input("enter a number(0 to quit):"))
print("total is", total)


enter a number(0 to quit):1
enter a number(0 to quit):2
enter a number(0 to quit):4
enter a number(0 to quit):5
enter a number(0 to quit):0
total is 12
```
