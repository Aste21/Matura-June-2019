def czy_pierwsza(x):
    k = 2
    while k*k <= x:
        if x%k == 0:
            return False
        k=k+1
    return True



f = open('liczby.txt', 'r')
print(f"4.1: ")
for linia in f:
    x = int(linia.strip())
    if czy_pierwsza(x) and x >= 100 and x <= 5000:
        print(x)

