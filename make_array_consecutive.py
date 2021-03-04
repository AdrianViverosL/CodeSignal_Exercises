def makeArrayConsecutive2(statues):
    statues.sort()
    print(statues)
    
    lst = [i for i in range(statues[0], statues[-1])]
    print(lst)

    diff = (len(lst) - len(statues)) + 1

    print(diff)

statues = [6, 2, 3, 8]

makeArrayConsecutive2(statues)