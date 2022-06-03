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
        keys= dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
            print(dict)    
char_frequency("Tessa") 

def slice_string(strng):
    if len(strng) < 2:
        print("")
    else:    
        print(strng[0:2] + strng[-2:])
slice_string("virginia")        
slice_string("h")  
slice_string("he")