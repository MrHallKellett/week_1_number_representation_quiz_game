
import main

assert convert_dec_to_bin_2s_mode(5, True) = "0101"
assert convert_dec_to_bin_2s_mode(-55, True) = "1001001"
assert convert_dec_to_bin_2s_mode(-5555, True) = "10101001001101" # check this later
assert convert_dec_to_bin_2s_mode(555, True) = "0" + bin(555)[2:]
assert convert_dec_to_bin_2s_mode(-12, True) = "10100" 
