L = [1, 5, 1, 2, 3, 4, 5, 6, 2, 8, 3, 1, 1, 12, 13, 14, 15, 16, 17, 12, 1]

max = 0
curr = None

for i in L:
    c = 0
    for j in L:
        if i == j:
            c += 1
    if c > max:
        max = c
        curr = i
        
print(curr)