L = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
new_L = []

for number in L:
    if (number % 3 == 0) and (number % 5 == 0):
        new_L.append(number)

print(new_L)