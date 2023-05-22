n, m = map(int, input().split())

a = m/n

def minRounds(a):
    count = 0
    while True:
        if a%2 == 0:
            a = a//2
        elif a%3 == 0:
            a = a//3
        elif a == 1:
            break
        else:
            count = -1
            break
        count += 1
    return count

print(minRounds(a))