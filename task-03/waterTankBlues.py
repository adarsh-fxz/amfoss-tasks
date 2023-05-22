t = int(input())

while t > 0:
    count = 0
    n = int(input())  # Number of water tanks
    water = list(map(int, input().split()))  # Amount of water in each tank

    for i in range(1, n):
        if water[i] == 0 and water[i-1] != 0:
            water[i] += 1
            water[i-1] -= 1
            count += 1

    for i in range(n-1):
        count += water[i]

    print(count)
    t -= 1