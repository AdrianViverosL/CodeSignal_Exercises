def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return sum([yourLeft,yourRight]) == sum([friendsLeft,friendsRight]) and max([yourLeft,yourRight]) == max([friendsLeft,friendsRight])

yourLeft = 10 
yourRight = 15 
friendsLeft = 15
friendsRight = 10
print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))