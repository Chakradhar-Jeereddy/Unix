# loop control statements
# break,continue,pass

- break will exit the loop
- continue will skip the step below in the loop and contol goes back to the loop
- pass will do nothing

# Nested for loop
```
list1 = ["hi","hello","welcome"]
names = ["Krishna","Ram","Madhav"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="Ram":
            continue
        print('good')
    print("exit inner loop")
print("exit outer loop")

for i in range(1,11):
    if i==2:
        continue
    else:
        print(i)

for i in range(11):
    pass
```
