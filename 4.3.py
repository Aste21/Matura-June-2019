def w(x):
    y = x
    while len(y)>1:
        z = 0
        for i in range(len(y)):
            z += int(y[i])
        y = str(z)
    return int(y)

ile = 0

f = open("pierwsze.txt", "r")

for linia in f:
    x = linia.strip()
    if w(x) == 1:
        ile += 1
print(f"4.3:  {ile}")
