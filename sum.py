from functools import reduce


# Вычисление суммы чисел с помощью reduce
def sum_numbers(numbers: list[int]) -> int:
    # reduce последовательно применяет лямбду к парам элементов:
    return reduce(lambda a, b: a + b, numbers)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    total = sum_numbers(nums)
    print(f"Числа: {nums}")
    print(f"Сумма: {total}")
