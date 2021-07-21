target = 100
for i in range(1, target + 1):
    n = i
    if(i % 3 == 0 and i % 5 == 0):
        n = "ApaBole"
    elif(i % 3 == 0):
        n = "Apa"
    elif(i % 5 == 0):
        n = "Bole"
    
    end_ = ', ' if i != target else ' '
    print(n, end = end_)