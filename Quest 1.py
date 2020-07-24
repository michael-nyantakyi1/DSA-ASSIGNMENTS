#Author: Michael Adumatta Nyantakyi
#ID: 48682022
#This function returns the dot product of two lists, each of size N

import numpy as ny
import random

def DotProduct():
    ListA = []    
    ListB = []
    N = int(input("Enter size of lists: "))
    
    for i in range(0,N):     #iteration for size of each array 
        L1 = random.randint(1,1000)     #Uniform random variates of ListA between 1-1000
        ListA.append(L1)        #Every random integer generated is added to the list till the specified size is met
        L2 = random.randint(1,1000)     #Uniform random variates of ListB between 1-1000
        ListB.append(L2)
    
    print(ListA)
    print(ListB)
    dp = ny.dot(ListA, ListB)        #this function determines the dotproduct of ListA & ListB
    print(dp)
    
DotProduct()