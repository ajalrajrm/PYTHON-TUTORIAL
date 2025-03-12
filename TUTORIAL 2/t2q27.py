def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:  # If no swaps were made, the list is already sorted
            break

n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]
bubble_sort(nums)
print("Sorted list:", nums)
