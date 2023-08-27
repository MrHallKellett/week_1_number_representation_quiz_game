import main

from random import randint


def test_convert_dec_to_bin():

    assert convert_dec_to_bin(0) = "0"
    assert convert_dec_to_bin(1) = "1"
    assert convert_dec_to_bin(512) = bin(512)[2:]
    assert convert_dec_to_bin(53242) = bin(53242)[2:]
    assert convert_dec_to_bin(94546333) = bin(94546333)[2:]


def test_convert_bin_to_dec():

    for _ in range(10):

        num = randint(1, 1000)

        assert convert_bin_to_dec(bin(num)[2:]) = num

def test_convert_dec_to_hex():

    for _ in range(10):

        num = randint(1, 1000)

        assert convert_dec_to_hex(num) = hex(num)[2:].upper()


def test_convert_hex_to_dec():
    for _ in range(10):

        num = randint(1, 1000)

        assert convert_hex_to_dec(hex(num)[2:].upper()) = num


def test_convert_bin_to_hex():
    assert convert_bin_to_hex("1") = "1""
    assert convert_bin_to_hex("1011") = "B"
    assert convert_bin_to_hex("100001000") = "108"
    assert convert_bin_to_hex("10101110111") = hex(int("10101110111", 2))[2:].upper()
    assert convert_bin_to_hex("01010101110000001111000") = hex(int("01010101110000001111000", 2))[2:].upper()
