class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

# Создаем несколько объектов класса Store
store1 = Store("Магазин №1", "ул. Ленина, 1")
store2 = Store("Магазин №2", "ул. Пушкина, 2")
store3 = Store("Магазин №3", "ул. Горького, 3")
store4 = Store("Магазин №4", "ул. Чехова, 4")

# Добавляем товары в каждый магазин
store1.add_item('яблоки', 150)
store1.add_item('бананы', 99)

store2.add_item('груши', 200)
store2.add_item('апельсины', 120)

store3.add_item('виноград', 300)
store3.add_item('манго', 400)

store4.add_item('ананасы', 250)
store4.add_item('киви', 180)

# Тестируем методы на магазине store1
print("\nТестирование методов на магазине store1:")

# Добавляем новый товар
store1.add_item('персики', 180)

# Обновляем цену товара
store1.update_price('бананы', 120)

# Удаляем товар
store1.remove_item('яблоки')

# Запрашиваем цену
print(f"Цена на 'бананы': {store1.get_price('бананы')}")
print(f"Цена на 'яблоки': {store1.get_price('яблоки')}")  # Должно вернуть None, так как товар был удален

# Выводим итоговый ассортимент магазина store1 для проверки
print(f"\nИтоговый ассортимент магазина {store1.name}: {store1.items}")
