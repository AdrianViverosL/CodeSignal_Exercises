def arrayChange(inputArray):
    print(len(inputArray))
    moves = 0
    
    for i in range(len(inputArray)-1):
        if(inputArray[i]>=inputArray[i+1]):
            #inputArray[i+1]+=(inputArray[i] - inputArray[i+1])+1
            m = (inputArray[i] - inputArray[i+1])+1
            inputArray[i+1]+=m
            moves += m

    return inputArray, moves

input = [1,1,1]
print(arrayChange(input))