t = int(input())

for i in range(t):
    n = int(input())
    heroes = list(map(int, input().split()))

    if 0 in heroes:
        print(len(heroes) - heroes.count(0))
    elif len(set(heroes)) != len(heroes):
        print(len(heroes))
    else:
        print(len(heroes) + 1)