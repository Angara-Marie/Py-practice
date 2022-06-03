temp = 35
if temp > 30:
    print("I'ts warm")
elif temp > 20:
    print("Its nice") 
else:
    print("Done")    
# first 10 even numbers
num = 0
while num <= 20:
    num += 1
    if num % 2 == 0:
        print(num)
#first 10 odd numbers
num = 0
while num <= 20:
    num += 1  
    if num % 2 != 0:
        print(num)  

num = 0
while num < 10:
    num += 1
    print(num)            

num = -1
while num < 10:
    num += 1
    print(num)

num = 1   
while num < 20:
    print(num, num*num)
    num+=1