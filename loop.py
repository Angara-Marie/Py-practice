# Write a program in Python to display the Factorial of a number
num = int(input("Enter number:"))
fac = 1
x = 1
while x<=num:
    fac = fac * x  
    x+=1
print(f"factorial of {num} is {fac}")
#REverse string
def word(strng):
    new_word=""
    for char in strng:
        new_word = char + new_word
    print(new_word)
word("Tessa")        

def squares():
    new_list=[]
    my_list = [2,3,4,5,6,7,8]
    for num in my_list:
        new_list.append(num**2)
    print(new_list)
squares()
def types():
    list_x = [23, "Python", 25.98]
    for x in list_x:
      new_list = [type(x)]
      print(new_list)
types()
# WAP to separate positive and negative number from a list.
list_x = [23,4,-6,25,-8,22,-9]
pos=[]
neg=[]
for i in range(len(list_x)):
    if list_x[i] < 0:
        neg.append(list_x[i])
    else:
        pos.append(list_x[i])   
print(pos)
print(neg)     
#Define a function that accepts 2 values and return its sum, subtraction and multiplication.
def sum_sub_mult(num1, num2):
    sum = num1 + num2
    subtraction= num1-num2
    multiplication= num1*num2
    return sum,subtraction,multiplication
print(sum_sub_mult(25,20))  
#Define a function that accepts roll number and returns whether the student is present or absent.
def number(roll) :
    numbers = [23,25,26,28,29]
    if roll in numbers:
        print("Student is present")
    else:
        print("Student is absent")       
number(23)   
#Define a function in python that accepts 3 values and returns the maximum of three numbers.
def maximum(a,b,c):
    if a > b and a > c:
        print(f"{a} is the greatest")
    elif b > a and b > c:
        print(f"{b} is the greatest")   
    else:
        print(f"{c} is the greatest") 
maximum(22,23,24)     
#Define a function which counts vowels and consonant in a word.
def count(strng):
    vowels= ['a','e','i','o','u']
    vowel_count = 0
    const_count = 0
    for char in strng:
        if char in vowels:
            vowel_count+=1
        else:
            const_count+=1   
    print(f"The number of vows is {vowel_count} and that of consonants is {const_count}") 
count("Tessa")  
#Define a function that accepts lowercase words and returns uppercase words.
def lower(word):
    result = word.upper()
    print(result)
lower("Tessa")    
#Define a function that accepts radius and returns the area of a circle.
def area(radius):
    Area = 3.142 * radius**2
    return Area
print(area(21))    
