import main

assert multiply_binary('10', '1010') == '10100'
assert multiply_binary('1001', '100') == '100100'
assert multiply_binary('1010', '101') == '110010'
assert multiply_binary('1000', '111') == '111000'
assert multiply_binary('100', '100') == '10000'
assert multiply_binary('111', '100') == '11100'
assert multiply_binary('1000', '1000') == '1000000'
