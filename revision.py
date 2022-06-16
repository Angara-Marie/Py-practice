def string_length(strng):
    count = 0
    for char in strng:
        count += 1
        print(count)
string_length("Nalenyi")   

def string_length(strng):
    leng = len(strng)  
    print(leng)   
string_length("Marie")   

def char_frequency(strng):
    dict = {}
    for char in strng:
        x= dict.keys()
        if char in x:
            dict[char] += 1
        else:
            dict[char] = 1
    print(dict)    
char_frequency("susan") 

def slice_string(strng):
    if len(strng) < 2:
        print("")
    else:    
        print(strng[0:2] + strng[-2:])
slice_string("virginia")        
slice_string("h")  
slice_string("he")

def  first_char(strng):
    char = strng[0] #gets the 1st character of a string
    strng = strng.replace(char, "$")#changes the char to the dollar sign
    strng = char + strng[1:]
    return strng
print(first_char("restart"))# prints out "resta$t" 

x = int(input("Enter number:"))
for i in range(x):
    for t in range(i):
        print(i, end = "")
    print(i)    
    
def check_speed(speed):
    total_demerit = 0
    if speed < 70:
        print("OK")
    elif speed >= 70:
        excess_speed = speed - 70
        demerits = (excess_speed *1)//5
        total_demerit+=demerits
        print(total_demerit)
        if total_demerit > 12:
           print("License suspended")    
check_speed(360)  

x = [{20:"you"}, {21:"me"}, {22:"them"}]
for i in x:
    name = i.values()
    age = i.keys()
    year = 2022 - age
    print(f"Hello {name} you were born in {year}")


    