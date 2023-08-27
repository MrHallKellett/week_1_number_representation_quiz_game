# Week 1: Number Representation Quiz Game

Practical programming tasks for Week 1 (2023-25) of the A Level CS course at Kellett School.

## SECTION A - functions

---

Note: some built-in functions exist in Python that will make this task too easy. You are not allowed to use these in this assignment:
	
	bin(x)	
	hex(x)	
	int(x, 2)	
	int(x, 16)	


Instead you should be focusing on an algorithmic approach to solving the problems - decomposing the methods you use on paper / on your calculator into control structures, e.g. iteration and conditional statements.

All code should be written in a consistent format that adheres to the naming conventions laid out in Python's PEP8 guidelines:  [https://gist.github.com/bourque/5004594018c9bf16a821410f5c9327a7](https://gist.github.com/bourque/5004594018c9bf16a821410f5c9327a7) 

### TODO

_solve each problem and pass the built-in tests_

---

#### Task 1

Program a function named `convert_dec_to_bin()` that takes a decimal number (int) as a parameter and converts it into binary.
	
	> convert_dec_to_bin(17)
	"10001"
	
---


#### Task 2

Program a function named `convert_bin_to_dec()` that takes a binary number (string) as a parameter and converts it into decimal.
	
	> convert_bin_to_dec("000100")
	
---



#### Task 3

Program a function named `convert_dec_to_hex()` that takes a decimal number (int) as a parameter and converts it into hexadecimal.
	
	> convert_dec_to_hex(160)
	"A0"
	
---




#### Task 4

Program a function named `convert_hex_to_dec()` that takes a hexadecimal number (string) as a parameter and converts it into decimal.
	
	> convert_hex_to_dec("A7")
	167
	
---



#### Task 5

Program a function named `convert_bin_to_hex()` that takes a binary number (string) as a parameter and converts it into hexadecimal.
	
	> convert_bin_to_hex("111011111")
	"1DF"
	
---


#### Task 6

Program a function named `convert_hex_to_bin()` that takes a hexadecimal number (string) as a parameter and converts it into binary.
	
	> convert_bin_to_hex("FF")
	"11111111"
	
---

#### Task 7

Extend your `convert_dec_to_bin()` and `convert_bin_to_dec()` functions to allow them to convert negative binary numbers, using the two's complement system.

You should add a second parameter to each function's header - `signed` (boolean).

If the `signed` parameter is set to `True`, the function will convert using the two's complement system. If the parameter is `False`, the function will convert using the standard binary system.
	
	> convert_bin_to_dec("1001", True)
	-7
	> convert_bin_to_dec("1000", False)
	8
---




#### Task 8

Program a function named `convert_asc_to_string()` that takes a list of decimal numbers (list) as a parameter and converts it into a word using ASCII.

You can use the built-in functions `ord()` and `chr()` for this task.
	
	> convert_asc_to_string([65, 66, 67, 68])
	"ABCD"
	
---



#### Task 9

Program a function named `convert_string_to_asc()` that takes a string as a parameter and converts it into a string of its corresponding ASCII binary codes (each code should be 7 bits).
	
	> convert_chr_to_asc("Hello")
	'10010001100101110110011011001101111'
	
---


#### Task 10

Implement data validation in your functions so that they reject numbers that are not acceptable  (at this stage - printing a message is fine). E.g:
	
	convert_bin_to_dec("123456")
	ERROR!
	I can't convert 123456 - not a binary number.
	
---

#### Task 11

Program a generalised function named `convert_number_base()` that takes accepts three parameters: `number_to_convert`, `start_base,` `end_base`. The function should convert the number given from the given starting base to the given ending base. The minimum base that can be converted is base-2 (binary) and the maximum base is base-10 (decimal).
	
	convert_number_base("1212", 3, 7)
	160
	
In the example above, the starting number base is ternary (base-3), and the final number base is septal (base-7).

The ternary number 1212 is equal to 50 in decimal. This is because:
	
	2 x 30 = 2
	1 x 31 = 3
	2 x 32 = 18
	1 x 33 = 27
	2 + 3 + 18 + 27 = 50
	
The decimal number 140 is equal to the septal number 260. This is because:
	
	0 x 70 = 0
	6 x 71 = 42
	2 x 72 = 98
	0 + 42 + 98 = 140.
	
This web link should help you to understand positional number bases:

 [https://www.cs.cas.cz/portal/AlgoMath/NumberTheory/Arithmetics/NumeralSystems/PositionalNumeralSystems/PositionalNumeralSystems.htm#:~:text=Subject%20Index-,Positional%20Numeral%20Systems,set%20of%20symbols%20is%20used.](https://www.cs.cas.cz/portal/AlgoMath/NumberTheory/Arithmetics/NumeralSystems/PositionalNumeralSystems/PositionalNumeralSystems.htm#:~:text=Subject%20Index-,Positional%20Numeral%20Systems,set%20of%20symbols%20is%20used.) 

---

### SECTION B

---

Program a number representation quiz in Python that has the following features:

1\. Asks randomly generated questions until the user gets 10 answers correct.

2\. Picks a question format from the following options:

- Convert the decimal number 45 to binary.

- Convert the binary number 101101 to decimal.

- Convert the decimal number 99 to hexadecimal.

- Convert the hexadecimal number 63 to decimal.

- Convert the hexadecimal number 63 to binary.

- Convert the binary number 101101 to hexadecimal.

- Convert the decimal value 45 into its corresponding Unicode character.

- Convert the Unicode character '-' into its corresponding decimal value.

- Convert the decimal number -45 into a Two's Complement binary number.

- Convert the two's complement binary number 1010011 into a decimal number.


3\. Gets the user's answer; checks if it is correct; awards a point if so, deducts a point if not.

4\. Displays appropriate feedback to the user.

5\. Each action contained inside the program should be created as a user-defined function and called when needed. _Use your functions from Section A!_

6\. At the end of the quiz, ask for the user's name. Record the following details to an external file:

- longest winning streak (the number of correct answers in a row)

- time taken to complete the quiz

7\. At a menu to the start of the game with the options a) play quiz and b) view stats.

8\. If view stats is chosen, provide the following functionality:

- Best Time - TOP 10 LEADERBOARD

- Longest Winning Streak - TOP 10 LEADERBOARD

- View User Stats - average time / average winning streak length

---
