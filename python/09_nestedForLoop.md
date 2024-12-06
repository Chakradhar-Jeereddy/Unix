# Nested for loop
```
list1 = ["hi","hello","welcome"]
names = ["Krishna","Ram","Madhav"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="Ram":
            break
    print("exit inner loop")
print("exit outer loop")
```
