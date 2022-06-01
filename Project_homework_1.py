import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

menu = {"наполеон": [["масло", "яйца", "коржи", "сахар"], 5, 600],
        "медовик": [["масло", "мука", "мёд"], 3, 730],
        "киевский": [["сахар", "мука", "какао", "фундук"], 8, 950]}

engine.say(f"Добро пожаловать в нашу кондитескую! Сегодня в меню у нас имеются седующие торты: {', '.join(menu.keys())};")
engine.runAndWait()

print("Добро пожаловать в нашу кондитескую!",
      f"\nСегодня в меню у нас имеются седующие торты: {', '.join(menu.keys())};",
      "\n(Для выхода из приложения введите: \"exit\")")

while True:
    engine.say("\nКакой торт Вас интересует?")
    engine.runAndWait()
    user_choice = input("\nКакой торт Вас интересует?: ").lower()
    if user_choice in menu:
        engine.say("\nЧто Вы хотели бы уточнить? Введите один из предложенных вариантов.")
        engine.runAndWait()
        print("\"Описание торта\" (введите цифру: 1), \"Цену торта\" (Введите цифру: 2), \"Вес торта в наличии\" (введите цифру: 3),",
        "\n\"Вернуться к выбору торта\" (введите цифру: 4), \"Купить торт\" (введите цифру: 5).",
        "\n(Для выхода из приложения введите: \"exit\")")

        while True:
            engine.say("\nЧто Вы хотели бы уточнить?")
            engine.runAndWait()
            scroll = input("\nЧто Вы хотели бы уточнить?: ").lower()
            if scroll == "1":
                print(f"Состав торта \"{user_choice}\": {', '.join(menu[user_choice][0])};")
                continue
            elif scroll == "2":
                print(f"Торт \"{user_choice}\" стоит {menu[user_choice][1]} рублей.")
                continue
            elif scroll == "3":
                print(f"Торта \"{user_choice}\" осталось {menu[user_choice][-1]} грамм.")
                continue
            elif scroll == "4":
                break

            elif scroll == "5":
                while True:
                    try:
                        heft = int(input("Сколько грамм торта Вам положить: "))
                    except ValueError:
                        print("\nВы ввели неверное значение! Вводите только числа!")
                        continue
                    if heft <= menu[user_choice][-1] and heft > 0:
                        print(f"К оплате {menu[user_choice][1] * heft / 100} рублей.")
                        print(f"торта {user_choice} осталось: {menu[user_choice][-1] - heft} грамм.")
                    elif heft <= 0 or heft > menu[user_choice][-1]:
                        print("Извините, мы не можем взвесить Вам такое количество! ")
                        break

                    solution = input("\nЖелаете что-то ещё? (да/нет): ").lower()
                    if solution == "да":
                        break
                    else:
                        engine.say("Досвидания! Возвращайтесь к нам ещё!")
                        engine.runAndWait()
                        print("\nДосвидания! Возвращайтесь к нам ещё!")
                        exit()

            elif scroll == "exit":
                engine.say("Досвидания! Возвращайтесь к нам ещё!")
                engine.runAndWait()
                print("Досвидания! Возвращайтесь к нам ещё!")
                exit()
            else:
                print("Извините, мы не можем это вам подсказать! Пожалйста, повторите выбор!")
                continue

    elif user_choice == "exit":
        engine.say("Досвидания! Возвращайтесь к нам ещё!")
        engine.runAndWait()
        print("Досвидания! Возвращайтесь к нам ещё!")
        exit()
    else:
        engine.say("Извините, такого торта нет! Пожалйста, повторите выбор!")
        engine.runAndWait()
        print("Извините, такого торта нет! Пожалйста, повторите выбор!")
        continue