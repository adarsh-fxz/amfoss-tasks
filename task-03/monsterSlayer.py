t = int(input())  # Number of groups of monsters

while t > 0:
    flag = True
    n = int(input())  # Number of monsters in each group
    health = list(map(int, input().split()))  # Health of each monster in each group

    if health[0] == 1:  
        print("YES")
    else:
        for i in range(1, n):
            if health[i] % health[0] != 0:
                flag = False
                break

        if flag:
            print("YES")
        else:
            print("NO")
    t -= 1