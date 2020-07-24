#This program finds the nth number of the fibonacci sequence

def fibo(n):
    first_num = 0          #First fibonacci number is 0
    sec_num = 1            #Second fibonacci number is 1
    if n == 0:
        return first_num
    if n == 1:
        return sec_num
    else:
        for i in range(1,n-1): 
            output = sec_num + first_num 
            first_num = sec_num
            sec_num = output
        return sec_num

print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))