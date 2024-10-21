- Find the circumference of a circle when a radius is passed.
- formula circumference = 2*pi*r and area = pi*r*r
- pi is always same or constant, declare it as class attribute.
```
class Circle:
    pi = 3.14
    def __init__(self,radius=6):
#    def __init__(self, radius):
        self.radius=radius
        self.area=self.pi*radius*radius
    def get_circim(self):
        return 2*self.pi*self.radius

circle_1 = Circle()
circle_2 = Circle(4)
print(circle_1.get_circim())
print(circle_2.get_circim())
print(circle_2.area)
```
