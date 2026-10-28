# Создаёт новую функцию: сначала применяет g, потом f
def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed


if __name__ == "__main__":
    composed = compose(lambda x: x * 2, lambda x: x + 1)

    x = 5
    print(f"Исходное число: {x}")
    print(f"double(increment(5)) = {composed(x)}")
