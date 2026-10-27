# Генератор чисел Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        # Формула получения следующего числа
        a, b = b, a + b


if __name__ == "__main__":
    gen = fibonacci()
    # Запрашиваем первые 10 чисел через next()
    first_10 = [next(gen) for _ in range(10)]
    print(f"Первые 10 чисел Фибоначчи: {first_10}")
