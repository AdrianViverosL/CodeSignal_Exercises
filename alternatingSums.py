def alternatingSums(a):
    team_1 = []
    team_2 = []
    output = []
    for i, value in enumerate(a):
        if (i % 2 == 0):
            team_1.append(value)
        else:
            team_2.append(value)
    
    output.append(sum(team_1))
    output.append(sum(team_2))
    
    return output
    
    
a = [50, 60, 60, 45, 70]
print(alternatingSums(a))