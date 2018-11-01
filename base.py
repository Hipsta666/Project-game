from random import *
from termcolor import *

question = "да"
while question == "да":
    empty_letters = list("АЕНОСТ")
    refresh = shuffle(empty_letters)
    collection = ''.join(empty_letters)

    # So the same letters do not fall out
    num_1 = num_2 = None
    while num_1 == num_2:
        num_1 = randint(0, 5)
        num_2 = randint(0, 4)

    # Drop two random letters
    word_letters = collection.replace(collection[num_1], "")
    new_word = word_letters.replace(word_letters[num_2], "")
    print("Отгадай слово из четырёх букв(А, Е, Н, О, С, Т)!")

    # Counting attempts and the number of correct letters
    letters_place = None
    i = 0
    while letters_place != 4 and i != 10:
        i += 1
        letters_place = 0
        print("Попытка №{}:".format(i), sep="", end="")
        my_word = input()

        # Create the ability to write in small letters
        if len(new_word) == len(my_word):
            for g in range(len(my_word)):
                if my_word[g].upper() == new_word[g]:
                    letters_place += 1
            print('На "своём месте":', letters_place)
            print('Не на "своём месте":', 4 - letters_place)

            if letters_place == 4:
                print("Правильно! Вы выиграли!\n")
            if i == 10:
                print("Извините, но вы проиграли.")
                print("Было загадано слово {}.\n".format(new_word))

        if len(my_word) < len(new_word):
            print("Не может быть загадано такое короткое слово.")
        if len(my_word) > len(new_word):
            print("Не может быть загадано такое длинное слово.")

    # If the user enters the wrong answer
    question = input("Хотите сыграть ещё раз?(да/нет)\n")
    while question != "нет" and question != "да":
        question = input("Хотите сыграть ещё раз?({}/{})\n".format(
            colored("да", "blue"), colored("нет", "red")))
        if question == "нет":
            print("Спасибо за игру!")
