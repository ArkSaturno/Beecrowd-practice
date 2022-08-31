X = int(input())

while(X > 0):
    M = int(input())
    vector = []

    for i in range(M):
        if i%2 == 0:
            vector.append(1)
        else:
            vector.append(-1)


    print(sum(vector))
    X -= 1