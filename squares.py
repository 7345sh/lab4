# Вычисление квадратов чисел от 1 до 10 с помощью map
def get_squares(numbers: list[int]) -> list[int]:
    # map применяет лямбду к каждому элементу списка
    return list(map(lambda x: x ** 2, numbers))


if __name__ == "__main__":
    nums = list(range(1, 11))
    result = get_squares(nums)
    print(f"Исходные числа: {nums}")
    print(f"Квадраты: {result}")
