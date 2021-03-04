def sortByHeight(a):
    a_iterable = iter(enumerate(a))
    not_trees = sorted([i for i in a if i != -1])
    output=[]
    y=0

    for x in a_iterable:
        if x[1] != -1:
            output.append(not_trees[y]) 
            y+=1
        else:
            output.append(-1)

    return output





a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))