# Генератор: читает файл построчно и отдаёт только числа > threshold
def filter_numbers(filename: str, threshold: int):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:           # пропускаем пустые строки
                continue
            try:
                number = int(line)
            except ValueError:     # если не число — пропускаем
                continue
            if number > threshold:
                yield number       # отдаём число наружу и замираем


if __name__ == "__main__":
    # Получаем все числа больше заданного
    x = 20
    file = "data.txt"
    filtered = list(filter_numbers(file, x))
    print(f"Числа больше {x}: {filtered}")
