#Write a program to create a list with random data types elements.
list_x = [22,"Tessa", 2.0]
for x in range(len(list_x)):
    print(list_x[x],type(x), end=",")

#Write a program to print all the elements of a list in single line.
list_y = [23,34,45,56,67]   
for x in range(len(list_y)):
    print(list_y[x], end=" ") 

#Write a program to count the number of items stored in a list.
list_y = [23,34,45,56,67]
count= 0
for x in list_y:
    count+=1
print(count)  

#Write a program to reverse a list in Python.
list_y = [23,34,45,56,67]
new_list = list_y[::-1]
print(new_list)

#Python program to square each element of a list.
my_list = [2,3,4,5,6,7]
new_list = [x**2 for x in my_list]
print(new_list)

#Python program to remove an empty element from a list.
my_list = ["Tessa", "", "Marie", "", "Angara"]
while "" in my_list:
    my_list.remove("")
print(my_list)

#Python program to append an element to a list.
my_list = [2,3,4,5,6,7]
my_list.append("Tessa")
print(my_list)

#Write a program to display those items from a list that is divisible by 5.
my_list = [20, 30,22,43,50]
for i in my_list:
    if i % 5 == 0:
       print(i, end=" ")

#Write a program to sum all the elements of a list.
my_list = [20, 30,22,43,50]
result = sum(my_list)
print(result)

#Write a program to get the maximum number from a list.
my_list = [20, 30,22,43,50]
maximum = max(my_list)
print(maximum)

#Write a program in Python to remove duplicate items from a list.
my_list = [20, 30,22,43,50,20]
new_list = []
for x in my_list:
    if x not in new_list:
        new_list.append(x)
print(new_list)

#Write a program to append data of the second list to the first list.
my_list = [20, 30,22,43,50]
list_y = [23,34,45,56,67]
for x in range (len(list_y)):
    my_list.append(list_y[x])
print(my_list)

#Write a program in Python to filter odd and even number from a list.
my_list = [20, 30,22,43,50,33]
even = []
odd = []
for x in my_list:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print(odd)
print(even)    

