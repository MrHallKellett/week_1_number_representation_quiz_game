import main

from random import randint

for _ in range(10):

    num = randint(1, 1000)

    assert convert_hex_to_dec(hex(num)[2:].upper()) == num
