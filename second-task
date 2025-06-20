import random as _rnd


def get_numbers_ticket(
        min_value: int,
        max_value: int,
        quantity: int,
) -> list[int]:
    """
    Генерує відсортований список *quantity* унікальних випадкових чисел
    у діапазоні [min_value, max_value].

    ▸ min_value ≥ 1, max_value ≤ 1000
    ▸ quantity не перевищує кількості доступних чисел
    ▸ повертає [] у разі будь‑якої невідповідності вимогам
    """
    # Перевірка вхідних параметрів
    is_valid = (
            isinstance(min_value, int)
            and isinstance(max_value, int)
            and isinstance(quantity, int)
            and 1 <= min_value <= max_value <= 1000
            and 1 <= quantity <= (max_value - min_value + 1)
    )

    if not is_valid:
        return []

    # Генерація унікальних випадкових чисел
    unique_numbers = _rnd.sample(range(min_value, max_value + 1), quantity)

    # Сортування списку
    return sorted(unique_numbers)


# Приклад використання
print(get_numbers_ticket(1, 49, 6))  # Наприклад, поверне 6 унікальних випадкових чисел.