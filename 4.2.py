def czy_pierwsza(x):
    k = 2
    while k*k <= x:
        if x%k == 0:
            return False
        k=k+1
    return True

f = open('pierwsze.txt', 'r')

print(f"4.2: ")

for linia in f:
    x = linia.strip()
    l = ''
    for i in range(len(x)-1,-1,-1):
        l += x[i]
    l = int(l)
    if czy_pierwsza(l):
        print(x)
