from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    """
    Повертає різницю у днях між *date* і сьогоднішньою датою.

    Parameters
    ----------
    date : str
        Рядок у форматі 'YYYY-MM-DD'.

    Returns
    -------
    int | None
        Позитивне число, якщо дата у минулому,
        від’ємне — якщо у майбутньому,
        0 — якщо сьогодні,
        None — якщо формат некоректний.
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = (target_date - today).days  # Різниця у днях
        return delta
    except ValueError:
        return None  # Повертаємо None у випадку некоректного формату

# Перевірка коду
print(get_days_from_today("2025-06-20"))
print(get_days_from_today("2025-06-30"))
print(get_days_from_today("invalid-date"))  # Поверне None
