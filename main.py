# Задача 1
message = "Привіт"
print(message)

message = "Як справи?"
print(message)
# Задача 2
name = "Олег"
print("Привіт, "+name+", як справи?")
# Задача 3
famous_person = "Альберт Ейнштейн"
message = famous_person+ ' одного разу сказав "Прагніть не до успіху, а до цінностей, які він дає."'
print(message)
# Задача 4
username1 = "---Олег---"
print(username1.strip('-'))
print(username1.lstrip('-'))
print(username1.rstrip('-'))
# Задача 5
print('Олег Нікулеску\nУкраїна\n58000\nЧернівці')
# Задача 6
meters = float(input("Введіть відстань в метрах: "))
inches = meters * 39.37
feet = meters * 3.281
yards = meters * 1.094
miles = meters / 1609
print("Відстань в метрах: {}".format(meters))
print("Відстань в дюймах: {:.2f}".format(inches))
print("Відстань в футах: {:.2f}".format(feet))
print("Відстань в ярдах: {:.2f}".format(yards))
print("Відстань в милях: {:.2f}".format(miles))
# Задача 7
days = float(input("Кількість днів: "))
total_hours = days * 24
total_minutes = total_hours * 60
total_seconds = total_minutes * 60
print('{:<10} {:<10}'.format('Години', 'Хвилини'))
print('{:<10} {:<10}'.format(total_hours, total_minutes))
print('{:<10} {:<10}'.format('Секунди', ''))
print('{:<10} {:<10}'.format(total_seconds, ''))
# Задача 8
C = float(input("Введіть температуру у градусах Цельсія: "))

F = 32 + 9/5 * C
K = C + 273.15

print("{:^15}".format("Температура"))
print("{:^15}".format("у град. Фаренгейтах (F)"))
print("{:^15}".format("у град. Кельвінах (K)"))
print("-" * 15)
print("{:^15.2f}".format(F))
print("{:^15.2f}".format(K))
# Задача 9
num = float(input("Чотирицифрове число: "))
thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
ones = num % 10
sum_digits = thousands + hundreds + tens + ones
print("{0} + {1} + {2} + {3} = {4}".format(thousands, hundreds, tens, ones, sum_digits))
# Задача 10
import math
# координати Пекіна
x1 = 39.9075000
y1 = 116.3972300

# координати Києва
x2 = 50.4546600
y2 = 30.5238000

x1_rad = math.radians(x1)
y1_rad = math.radians(y1)
x2_rad = math.radians(x2)
y2_rad = math.radians(y2)

distance = 6371.032 * math.acos(math.sin(x1_rad) * math.sin(x2_rad) +
                                math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad - y2_rad))

print(f"Відстань між Пекіном та Києвом: {distance:.3f} км".rjust(10))




