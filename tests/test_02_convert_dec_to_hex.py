import main

from random import randint

for _ in range(10):

    num = randint(1, 1000)

    assert convert_dec_to_hex(num) == hex(num)[2:].upper()
