import ast

class Operation:
    def __init__(self):
        #Dictionary to store variables and its value
        self.variables = {}

        self.keywords = {
            'INTO',
            'BEG',
            'PRINT',
            'ADD',
            'SUB',
            'MULT',
            'DIV',
            'MOD',
            'EXIT!',
        }

        self.arithmetic = {
            'ADD': self.add,
            'SUB': self.sub,
            'MULT': self.mult,
            'DIV': self.div,
            'MOD': self.mod,
        }

        self.exit = 0

    #HELPER FUNCTIONS
    # Since tokens input is in string, we will need a function that will convert digits to value types INT or FLOAT
    def numConvert(self, token):
        try:
            try:
                return int(token), True
            except ValueError:
                return float(token), True
        except ValueError:
            return token, False

    #This function converts and checks if all operands in an operation is of the same type
    #Returns a tuple, 
    #tuple[0] is if it succesfully converted arithmetic operands, 
    #[1] boolean value depending if the operand is a valid variable 
    def numberChecker(self, tokens):
        converted = False #status if succesfully converted 
        undefined_variable = False #if the variable is undefined
        try:
            print("tokens = " + str(tokens))
            result = [ast.literal_eval(x) for x in tokens[-2:]] 
            #safely evaluate the given string containing a Python expression. It could convert the string to either float or int automatically.
            print("result = " + str(result))
            print("new tokens = " + str(tokens))

            if len(tokens) <= 3:
                token1 = 1
                token2 = 2
            elif len(tokens) <= 6:
                token1 = 4
                token2 = 5

            if isinstance(result[0], int) and isinstance(result[1], int):
                tokens[token1] = result[0]
                tokens[token2] = result[1]
                print(str(tokens[token1]))
                print(str(tokens[token2]))
                converted = True

            else:
                tokens[token1] = result[0]
                tokens[token2] = result[1]
                print(str(tokens[token1]))
                print(str(tokens[token2]))
                converted = True
            return converted, undefined_variable

        except ValueError as e:
            
            if len(tokens) <= 3:
                e = str(e).split(": ")
                stripped_e = str(e[-1:]).replace("'", "").strip("[]").strip('"')
                if stripped_e.isidentifier():
                    self.error('varErr', stripped_e)
                else:
                    self.error('wordErr', stripped_e)
                    token2 = 2
            elif len(tokens) <= 6:
                print("ELIF ERORR HJERE")
                print("token length is" + str(len(tokens)))
            else:
                print("token length is" + str(len(tokens)))
                print("ELSE ERROR HERE")
 
            undefined_variable = True
            return converted, undefined_variable
    

    # Variable format checker
    # returns true if variable name is valid, (not in keywords or not an identifier)
    def varNameChecker(self, tokens):
        return str(tokens).isidentifier() and not (tokens in self.keywords)
#       Use this for typchecking
#         >>> 'X'.isidentifier()
#               True


    # MAIN OPERATIONS
    # Assignment operation
    def into(self, tokens):
        # simple assignment : tokens = ['INTO', 'new_variable_name', 'IS', 'value'/'assigned_variable_name']
        # assignment with operation : tokens = ['INTO', 'new_variable_name', 'IS', 'OPERATION', 'value'/'assigned_variable_name', 'value'/'assigned_variable_name']

        #check syntax error
        try:
            if self.varNameChecker(tokens[1]):
                if tokens[2] == 'IS':
                    if len(tokens) == 4: # If simple assignment
                            if tokens[3] in self.variables: #check if in variables dictionary, then assign to tokens[1]
                                self.variables[tokens[1]] = self.variables[tokens[3]]
                            else: #if not in variables, treat tokens[3], check if a value and assign if it is a valid value
                                tokens[3] = self.numConvert(tokens[3])
                                if tokens[3][1]:
                                    self.variables[tokens[1]] = tokens[3][0]
                                else:
                                    self.error('formatErr')
                        
                    elif len(tokens) >= 5: #if assignment with operation
                            if tokens[3] in self.arithmetic: 
                                #Check if it is in dictionary
                                if tokens[4] in self.variables:
                                    tokens[4] = self.variables[tokens[4]]
                                    

                                if tokens[5] in self.variables:
                                    tokens[5] = self.variables[tokens[5]]


                                #check if datatypecompatible
                                typeCompatible = self.numberChecker(tokens)
                                if typeCompatible[0]:
                                    tokens[3] = self.arithmetic[keyword](tokens) 
                                    self.variables[tokens[1]] = tokens[3]
                                # if validVariable and validVariable2:
                                #     self.error('typeErr')
                                else:
                                    self.error("varErr")
                            else:
                                self.error('cmdErr')

                    else:
                        self.error('cmdErr')                 
                else:
                    self.error('cmdErr')
            else:
                self.error('wordErr', str(tokens[1]))

        except IndexError:
            self.error('cmdErr')

    def beg(self, tokens):
        # tokens = ['BEG', 'value'/'assigned_variable_name']
        try:
            if self.varNameChecker(tokens[1]):
                value = input("SNOL> Please enter value for "+ tokens[1] + "\nInput: ")
                value = self.numConvert(value)
                if value[1]:
                    self.variables[tokens[1]] = value[0]
                else:
                    self.error('formatErr')
            
            else:
                self.error('wordErr', str(tokens[1]))
            
        except IndexError:
            self.error('cmdErr')

    def print(self, tokens):
        # tokens = ['PRINT', 'assigned_variable_name']

        try:
            if len(tokens) == 1 and tokens[0] in self.variables:
                print("")
            elif tokens[1] in self.variables:
                print("SNOL> " + "[" + tokens[1]+ "]" + " = " + str(self.variables[tokens[1]]))
            else:
                if self.numConvert(tokens[1])[1]:
                    print("SNOL> " + "[" + tokens[1]+ "]")
                else:
                    self.error('varErr', tokens[1])
        except IndexError:
            self.error('cmdErr')

    def add(self, tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = str(self.variables[tokens[1]])
                    print(str(tokens[1]))
                if tokens[2] in self.variables:
                    tokens[2] = str(self.variables[tokens[2]])
                    print(str(tokens[1]))
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print("Type compatible")
                    return str(tokens[1] + tokens[2])
                else:
                    if typeCompatible[1]:
                        self.error('varErr')
                    else:
                        self.error('typeErr')
            elif len(tokens) <= 6:
                return str(tokens[4] + tokens[5])
        except IndexError:
             self.error('cmdErr')

    def sub(self, tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = str(self.variables[tokens[1]])
                    print(str(tokens[1]))
                if tokens[2] in self.variables:
                    tokens[2] = str(self.variables[tokens[2]])
                    print(str(tokens[1]))
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print("Type compatible")
                    return str(tokens[1] - tokens[2])
                else:
                    if typeCompatible[1]:
                        self.error('varErr')
                    else:
                        self.error('typeErr')
            elif len(tokens) <= 6:
                return str(tokens[4] - tokens[5])
        except IndexError:
             self.error('cmdErr')

    def mult(self, tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = str(self.variables[tokens[1]])
                    print(str(tokens[1]))
                if tokens[2] in self.variables:
                    tokens[2] = str(self.variables[tokens[2]])
                    print(str(tokens[1]))
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print("Type compatible")
                    return str(tokens[1] * tokens[2])
                else:
                    if typeCompatible[1]:
                        self.error('varErr')
                    else:
                        self.error('typeErr')
            elif len(tokens) <= 6:
                return str(tokens[4] * tokens[5])
        except IndexError:
             self.error('cmdErr')

    def div(self, tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = str(self.variables[tokens[1]])
                    print(str(tokens[1]))
                if tokens[2] in self.variables:
                    tokens[2] = str(self.variables[tokens[2]])
                    print(str(tokens[1]))
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print("Type compatible")
                    return str(tokens[1] / tokens[2])
                else:
                    if typeCompatible[1]:
                        self.error('varErr')
                    else:
                        self.error('typeErr')
            elif len(tokens) <= 6:
                return str(tokens[4] / tokens[5])
        except IndexError:
                self.error('cmdErr')
    def mod(self,tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = str(self.variables[tokens[1]])
                if tokens[2] in self.variables:
                    tokens[2] = str(self.variables[tokens[2]])
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    if isinstance(tokens[1], int) and isinstance(tokens[2], int):
                        return str(tokens[1] % tokens[2])
                    else:
                        print("MOD operation only allows integer type")
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        self.error('typeErr')
                        None 
            else:
                if isinstance(tokens[4], int) and isinstance(tokens[4], int):
                    return str(tokens[4] % tokens[5])
                else:
                    print("MOD operation only allows integer type")
        except IndexError:
            self.error('cmdErr')
    # Mutates exit variable to 1, to exit the loop
    def error(self, errcode, str=''):
        keywords = {
            'wordErr': 'Unknown word ' + '['+str+']',
            'cmdErr': 'Unknown command! Does not match any valid command of the language.',
            'typeErr': 'Incompatible types: Error! Operands must be of the same type in an arithmetic operation!',
            'varErr': 'Undefined variable ' '['+str+']',
            'formatErr': 'Invalid number format ' + str,
        }
        print(keywords[errcode])
        
    def exit(self, tokens):
        print("Interpreter is now terminated...")
        self.exit = 1