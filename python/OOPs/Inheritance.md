- Inheritance
- Inheriting attributes and methods of a created class into another class being created.
- Parent,supper or base class
- Derived, child and subclass
-  Why inheritance
- Syntax for inheritance
```
class ChiledClass(ParentClass):
    <Class defination>
```
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Make:
    def eat(self):        #repeating the methods
        print("I can eat")
    def work(self):
        print("I can work") #repeating the methods

class MakeI(Human):  #MakeI class is inheriting methods and attributes from Human class.
    pass
making=MakeI()  
making.eat()    #getting this method from human class
making.work()   #getting this method from human class
```

```
#Supper() gives access to all the attributes and methods of supper class to a subclass.

class Human:
    def __init__(self,num_heart):
        self.eyes=2
        self.nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)  #when you do local initialization, you need super clause for parent initialization
        self.name=name
    def flirt(self):
        print(f"I can flirt, I have {self.nose} heart")
    def work(self):  #method overriding, overriding the method of Human class.
        super().work()  #This will help to extend the functionality of parent class method
        print("I can code")
    def display(self):
        print(f"Hi, I am {self.name} and I have {self.num_heart} heart.")
making=Male("chakra",2)
#making.eat()
making.work()  #this method prints "I can code" because it is overwritten in child class
making.flirt()
making.display()
```
