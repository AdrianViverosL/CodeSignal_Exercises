def isIPv4Address(inputString):
    x = inputString.split('.')
    x = [item for item in x if (len(item)>1 and item[0] != '0') or len(item) == 1]
    #print(x)
    
    try:
        x = [int(i) for i in x if i != '']

    except ValueError:
        return False
    
    if(len(x) != 4):
        return x, False
    
    for value in x: 
        if value not in range(0,256):
            return x, False

    return x, True
    
    #return len(x) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in x )

print(isIPv4Address("172.16.254.1")) #True
#print(isIPv4Address("172.316.254.1")) #False 316 is not in the range 0, 255
#print(isIPv4Address(".254.255.0")) #False, first number missing
print(isIPv4Address("01.233.161.131")) 
print(isIPv4Address("0..1.0.1")) 