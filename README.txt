INTRODUCTION:
================================================================

This program is based on an assignment I completed as homework during my CMPSCI 132 course at Penn State. I have refractored it to make it more readable and more efficient.

It is a basic calculator that takes an arithmetic expression as an input string and returns the numerical equivalent of the expression as a standard calculator would. 

The calculator can perform addition, subtraction, multiplication, division, and exponentiation in any order and supports the use of parenthesis to change operation precedence.

RUNNING THE PROGRAM:
================================================================

Note: As of the latest update, the program works only with python 3.9.2.

To run the program, simply open up your terminal, traverse to the directory the program was installed, and type in:

	python CalcMain.py


To run doctests on individual python programs in the package, type in:

	python -m doctest -v *program*.py 
		(exclude the star '*' characters)

When the program first runs, it will display a welcome message and directions for displaying documentation. Afterwords, the calculator will begin to take input as denoted by "Input: " being displayed on the lower left corner. 

THE CALCULATOR:
================================================================

The calculator takes two types of inputs: calls to command line UI, and arithmetic expressions. 

Calls to the UI include calls to display help documentation, to navigate, and to quit the program. 

To display help documentation simply type in "?" and press enter. To get back to the calculator, press "b".

To quit the program type in "exit" and press enter.

The calculator also evaluates infix arithmetic expressions and returns their equivalent numerical value to 13 decimal places. 

The calculator correctly evaluates only valid, infix arithmetic expressions. This means that the input expression must follow all the conventions of infix notation. Any expressions which violate the following rules will not be evaluated by the calculator:
	1) Every open parenthesis '(' must have a matching closed parenthesis ')' that succeeds it.
	2) Every closed parenthesis must have a matching open parenthesis that preceeds it.
	3) The operands in the arithmetic expressions must be expressed either as integers (e.g 5) or as floating point numbers (e.g 5.0).
	4) An operator must not directly preceed a closed parenthesis ( e.g. "*)" ).
	5) An operator must not directly succeed an open parenthesis, ( e.g. "(*" ).
	6) There cannot be any consecutive operators
	7) There cannot be a number preceeding an open parenthesis
	8) There cannot be a number succeeding a closed parenthesis

Note: as you can see the calculator does not support implicit multiplication. 

To evaluate a legitimate, infix arithmetic expression, simply type in the expression while in the calculator and press enter. The result will be displayed on the next line underneath the expression entry.
