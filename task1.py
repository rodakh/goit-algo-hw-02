import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

def generate_request():
    # Генерує нову заявку з унікальним ідентифікатором і додає її до черги.
    request_id = random.randint(1000, 9999)  # Генерація унікального ідентифікатора заявки
    print(f"Генерується заявка з ідентифікатором {request_id}")
    request_queue.put(request_id)

def process_request():
    # Обробляє заявку, видаляючи її з черги.
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробляється заявка з ідентифікатором {request_id}")
    else:
        print("Черга пуста")

# Головний цикл програми
try:
    while True:
        generate_request()  # Створення нових заявок
        process_request()  # Обробка заявок
        time.sleep(1)  # Затримка для імітації часу обробки
except KeyboardInterrupt:
    print("Програма завершена користувачем")
