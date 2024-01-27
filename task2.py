from collections import deque


def is_palindrome(s):
    # Підготовка рядка: перетворення у нижній регістр і видалення пробілів
    formatted_str = ''.join(ch.lower() for ch in s if ch.isalnum())

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(formatted_str)

    while len(char_deque) > 1:
        # Порівняння і видалення символів з обох кінців черги
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


# Приклади використання функції
print(is_palindrome("А роза упала на лапу Азора"))  # Приклад паліндрому
print(is_palindrome("Привіт, світ!"))  # Не паліндром
