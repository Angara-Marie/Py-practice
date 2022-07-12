#Write a program to reverse a string in python.
strng = input("Enter word:")
new_word= ""
for char in strng:
    new_word = char + new_word
print(new_word)   
#Write a program to remove duplicates in a string.
strng =input("Enter word:")
new_word =[]
for char in strng:
    if char not in new_word:
        new_word.append(char)
print(str(new_word))
# Write a program to count the number of letters in a word
strng = input("Enter word:")
count = 0
for char in range(len(strng)):
    count+=1
print(count)

# # Python program to count the occurrence of each character in a word.
strng = input("Enter word:")
dict = {}
for char in strng:
    keys = dict.keys()
    if char in keys:
        dict[char]+=1
    else:
        dict[char]=1
print(dict)            
# Python program to convert lower letter to upper and upper letter to lower in a string.
strng = input("Enter word:")
new_word=[]
for x in range(len(strng)):
    if strng[x].islower():
        new_word.append(strng[x].upper())
    elif strng[x].isupper():
        new_word.append(strng[x].lower())  

for x in range(len(new_word)):
    print(new_word[x],end='')

# Write a python program to sort letters of word by lower to upper case format.
strng = input("Enter word:")
lower = []
upper = []
for x in range(len(strng)):
    if strng[x].islower():
        lower.append(strng[x])
    else:
        upper.append(strng[x])

result = "".join(lower+upper)
print(result)   

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string.
word= input("Enter word")
if len(word) < 2:
    print("")
else:
    print(word[0:2] + word[-2:]) 


#  Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
def replace_char(word):
       char = word[0].lower()
       strng= word.replace(char, '$')
       strng = char + strng[1:]
       print(strng)
replace_char("Angara")  

# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
def swap_char(strng1, strng2): 
       single_strng =strng2[:2] + strng1[2:] + " " +strng1[:2] + strng2[2:]
       print(single_strng)
swap_char("Tessa", "Marie")   

#  Given a string, convert the first half of the string to upper and the other half to lower.
def case_converter(word):
       half_index = len(word) // 2
       result = ""
       for char in range(len(word)):
              if char < half_index:
                     result += word[char].upper()
              else:
                     result += word[char]   
       print(result) 
case_converter("tessa")   

x=[1,2,45,6,8,"winter"]
z= set(dict.fromkeys(x))
print(z) 