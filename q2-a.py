import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    with open("lista_arquivos.txt", "r") as f:
        file_list = f.read().splitlines()

    # Test Bubble Sort
    data = file_list[:]
    time_bubble = measure_time(bubble_sort, data)
    print(f"Bubble Sort: {time_bubble:.6f} seconds")

    # Test Selection Sort
    data = file_list[:]
    time_selection = measure_time(selection_sort, data)
    print(f"Selection Sort: {time_selection:.6f} seconds")

    # Test Insertion Sort
    data = file_list[:]
    time_insertion = measure_time(insertion_sort, data)
    print(f"Insertion Sort: {time_insertion:.6f} seconds")
