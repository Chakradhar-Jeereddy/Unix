- class is a blueprint like idly maker, makes idlies faster and easier to make
- variables inside class are called attributes, they are associated with the class not freely floating
- Functions inside the class are called methods, they are associated with class
- Attributes stores information and methods does something using the information stored in attributes.
```
#class Chakra:
#    def meth(self):
#        print("My name is chakradhar jeereddy")
#l = Chakra()
#b = Chakra()
#print(l)
#print(b)

# old school method off declaring attributes
class Info:
    def __init__(self):
        pass
        #print("creating an object")
info = Info()
info.name = 'Chakradhar'
info.lastname = 'Jeereddy'
info.country = 'Canada'
#print(info.name,info.lastname,info.country)

# Constructor will tell what would happen when object is created, it will initialize to store attributes
# To construct or initialize we use init mettod __init__, it is a predefined method and python knows what to do
# when it is defined

class Info2:
    def __init__(self):
        print("creating an object")

#bol = Info2() # Every time we create an object the init function is called
#bai = Info2() # Every time we create an object the init function is called
#print(bol,bai)  # Every time we create an object the init function is called
class Info2:
    def __init__(self,name,address):
        self.iname=name
        self.iaddress=address
        self.city='montreal'  # As city always remains same, we have a default value
kung = Info2('Chakradhar','Canada')
#print(kung.iname, kung.iaddress,kung.follower)

#class Chakra:
#    def __init__(self,name,address):   #self is referring to object itself here the object is "chakra_object"
#      self.myname=name
#      self.address=address

#chakra_object = Chakra('chakra','canada')  #passing arguments is mandatory, unless it is defined with default value
#print(chakra_object.myname)


## Methods are to define what function has to do.

class Chakra:
    def __init__(self,name,address):   #self is referring to object itself here the object is "chakra_object"
      self.myname=name
      self.address=address
#def display(self):
# This will accept subject name as string
    def display(self,subject_name):
       print(f"hi, my name is {self.myname} and I teach {subject_name}.")   # no need to use self.subject_name, 
       # it is local parameter of function
#      print("Hi {self.myname}") #you need to use self.myname, because it is attribute and not variable.
#      return 0

chakra_object = Chakra('chakra','canada')  #passing arguments is mandatory, unless it is defined 
# with default value
#print(chakra_object.myname)
#print(chakra_object.display())  # we get "hi chakra" and None, the None we get because there is no return 
# statement in funtion
#chakra_object.display()         # removed the print, now it returns only "Hi chakri"
#chakra_object.display("python")

#Define class

class Chakra:
# Intitialize the class, what should happen when object is created.
  def __init__(self,name,address):  #name, address accept string object
      self.myname=name
      self.address=address #the attribute name can be same or anything but parameter name should match.
      self.follower=0
  def display(self,subject_name): #subject_name accepts string object
      print(f"Hi, I am {self.myname} I teach {subject_name}") #myname is attribute, it needs self, subject_name is variable
  def follwers(self,follower):
      self.follower+=1
      print(self.follower)
chakra_object=Chakra('chakra','canada')
chakra_object.display('java')
chakra_object.follwers("chakra")

```
