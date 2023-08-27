import main

assert convert_number_base("2201", 3, 10) = int("2201", 3)
assert convert_number_base("707532", 8, 2) = bin(int("707532", 8))[2:]
assert convert_number_base("404044404", 5, 16) = hex(int("404044404", 5))[2:].upper()
assert convert_number_base("GJI1031AAA", 30, 10) = int("GJI1031AAA", 30)

