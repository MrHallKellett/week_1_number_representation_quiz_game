import main

assert convert_bin_to_hex("1") == "1""
assert convert_bin_to_hex("1011") == "B"
assert convert_bin_to_hex("100001000") == "108"
assert convert_bin_to_hex("10101110111") == hex(int("10101110111", 2))[2:].upper()
assert convert_bin_to_hex("01010101110000001111000") == hex(int("01010101110000001111000", 2))[2:].upper()
