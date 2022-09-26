# num=int(input("Enter number:"))
# fac=1
# x=1
# while x<=num:
#     fac=fac*x
#     x+=1
# print(fac)
# #Write a Python program to reverse a number.

# x="14346"
# y = x[::-1]
# print(y)

# # list with random data types
# rand = [22, "Tessa", 22.3]
# for item in range(len(rand)):
#     print(rand[item], type(rand[item]))

# # print all elements of a list in a single line
# num = [23,24,25,26,27]
# for i in range(len(num)):
#     print(num[i], end=" ")

# # count number of items stored in a list
# numbers = [23,24,25,26,27]
# count = 0
# for item in range(len(numbers)):
#     count += 1
# print(count)

# # reverse a list
# nums = [23,24,25,26,27]
# new_list = nums[::-1]
# print(new_list)

# # square each element
# numbers = [2,3,4,5,6,7]
# new_list = [x**2 for x in numbers]
# print(new_list)

# # remove an empty element
# num = ["Hello", 34,35,"",40]
# # my_list = num.remove("")
# # print(my_list)
# while "" in num:
#     num.remove("")
#     print(num)

# # append an element to a list
# num =[23,45,67,8,9]
# element =input ("Enter item to insert:")
# num.append(element)
# print(num)

# # items from a list that is divisible by 5
# numbers = [2,3,5,120,10,15,33]
# new_list = [num for num in numbers if num % 5 == 0] 
# print(new_list) 

# Append list2 to list1
list_1 = [23,24,25,26]
list_2 = [27,28,29,30]
# list_3 = [list_1.append(list_2[i]) for i in range(len(list_2))]
# # # print(list_1.append(list_2))
# # list_1.extend(list_2)
# print(list_3)
# print(*list_1, *list_2)
# [list_1.append(i) for i in list_2]
# print(list_1)

res_list = [y for x in [list_1, list_2] for y in x]
print(res_list)
