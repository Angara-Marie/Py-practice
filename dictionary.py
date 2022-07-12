code={67:"Effence", 41:"Saido", 38:"Tessa", 58:"Nkimalantoi"}
print(code[67])
print(code.get(67))
print(code.get(101))
code[38]= "MARIE"
print(code)
code.update({38:"Tessa"})
print(code)
code[42]= "Munde"
print(code)
del code[58]
print(code)
my_dict= code.copy()
print(my_dict)
thisdict = dict(code)
print(thisdict)

# # Adding an item in a dictionary
# code[102]= "Shirleen"
# print(code)

# # Remove an elemnt from a dictionary
# code.pop(58)
# print(code)
# print(code.popitem())
# print(code)
# # Dictionary Comprehension
# squares = {x: x*x for x in range(6)}
# print(squares)

# #Write a program to check whether a given key exists in a dictionary or not.
# code={67:"Effence", 41:"Saido", 38:"Tessa", 58:"Nkimalantoi"}
# num =input("Enter key to check:")
# if 67 in code:
#     print("True")
# else: 
#     print("false")

#Write a program to iterate over dictionary items using for loop. 
code={67:"Effence", 41:"Saido", 38:"Tessa", 58:"Nkimalantoi"}
for key,val in code.items():
    print(f"the value of {key}, is {val}")
# Write a program to print only keys of a dictionary.
code={67:"Effence", 41:"Saido", 38:"Tessa", 58:"Nkimalantoi"}
print(code.keys())                                                                   

# Write a program to print values of dictionary.
code={67:"Effence", 41:"Saido", 38:"Tessa", 58:"Nkimalantoi"}
print(code.values())

# Write a program in python to map 2 lists into a dictionary.
names = ["Tessa", "Marie", "Angara"]
ages = [25,26,27]
my_dict={}
for name in names:
    for age in ages:
        my_dict[name]=age
print(my_dict)
