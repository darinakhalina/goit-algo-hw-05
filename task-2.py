def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    closest_larger = None
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value < x:
            low = mid + 1
        elif mid_value > x:
            closest_larger = mid_value
            high = mid - 1
        else:
            return mid_value, iterations

    return (
        (closest_larger, iterations)
        if closest_larger is not None
        else (arr[-1], iterations)
    )


if __name__ == "__main__":
    arr = [1.1, 2.5, 5.7, 11, 22.2, 35.5, 48.2, 55, 63.7, 100, 103.5, 112]
    x = 112

    larger_number, iterations = binary_search(arr, x)

    if larger_number == x:
        print(f"Елемент {x} знайдений на позиції {arr.index(x)}.")
        print(f"Кількість ітерацій: {iterations}.")
    elif x > max(arr):
        print(f"Введене число {x} більше за всі присутні числа.")
        print(f"Найбільше присутнє число: {max(arr)}.")
    else:
        print(f"Елемент {x} не знайдений.")
        print(f"Найближчий елемент: {larger_number}.")
        print(f"Кількість ітерацій: {iterations}.")
