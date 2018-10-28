from random import *

empty_letters = list("АЕНОСТ")
refresh = shuffle(empty_letters)
b = ''.join(empty_letters)
num_1 = num_2 = None

while num_1 == num_2:
    num_1 = randint(0, 5)
    num_2 = randint(0, 4)

# drop two random letters
word_m_sign = b.replace(b[num_1], "")
new_word = f.replace(f[num_2], "")

print(q, num_1, num_2)
