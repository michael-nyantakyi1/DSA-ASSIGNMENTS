#Author: Michael Adumatta Nyantakyi
#Student ID: 48682022
import random
import datetime

arr = []
N = int(input("Enter size of array: "))
for i in range(N):
    val = random.randint(1,32767)      #Generated sequence of N uniform random numbers between 1 & 32767
    arr.append(val)   
arr.sort()
tar = int(input("Enter target element: "))
print()

start = datetime.datetime.now()
def interpolSearch(arr,low,high,tar):         #Function returns the index of target element if present,and
                                              #returns -1 if target cannot be found
    if (low <= high and tar >= arr[low] and tar <= arr[high]):   
        pos = low + ((high - low)//(arr[high] - arr[low]) * (tar - arr[low])) 
   
        if arr[pos] == tar: 
            return pos
        
        if arr[pos] < tar:
            low = pos + 1
            return interpolSearch(arr,low,high,tar) 
          
        if arr[pos] > tar:
            high = pos - 1
            return interpolSearch(arr,low,high,tar) 
    return -1

idx = interpolSearch(arr,0,N - 1,tar)
if idx != -1:  
    print("Target found at index", idx) 
else:  
    print("Target not found")

end = datetime.datetime.now()
time_diff = (end - start)
execution_time = time_diff.total_seconds() * 1000   
print("Interpolation Search Method: %.3f ms"% execution_time,'\n')  #ISM execution time in milli-seconds

start = datetime.datetime.now()
def binarySearch(arr,leftsec,rightsec,tar):       #Function returns the index of target element if present,and
                                                  #returns -1 if target cannot be found
    if rightsec >= leftsec: 
        midpoint = leftsec + (rightsec-leftsec)//2
   
        if arr[midpoint] == tar: 
            return midpoint    
        
        elif arr[midpoint] > tar:
            rightsec = midpoint - 1
            return binarySearch(arr,leftsec,rightsec, tar) 
        
        else:
            leftsec = midpoint + 1
            return binarySearch(arr,leftsec,rightsec,tar) 
    else:  
        return -1

idx1 = binarySearch(arr,0,N - 1,tar)
if idx1 != -1:  
    print("Target found at index", idx) 
else:  
    print("Target not found")

end = datetime.datetime.now()
time_diff = (end - start)
execution_time = time_diff.total_seconds() * 1000   
print("Binary Search Method: %.3f ms"% execution_time)  #BSM execution time in milli-seconds