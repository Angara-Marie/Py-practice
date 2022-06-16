# Accept two numbers from the user and return their sum, multiplication and division.
def sum_mult_div():
    num1 = int(input("Enter number:"))
    num2 = int(input("Enter number:"))
    sum = num1 + num2
    multiplication = num1 * num2
    division = num1 / num2
    return sum,multiplication,division
print(sum_mult_div())  
# Write all the contents of a given file to new file.
def copy_file():
    file = [2,3,4,5,6]
    new_file = [x.write() for x in file]
    print(new_file)    
copy_file()  
#Accept three input values from the user in one input() call.
word1,word2,word3=input("Enter three words:").split()
print(word1,word2,word3)  
