def bubble_sort(numbers):
    n = len(numbers)
    
    for i in range(n):
        for j in range(n - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
    return numbers

my_list = [5, 2, 8, 1, 4]
print(bubble_sort(my_list))
