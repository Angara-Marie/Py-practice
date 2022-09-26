import ipaddress

# def solution(S):
    
# # Splitting by "."
#     S = S.split(".") 
#     print(S)
#     # counter = 0
#     # for i in S:
#     #     print(i)
#     #     if len(i) <= 3 and int(i) >= 0 and int(i) <= 255:
#     #         counter += 1 
#     #         return counter
# solution('255255255255')
def convert(s):
    length= len(s)
 
    # Check for string size
    if length > 12:
        return []
    possible_ip = s 
 
    # Generating different combinations.
    for x in range(1, length - 2):
        for y in range(x + 1, length - 1):
            for z in range(y + 1, length):
                possible_ip = possible_ip[:z] + "." + possible_ip[z:]
                possible_ip = possible_ip[:y] + "." + possible_ip[y:]
                possible_ip = possible_ip[:x] + "." + possible_ip[x:]

                possible_ip = s
                counter = 0
                for i in possible_ip:
                    if len(i) <= 3 and int(i) > 0 and int(i) <= 255 and i[0] != 0:
                        counter += 1
                    return counter
    
print(convert("255255255255"))  