def matrixElementsSum(matrix):
    #print([i for i in matrix])
    haunted = []
    a_rooms = []
    
    for x in range(0,len(matrix)):
        #print(matrix[x])
        #e_lst = list(iter(enumerate(matrix[x])))
        e_lst = iter(enumerate(matrix[x])) 
        #print(e_lst)
        for y in e_lst:
            #print(y)

            if y[0] in haunted:
                pass
            else:
                if(y[1] != 0):
                    a_rooms.append(y[1])
                else:
                    haunted.append(y[0])

    print(a_rooms)
    print(haunted)
    return(sum(a_rooms))        

    
    

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

total = matrixElementsSum(matrix)
print(total)