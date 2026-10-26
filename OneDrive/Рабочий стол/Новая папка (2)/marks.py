marks = {
    "Аня": 5,
    "Ира": 4,
    "Миша": 3
}
print(marks["Ира"])

marks["Оля"] = 5
marks["Ира"] = 5
del marks["Миша"]

print(marks)

name = input("Введите имя: ")

if name in marks:
    print(marks[name])
else:
    print("Нет такого ключа")

print(marks.keys())
print(marks.values())
print(len(marks))

prices = {
    "Хлеб": 50,
    "Молоко": 90,
    "Сыр": 250
}
for name in prices:
    print(name, prices[name])


prices1 = {
    "Хлеб": 50,
    "Молоко": 90,
    "Сыр": 250
}
total = 0
max_price1 = 0
max_name = ""
for name in prices1:
    total += prices1[name]
    if prices1[name] > max_price1:
        max_price1 = prices1[name]
        max_name1 = name
print("Сумма цен:", total)
print("Самый дорогой товар:", max_name1)


text = "мама"
counts = {}
for char in text:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1
print(counts)


text = "кот пёс кот дом кот пёс"
words = text.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
max_word = ""
max_count = 0
for word in counts:
    if counts[word] > max_count:
        max_count = counts[word]
        max_word = word
print("Самое частое слово:", max_word)
print("Количество:", max_count)


data = {
    "Аня": 5,
    "Ира": 4,
    "Миша": 3
}
new_data = {}
for key in data:
    value = data[key]
    new_data[value] = key
print(new_data)
countries = ["Россия", "Франция", "Япония"]
capitals = ["Москва", "Париж", "Токио"]
data = {}
for i in range(len(countries)):
    data[countries[i]] = capitals[i]
country = input("Введите страну: ")
if country in data:
    print("Столица:", data[country])
else:
    print("Нет такой страны")