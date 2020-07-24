#Author: Michael Adumatta Nyantakyi
#Student ID: 48682022

maxArraySize = 100
import random

class Deque:
    def __init__(self):
        self.arr = []
    
    def isFull(self):
        return len(self.arr) == 100    #maxArraySize=100
    
    def isEmpty(self):
        return self.arr == []
    
    def addFront(self,x):
        self.arr.insert(0,x)
        
    def addRear(self,x):
        self.arr.append(x)    
        
    def removeFront(self):
        if (self.arr == []):
            print("Deque is empty")     
        else:
           self.arr.pop(0)
           
    def removeRear(self):
        if (self.arr == []):
            print("Deque is empty")
        else:
           self.arr.pop()
           
    def size(self):
        return len(self.arr)

halfFull = maxArraySize//2
for i in range(halfFull):
    val = random.randint(1,100)
    Deque.addRear(val)
n = random.uniform(0,1)

if n > 0 and n <= 0.1:
    val = random.randint(1,100)
    Deque.addFront(val)
    
if n > 0.1 and n <= 0.2:
    val = random.randint(1,100)
    Deque.removeFront()
    
if n > 0.2 and n <= 0.4:
    val = random.randint(1,100)
    Deque.addRear(val)
    
if n > 0.4 and n <= 0.6:
    val = random.randint(1,100)
    Deque.addRear()
            
        
        
    