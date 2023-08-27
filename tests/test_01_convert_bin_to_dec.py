import main

from random import randint

for _ in range(10):

    num = randint(1, 1000)

    assert convert_bin_to_dec(bin(num)[2:]) = num
