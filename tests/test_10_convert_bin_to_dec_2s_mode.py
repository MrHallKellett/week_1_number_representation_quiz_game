import main

assert convert_bin_to_dec_2s_mode("111", True) == -1
assert convert_bin_to_dec_2s_mode("1101", True) == -3
assert convert_bin_to_dec_2s_mode("11100", True) == -4
assert convert_bin_to_dec_2s_mode("0110001", True) == 97
assert convert_bin_to_dec_2s_mode("1110101110", True) == -82
