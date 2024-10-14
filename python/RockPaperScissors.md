# rock paper scissors
# rock = 0
# paper = 1
# scissor = 2
```
import random as r
l = ['rock','paper','scissor']
computer = r.randint(0,2)
user = int(input("User input the number: "))
if user not in [0,1,2]:
#if user >=3 or user <0:
    print("enter the correct input")
elif computer==user:
    print(f"{l[computer]} and {l[user]} Draw")
elif computer==2 and user==0:
    print(f"{l[computer]} and {l[user]} User wins")
elif computer==0 and user==2:
    print(f"{l[computer]} and {l[user]} user will lose")
elif computer>user:
    print(f"{l[computer]} and {l[user]} user will lose")
else:
    print("user wins")
print(f"computer choise is {computer}")
```
