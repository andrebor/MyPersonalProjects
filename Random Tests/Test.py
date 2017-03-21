age = 21

if age >= 21:
    print("you can buy beer")
else:
    print("you can't buy beer")



foods = ["bacon", "tuna", "sausage", "ham", "beef",]
for f in foods[:2]:
    print(f)
    print(len(f))



for x in range(10):
    print("Bucky is awesome")



for x in range(5,13,3):
    print(x)


buttcrack = 5

while buttcrack < 10:
    print(buttcrack)
    buttcrack += 1
dos = [2*(10**-4), 10**-3, 5*(10**-3), 25*(10**-3), 10**-1, 5*(10**-1)]
levande = [20, 20, 19, 15, 11, 9]

import matplotlib.pyplot as plt
plt.plot(dos,levande)
plt.show()