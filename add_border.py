def addBorder(picture):
    output = []
    b_picture = []
    for item in picture:
        item_ls = list(item)
        item_ls.insert(0, '*')
        item_ls.append('*')
        output.append(item_ls)
    
    frame = ['*' for i in range(len(item_ls))]
    output.insert(0, frame)
    output.append(frame)

    for i in output:
        item_str = ''.join(char for char in i)
        print(item_str)
        b_picture.append(item_str)
    #output = [str(i) for i in output]
    #print(frame) 
    #print(output)
    return b_picture

picture = ["abc",
           "ded"]

print(addBorder(picture))