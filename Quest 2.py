#Author: Michael Adumatta Nyantakyi
#ID: 48682022
'''This function defines a rectangle class that returns
the area, perimeter, and whether two rectangles intersect'''

class Point:
    def __init__(self,xcord=0,ycord=0):
        self.xcord = xcord
        self.ycord = ycord
        
    def get_xcord(self):
        return self.xcord 
    
    def get_ycord(self):
        return self.ycord 

        
class Rectangle:
    def __init__(self,blc,trc):   #blc: bottomLeftCorner, trc: topRightCorner
        self.blc = blc
        self.trc = trc
        
    def get_blc(self):
        return self.blc
    
    def get_trc(self):
        return self.trc
                
    
    def area(self):          #Function returns area of rectangle
        xval = (self.trc[0] - self.blc[0])
        yval = (self.trc[1] - self.blc[1])
        return xval*yval
    
    def perimeter(self):      #Function returns perimeter of rectangle
        xval = (self.trc[0] - self.blc[0])
        yval = (self.trc[1] - self.blc[1])
        return 2*(xval+yval)

    
def intersect():    #Checks whether two rectangles intersect or not and returns True or False
    p1 = Point()
    p1.xcord = int(input("Enter x1:"))
    p1.ycord = int(input("Enter y1:"))
        
    p2 = Point()
    p2.xcord = int(input("Enter x2:"))
    p2.ycord = int(input("Enter y2:"))
        
    p3 = Point()
    p3.xcord = int(input("Enter x3:"))
    p3.ycord = int(input("Enter y3:"))
        
    p4 = Point()
    p4.xcord = int(input("Enter x4:"))
    p4.ycord = int(input("Enter y4:"))
        
    if p1.xcord >= p2.xcord or p3.xcord >= p4.xcord:
        return False
    if p1.ycord <= p2.ycord or p3.ycord <= p4.ycord:
        return False
    return True


r1 = Rectangle((5,5), (30, 20))
print('Area:',r1.area())
print('Perimeter:',r1.perimeter(),'\n')
print(intersect()) #To test try points (0,10),(10,0),(5,5),(15,0)
