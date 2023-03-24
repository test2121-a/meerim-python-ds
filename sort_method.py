def sort_array(arr):
    n = len(arr)
    for i in range(n):
        j = i + 1
        while j < n:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

if __name__ == '__main__':
    arr = [10, 5, 11, 3]
    sorted_arr = sort_array(arr)
    print(sorted_arr)
