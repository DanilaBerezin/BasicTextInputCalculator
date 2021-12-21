from Stack import Stack

class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str) and len(new_expr.strip())>0:
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None
        
    def isNumber(self, txt):
        if not isinstance(txt,str) or len(txt)==0:
            print("stripped text : ", txt.strip())
            print("Argument error in isNumber")
            return False
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except ValueError:
            return False

    def _getPostfix(self, txt):
        '''   
            Required: _getPostfix must create and use a Stack for expression processing. Follow PEMDAS
            >>> x=Calculator()
            >>> x._getPostfix(' 2 ^        4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1*5+3^2+1+4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('(2.5)')
            '2.5'
            >>> x._getPostfix ('((2))')
            '2.0'
            >>> x._getPostfix ('     2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
            '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 *    5   +   3    ^ -2       +1  +4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')
            >>> x._getPostfix('2*(5 +3)^ 2+)1  +4(    ')
        '''
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in _getPostfix")
            return None

        postfix_Stack=Stack()
        # YOUR CODE STARTS HERE
        
        operators = ["-", "+", "/", "*", "^"]
        parenthesis = ["(", ")"]

        #Evaluations if a character is a parenthesis
        def isParen(c):
            for p in parenthesis:
                if c == p:
                    return True
            return False

        #Evaluates if a character is an arithmetic operator
        def isOp(c):
            for op in operators:
                if c == op:
                    return True
            return False

        #Defines the precedence of an arithmetic operator
        def precedence(c):
            if c == "^":
                return 2
            if c == "/" or c == "*":
                return 1
            if c == "+" or c == "-":
                return 0
            return None

        #Determines if the input is a valid, infix, arithmetic expression
        def isValid(text):    
            openCount = 0  
            for i in range(len(text)):
                if not text[i].isnumeric and text[i] != "." and not isOp(text[i]) and text[i] != " " and not isParen(text[i]):  #Returns false if there is an invalid character in the expression
                    return False
                if isOp(text[i]) and (i == len(text)-1 or i == 0):  #Returns false if there is an arithmetic operator at the beginning or end of the string
                    return False
                if text[i] == ")" and openCount == 0:  #Returns false if there is a hanging closing parenthesis
                    return False
                if text[i] == "(":
                    openCount +=1
                elif text[i] == ")":
                    openCount -= 1
            if openCount != 0:  #Returns False if there are any asymmetrical set of parenthesis
                return False

            #Splits the input string between operators
            nums = []
            beg = 0
            for i in range(len(text)):
                if isOp(text[i]) or isParen(text[i]):
                    if len(text[beg:i].strip()) != 0:  #Skips all strings which are empty or whitespace
                        nums.append(text[beg:i])
                    beg = i+1
            if len(nums) == 0:
                nums.append(text)

            #If any string between two operators cannot be evaluated as a number, returns false
            for n in nums:
                n = n.strip()
                for c in n:
                    if not self.isNumber(c) and c != ".":
                        return False

            txt = "".join(text.split())
            for i in range(len(txt)):
                if isOp(txt[i]) and isOp(txt[i+1]):  #Returns false if there are any two consecutive operators
                    return False  
                if txt[i] == "(":
                    if isOp(txt[i+1]):  #Returns false if there is an operator preceeding an open parenthesis
                        return False
                    if i == 0:  #Avoids an error in the next line as txt[-1] does not exist
                        continue
                    if self.isNumber(txt[i-1]):  #Returns false if there is a number preceeding an open parenthesis
                        return False
                elif txt[i] == ")":
                    if isOp(txt[i-1]):  #Returns false if there is an operator preceeding a closing parenthesis
                        return False
                    if i == len(txt)-1:  #Avoids an error in the next line as txt[len(txt)] does not exist
                        continue
                    if self.isNumber(txt[i+1]):  #Returns false if there is a number succeeding a closing parenthesis
                        return False

            return True
                
        if not isValid(txt):
            return None

        #Removes whitespace from input after verifying expression
        text = "".join(txt.split())  

        #Initializing global variables
        stack = Stack()
        inp = []
        outp = ""

        #Splitting the input string into operators, parenthesis, and numbers all in order of input so that they can be scanned easily
        beg = 0
        for i in range(len(text)):
            if isOp(text[i]) or isParen(text[i]):
                if i == 0:
                    inp.append(text[i])
                    if len(text[beg:i]) != 0:
                        inp.append(text[beg:i])
                else:
                    if len(text[beg:i]) != 0:
                        inp.append(text[beg:i])
                    inp.append(text[i])
                beg = i+1
	
        if(len(text[beg:len(text)]) != 0):      #To make sure that a null character isn't appended to the list
            inp.append(text[beg:len(text)])

        #Scanning the input and returning a postfix expression for it
        for i in range(len(inp)):
            scanned = inp[i]
            if self.isNumber(scanned):  #Keep in mind this will always print "Error in isNumber" if the scanned element isn't a number
                scanned = str(float(scanned))
                scanned += " "
                outp += scanned
            elif stack.isEmpty():
                stack.push(scanned)
            elif scanned == "(":
                stack.push(scanned)
            elif isOp(scanned):
                if isParen(stack.peek()) or precedence(scanned) > precedence(stack.peek()):
                    stack.push(scanned)
                else:
                    while not stack.isEmpty() and not isParen(stack.peek()) and precedence(scanned) <= precedence(stack.peek()):
                        outp += stack.pop() + " "
                    stack.push(scanned)
            elif scanned == ")":
                while stack.peek() != "(":
                    outp += stack.pop() + " "
                stack.pop()
        while not stack.isEmpty():
            outp += stack.pop() + " "
        outp = outp.strip()
        return outp
                
    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('    4  +      3 -2')
            >>> x.calculate
            5.0
            >>> x.setExpr('  2  +3.5')
            >>> x.calculate
            5.5
            >>> x.setExpr('4+3.65-2 /2')
            >>> x.calculate
            6.65
            >>> x.setExpr(' 23 / 12 - 223 +      5.25 * 4    *      3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('   2   - 3         *4')
            >>> x.calculate
            -10.0
            >>> x.setExpr(' 3 *   (        ( (10 - 2*3)))')
            >>> x.calculate
            12.0
            >>> x.setExpr(' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr(' 2   *  ( 4 + 2 *   (5-3^2)+1)+4')
            >>> x.calculate
            -2.0
            >>> x.setExpr('2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr("4++ 3 +2") 
            >>> x.calculate
            >>> x.setExpr("4    3 +2")
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*(2 - 3*2)) ')
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*/(2 - 3*2) ')
            >>> x.calculate
            >>> x.setExpr(')2(*10 - 3*(2 - 3*2) ')
            >>> x.calculate
        '''
        if not isinstance(self.__expr,str) or len(self.__expr.strip())==0:
            print("Argument error in calculate")
            return None

        calculator_Stack=Stack()
        # YOUR CODE STARTS HERE

        #Performs basic arithmetic operations on operands num1, num2, given operator op
        def Eval(num1, num2, op):
            if op == "^":
                return num2**num1
            if op == "*":
                return num2*num1
            if op == "/":
                return num2/num1
            if op == "+":
                return num2+num1
            if op == "-":
                return num2-num1
            return None

        #Returns None if the expression is not valid
        if self._getPostfix(self.__expr) == None:
            return None

        #Initializing global variables
        postfix = self._getPostfix(self.__expr)
        inp = postfix.split()  #Splitting input string into easily processed elements
        stack = Stack()

        #Scanning input and evaluating the postfix expression
        for i in range(len(inp)):
            scanned = inp[i]
            if self.isNumber(scanned):
                stack.push(scanned)
            else:
                num1 = float(stack.pop())
                num2 = float(stack.pop())
                calc = Eval(num1, num2, scanned)
                stack.push(calc)

        output = stack.pop()
        return output
