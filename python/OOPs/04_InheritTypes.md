# Five(5) types of inheritance
- Single inheritance (One parent class and one child class)
- Multiple inheritance (Child class inherit properties from more then 1 parent classes) - Child from mother & father
- Miltilevel inheritance
- Hierarchical inheritance
- Hybrid inheritance

# Multipule inheritance
```
class Human:
    def __init__(self,lang):
        self.num_eyes=2
        self.num_nodes=1
    def eat(self):
        print("I can eat")
#    def work(self):
#        print("I can work")

class Male():
    def __init__(self,name):
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")
class Boy(Human,Male):
    def __init__(self,name,lang):
        Human.__init__(self,lang)
        Male.__init__(self,name)
#     def work(self):
#         print("I can test")
boy_1 = Boy("chakra","hindi")
#boy_1.flirt()
#boy_1.eat()
#boy_1.work() #This will call work method of first class inherited based on order that is Human.
             #After changing order class Boy(Male,Human), it will call method from Male class
#print(Boy.mro()) #Method resolution order, it resolves first Boy class,Male class and then Human class
                 #[<class '__main__.Boy'>, <class '__main__.Male'>, <class '__main__.Human'>, <class 'object'>]

#Human.work(boy_1) #to overcome this use class.method(object)
print(boy_1.num_eyes)
```
