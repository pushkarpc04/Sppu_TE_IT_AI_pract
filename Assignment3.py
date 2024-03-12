#Write a program for sorting algorithms using appropriate knowledge representation and
#reasoning techniques
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def get_user_input_array():
    input_str = input("Enter space-separated integers for the array: ")
    arr = list(map(int, input_str.split()))
    return arr

def get_sorting_method():
    print("\nSelect sorting method:")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Selection Sort")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        arr = get_user_input_array()
        choice = get_sorting_method()

        if choice == '1':
            bubble_sorted_arr = list(arr)
            bubble_sort(bubble_sorted_arr)
            print("Bubble Sorted Array:", bubble_sorted_arr)
        elif choice == '2':
            merge_sorted_arr = list(arr)
            merge_sort(merge_sorted_arr)
            print("Merge Sorted Array:", merge_sorted_arr)
        elif choice == '3':
            selection_sorted_arr = list(arr)
            selection_sort(selection_sorted_arr)
            print("Selection Sorted Array:", selection_sorted_arr)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
