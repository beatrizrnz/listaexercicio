valores=[1, 1, 2, 2, 3, 4, 8, 9, 9]
valores1= []
for a in valores:
    if a not in valores1:
        valores1.append(a)
print(valores1)