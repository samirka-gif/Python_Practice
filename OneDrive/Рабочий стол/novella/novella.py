print("Добро пожаловать в игру Roblox!")
print("Тебе нужно пройти 4 уровня и выбраться из забытого мира.")
print("Удачи!")

# Информация об игроке
player = {
    "name": "",
    "coins": 0,
    "health": 100
}

# Предметы в игре
items = {
    "ключ": "Открывает ворота",
    "меч": "Помогает победить монстра",
    "кристалл": "Нужен для запуска сервера",
    "чип": "Последняя деталь для выхода"
}

# Коллекции игрока
inventory = []
completed_levels = set()
enemies = set()

# Названия уровней
levels = ("Лобби", "Лес", "Башня Obby", "Последний сервер")

print()
player["name"] = input("Введи имя своего персонажа: ")

print()
print("Привет,", player["name"])
print("Твоё приключение начинается!")

# УРОВЕНЬ 1

print()
print("УРОВЕНЬ 1:", levels[0])
print("Ты появился в заброшенном лобби.")
print("Перед тобой закрытые ворота.")
print("Рядом лежит старый ключ.")

print()
print("1 - Взять ключ")
print("2 - Пройти мимо")

choice = input("Твой выбор: ")

if choice == "1":
    inventory.append("ключ")
    print("Ты взял ключ!")
else:
    print("Ты прошёл мимо ключа.")

print()
print("Теперь нужно открыть ворота.")

if "ключ" in inventory:
    print("Ты использовал ключ и открыл ворота!")
    player["coins"] = player["coins"] + 10
    completed_levels.add("Лобби")
    print("Ты получил 10 монет.")
else:
    print("У тебя нет ключа.")
    print("Ты нашёл ключ возле ворот.")
    inventory.append("ключ")
    print("Ты открыл ворота.")
    completed_levels.add("Лобби")

print()
print("Инвентарь:", inventory)

# УРОВЕНЬ 2

print()
print("УРОВЕНЬ 2:", levels[1])
print("Ты попал в тёмный лес.")
print("В лесу живёт злой монстр.")
print("Чтобы пройти дальше, нужно найти меч.")

print()
print("1 - Искать меч")
print("2 - Спрятаться за деревом")

choice = input("Твой выбор: ")

if choice == "1":
    print("Ты нашёл меч!")
    inventory.append("меч")
else:
    print("Ты спрятался, но меч всё равно нужно найти.")
    print("Ты осмотрел дерево и нашёл меч.")
    inventory.append("меч")

print()
print("Перед тобой появился монстр!")
print("1 - Сразиться с монстром")
print("2 - Попробовать убежать")

choice = input("Твой выбор: ")

if choice == "1":
    if "меч" in inventory:
        print("Ты победил монстра!")
        enemies.add("Монстр")
        player["coins"] = player["coins"] + 20
        print("Ты получил 20 монет.")
    else:
        print("У тебя нет меча.")
        print("Ты смог убежать от монстра.")
else:
    print("Ты убежал от монстра.")
    print("Монстр не стал тебя преследовать.")

completed_levels.add("Лес")

print()
print("Твой инвентарь:", inventory)
print("Твои монеты:", player["coins"])

# УРОВЕНЬ 3

print()
print("УРОВЕНЬ 3:", levels[2])
print("Ты оказался возле высокой башни Obby.")
print("Чтобы подняться наверх, нужно пройти испытания.")

print()
print("Первое испытание!")
print("Что нужно сделать, чтобы перепрыгнуть препятствие?")
print("1 - Прыжок")
print("2 - Приседание")
print("3 - Бег")

answer = input("Твой ответ: ")

if answer == "1":
    print("Правильно! Ты прошёл первое испытание.")
    player["coins"] = player["coins"] + 10
else:
    print("Неправильно, но тебе дают ещё одну попытку.")
    answer = input("Попробуй ещё раз. Введи 1: ")

    if answer == "1":
        print("Теперь правильно!")
    else:
        print("Ты не прошёл испытание, но тебя пропускают дальше.")

print()
print("Второе испытание!")
print("Разгадай загадку 'Назови ее по имени и она исчезнет'")

answer = input("Твой ответ: ")

if answer == "тишина":
    print("Правильно! Ты прошёл испытание.")
    inventory.append("кристалл")
    print("Ты получил кристалл.")
else:
    print("Ответ неправильный.")
    print("Попробуй ещё раз.")
    answer = input("Введи ответ: ")

    if answer == "тишина":
        print("Правильно!")
        inventory.append("кристалл")
    else:
        print("Ты не получил кристалл.")
        print("Но нашёл его возле башни.")
        inventory.append("кристалл")

completed_levels.add("Башня Obby")

print()
print("Ты прошёл башню!")
print("Твой инвентарь:", inventory)

# УРОВЕНЬ 4

print()
print("УРОВЕНЬ 4:", levels[3])
print("Ты добрался до последнего сервера.")
print("Чтобы выбраться из игры, нужно запустить сервер.")
print("Для этого нужны три предмета:")
print("Ключ, кристалл и чип.")

print()
print("Ты осматриваешь комнату.")
print("На столе лежит чип.")

print("1 - Взять чип")
print("2 - Не брать чип")

choice = input("Твой выбор: ")

if choice == "1":
    inventory.append("чип")
    print("Ты взял чип!")
else:
    print("Ты решил не брать чип.")
    print("Но без него нельзя запустить сервер.")
    print("Ты вернулся за ним.")
    inventory.append("чип")

print()
print("Проверка предметов...")

if "ключ" in inventory:
    print("Ключ найден!")
else:
    print("Ключ не найден.")

if "кристалл" in inventory:
    print("Кристалл найден!")
else:
    print("Кристалл не найден.")

if "чип" in inventory:
    print("Чип найден!")
else:
    print("Чип не найден.")

print()

if "ключ" in inventory and "кристалл" in inventory and "чип" in inventory:
    print("Все предметы собраны!")
    print("Ты вставил детали в сервер.")
    print("Сервер успешно запущен!")
    print("Ты выбрался из забытого мира Roblox!")
    completed_levels.add("Последний сервер")
    player["coins"] = player["coins"] + 30
else:
    print("Не хватает предметов.")
    print("Ты не смог запустить сервер.")

# КОНЕЦ ИГРЫ

print()
print("ИГРА ЗАВЕРШЕНА!")
print("Имя игрока:", player["name"])
print("Количество монет:", player["coins"])
print("Здоровье:", player["health"])

print()
print("Пройденные уровни:")
print(completed_levels)

print()
print("Побежденные враги:")
print(enemies)

print()
print("Твой инвентарь:")
print(inventory)

print()
print("Спасибо за игру!")