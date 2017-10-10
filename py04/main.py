from math import pi
import math
class Geometrie(object):
    def __init__(self):
        pass
    def computer_area(self):
        pass


class Rectangle(Geometrie):
    def __init__(self,h,w):
        self.h=h
        self.w=w
    def area(self):
        return self.h*self.w
    
class Square(Rectangle):
    def __init__(self, h):
        self.h=h
        self.w=h
        
class Ellipse(Rectangle):
    def __init__(self,h,w):
        self.h=h
        self.w=w
        
class Circle(Geometrie):
    def __init__(self,r):
        self.r=r
    def area(self):
           return pi*self.r*self.r

shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5), Square(15),Ellipse(10, 20),]
def compute_area(shapes):
	areas=0
	for shape in shapes:
		areas+=shape.area()
	return areas
if __name__ =="__main__":
	total_area = compute_area(shapes);
	print(total_area)
