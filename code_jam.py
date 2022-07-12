var= "james bond"
print(var[2::-1])

sample = {"Jodi", "Erick", "Garry"}
sample.add("vicki")
print(sample)

var = "James" *2*3
print(var)

for i in range(10, 15,2):
    print( i, end=',')

def calculate(num1, num2=4):
    res = num1*num2
    print(res)    
calculate(5)
for i in range(1,5):
    print(i)
else:

    print("this is else block statment")   
var1=1
var2=2
var3="3"
print(var1+var2+var3)

listOne=[20,40,60,80]
listTwo=[20,40,60,80]

print(listOne==listTwo)
print(listOne is listTwo)

range =(1,200)
x = 1
while x in range(1,20):
    x+=1
    if x % 2 == 0:
        print(x)

listx=[30,60,1,20,32]
smallest = 0
for item in listx:
    if item < listx[listx.index(listx[0])-1] and item<smallest:
        smallest=item
        print(smallest)
list_a= [10,20,30,40,50,60]
list_b= [20,80]
for x in list_a:
    if x in list_b:
        print(True)

if 'bar' in {'foo' :1,'bar': 2,'baz':3}:
   print(1)
   print(2)
   if 'a' in 'qux':
     print(3)
print(4) 

a= 100
b= 50
if a >b:
  m=b
  print(m) 
else:
    m=a
    print(m)   

print('a' + 'x' if '123'.isdigit() else 'y' + 'b')






