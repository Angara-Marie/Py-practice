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