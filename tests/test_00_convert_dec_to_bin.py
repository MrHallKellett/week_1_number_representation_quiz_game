import main

assert convert_dec_to_bin(0) == "0"
assert convert_dec_to_bin(1) == "1"
assert convert_dec_to_bin(512) == bin(512)[2:]
assert convert_dec_to_bin(53242) == bin(53242)[2:]
assert convert_dec_to_bin(94546333) == bin(94546333)[2:]
