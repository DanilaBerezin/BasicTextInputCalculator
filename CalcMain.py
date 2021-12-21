from BasicCalculator import Calculator
from os import system, name

import os

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def main():
    pdir = os.path.dirname(__file__)
    helppath = os.path.join(pdir, 'README.txt')

    print("Welcome! Calculator running...")
    print("For help using the calculator type \"?\"\n")

    while True:
        
        user_input = input("Input: ")

        if user_input == "exit":
            clear()
            print("Exiting calculator...")
            return

        if user_input == "?":
            clear()
            
            print("To view the contents displayed here at any time, simply read the README in this program package\n")

            with open(helppath, 'r') as f:
                print(f.read())

            if(input("\nPRESS 'B' KEY AND PRESS ENTER TO GO BACK") == 'b'):
                clear()
                
                print("Welcome! Calculator running...")
                print("For help using the calculator type \"?\"\n")
                
                continue

        calc = Calculator()
        
        calc.setExpr(user_input)

        print("=", calc.calculate)

if __name__ == "__main__":
    main()


        

            
