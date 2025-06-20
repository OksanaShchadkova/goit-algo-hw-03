import re
def normalize_phone(phone_number: str) -> str | None:
    """
    Нормалізує телефон до міжнародного формату.

    Параметри:
    phone_number : str  
        Рядок з телефонним номером у різноманітних форматах.

    Повертає:
        Нормалізований телефонний номер у вигляді рядка або None, якщо номер не містить цифр.
    """
    # Перевірка на None або пустий рядок  
    if not phone_number:
        return None

    # Видаляємо все символи, крім цифр та '+'
    digits = re.sub(r"[^\d+]", "", phone_number.strip())
    
    # Якщо номер не містить жодних цифр  
    if not re.search(r"\d", digits):
        return None

    # Нормалізація номера  
    if digits.startswith('+'):
        return digits  # Якщо номер вже починається з '+', повертаємо його  
    elif digits.startswith('380'):
        return f"+{digits}"  # Додаємо '+' до номера, що починається з '380'
    else:
        return f"+38{digits}"  # Додаємо '+38' до номера, що не має міжнародного коду

# Приклади використання:
print(normalize_phone("    +38(050)123-32-34"))  # +380501233234  
print(normalize_phone("     0503451234"))         # +380503451234  
print(normalize_phone("(050)8889900"))            # +380508889900  
print(normalize_phone("38050-111-22-22"))         # +380501112222  
print(normalize_phone("38050 111 22 11   "))      # +380501112211  
print(normalize_phone("invalid-number"))           # None  
print(normalize_phone(None))                        # None