#Author: Michael Adumatta Nyantakyi
#Student ID: 48682022

maxArraySize = 100     #defined maximum size of array
import random

class Deque:
    def __init__(self):
        self.arr = []
    
    def isFull(self):                    #function checks whether the deque is full or not
        return len(self.arr) == 100    
    
    def isEmpty(self):                   #function checks whether the deque is empty or not
        return self.arr == []
    
    def addFront(self,x):                #function adds x to the front of the sequence
        self.arr.insert(0,x)
        
    def addRear(self,x):                 #function adds x to the back of the sequence
        self.arr.append(x)    
        
    def removeFront(self):               #function removes and returns the front element of the sequence
        if (self.arr == []):
            print("Deque is empty")     
        else:
           self.arr.pop(0)
           
    def removeRear(self):                #function removes and returns the last element of the sequence
        if (self.arr == []):
            print("Deque is empty")
        else:
           self.arr.pop()
           
    def size(self):                      #function checks number of elements in the deque
        return len(self.arr)

sim = Deque()
halfFull = maxArraySize//2

for i in range(halfFull):
    val = random.randint(1,100)
    sim.addRear(val)

arr = random.uniform(0,1)
print("Uniform random number generated between 0 & 1 is: %.3f"% arr)

print("First row simulation")
if arr > 0 and arr <= 0.1:
    val = random.randint(1,100)
    print("Random integer generated is: ",val)
    sim.addFront(val)
    
if arr > 0.1 and arr <= 0.3:
    val = random.randint(1,100)
    print("Random integer generated is: ",val)
    sim.removeFront()
    
if arr > 0.3 and arr <= 0.4:
    val = random.randint(1,100)
    print("Random integer generated is: ",val)
    sim.addRear(val)
    
if arr > 0.3 and arr <= 1:
    val = random.randint(1,100)
    print("Random integer generated is: ",val)
    sim.removeRear()
    
print()    
print("Second row simulation")
if arr > 0 and arr <= 0.1:
    val = random.randint(1,100)
    print("Random integer generated is: ",val)
    sim.addFront(val)
    
if arr > 0.1 and arr <= 0.7:
    val = random.randint(1,100)
    print("Random integer generated is: ",val)
    sim.removeFront()
    
if arr > 0.7 and arr <= 0.8:
    val = random.randint(1,100)
    print("Random integer generated is: ",val)
    sim.addRear(val)
    
if arr > 0.8 and arr <= 1:
    val = random.randint(1,100)
    print("Random integer generated is: ",val)
    sim.removeRear()
            
print()
print("Array elements:", sim.arr)
print("Check if array is full:",sim.isFull())
print("Check if array is empty:",sim.isEmpty())
 