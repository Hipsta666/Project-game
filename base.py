from random import *

qws = None
while qws != "нет":
    empty_letters = list("АЕНОСТ")
    refresh = shuffle(empty_letters)
    b = ''.join(empty_letters)
    num_1 = num_2 = None

    while num_1 == num_2:
        num_1 = randint(0, 5)
        num_2 = randint(0, 4)

    # drop two random letters
    word_m_sing = b.replace(b[num_1], "")
    new_word = word_m_sing.replace(word_m_sing[num_2], "")

    print(new_word, num_1, num_2)
    print("Отгадай слово из четырёх букв!")

    my_word = None
    c = None
    qws = None
    i = 0

    while c != 4 and i != 10:
        i += 1
        c = 0
        print("Попытка №", i, ":", sep="", end="")
        my_word = input()

        for g in range(len(my_word)):
            if my_word[g].upper() == new_word[g]:
                c += 1
        print('На "своём месте":', c)
        print('Не на "своём месте":', 4 - c)

        if c == 4:
            print("Правильно! Вы выиграли!")
        if i == 10:
            print("Извините, но вы проиграли.\n")

    qws = input("Хотите сыграть ещё раз?(да/нет)")
    if qws == "нет":
        print("Спасибо за игру!")
