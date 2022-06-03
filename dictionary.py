code={67:"Effence", 41:"Saido", 38:"Tessa", 58:"Nkimalantoi"}
print(code[67])
print(code.get(67))
print(code.get(101))

# Adding an item in a dictionary
code[102]= "Shirleen"
print(code)

# Remove an elemnt from a dictionary
code.pop(58)
print(code)
print(code.popitem())
print(code)
# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

print(squares)




