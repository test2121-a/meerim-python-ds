L = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
small = None

for num in L:
    if num > 0:
        if small is None or num < small:
            small = num
        
print(small)