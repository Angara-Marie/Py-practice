char = input("Enter character:")
vowels = ["a", "e", "i", "o", "u"]
if char in vowels:
    print(f"{char} is a vowel")

else:
    print(f"{char} is a consonant")

even_count = 0
odd_count = 0
for num in range(10,55):
    if num % 2 == 0:
        even_count+=1
    elif num % 2 != 0:
        odd_count += 1
print(f"even numbers is {even_count}")
print(f"odd numbers is {odd_count}")     

def accelerate(v1,v2,t1,t2):
    acceleration = (v2 - v1) / (t2 - t1)
    return acceleration
print(accelerate(0, 10, 0 ,20)) 

num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))
num3 = int(input("Enter number:"))
my_list= []
my_list.append(num1)
my_list.append(num2)
my_list.append(num3)
my_list.sort()
print(my_list)

for num in range(10, 25):   
    if num % 5 != 0:
        print(num)

num = input("Enter number:")
my_list = [1,2,3,4,2,3,4,3]
count = 0
for x in range(len(my_list)):
    if my_list[x] == num:
        count+=1
print(f"{num} has occured {count} times")

word = input("Enter word:")
strng = "I love you, I love you"
number= strng.count(word)
print(f"{word} has been repeated {number} times")

number = int(input("Enter number"))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

def numbers(num1, num2):
    product = num1 * num2
    sum = num1 + num2 
    if product > 500:    
        return sum
print(numbers(125, 6))   

def greatest():
    num1=int(input("Enter number"))
    num2=int(input("Enter number"))
    num3=int(input("Enter number"))
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the greatest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the greatest") 
    else:
        print(f"{num3} is the greatest")  
greatest()

def multiple_of_five():
    for num in range(10,50):
        if num % 5 == 0:
            print(num)
multiple_of_five()            

def word(strng):
        if strng[0] == strng[-1]:
            return True

        else:
            return False
print(word("Tessa") )   

for i in range(1,6):
    for j in range(1, i+1):
       print("*", end=" ")        
           

