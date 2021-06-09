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

    #This function converts and and checks if all operands in an operation is of the same type

    def numberChecker(self, tokens):
        converted = False #status if succesfully converted 
        
        tokenscopy = tokens #create copy of tokens and convert to str last two elements
        tokenscopy[-2] = str(tokens[-2])
        tokenscopy[-1] = str(tokens[-1]) 
      
        try:
            result = [int(s) if s.isdigit() else float(s) for s in tokenscopy[-2:]]
            # evaluate the given string containing a Python expression. It could convert the string to either float or int automatically.

            if len(tokens) == 3:
                token1 = 1
                token2 = 2
            elif len(tokens) == 6:
                token1 = 4
                token2 = 5

            if (isinstance(result[0], float) and isinstance(result[1], float)) or (isinstance(result[0], int) and isinstance(result[1], int)):
                if isinstance(result[0], int) and isinstance(result[1], int):
                    tokens[token1] = result[0]
                    tokens[token2] = result[1]
                    converted = True

                if isinstance(result[0], float) and isinstance(result[1], float):
                    tokens[token1] = result[0]
                    tokens[token2] = result[1]
                    converted = True

            if type(result[0]) != type(result[1]):
                self.error('typeErr')
                converted = False
   
            else:
                converted = True
            
            return converted

        except ValueError:
            for token in tokens[-2:]:
                if not self.varNameChecker(token) and not self.numConvert(token)[1]:
                    self.error('wordErr', token)
                    break
                elif not token in self.variables and not self.numConvert(token)[1]:
                    self.error('varErr', token)
           
                    break
            return converted

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
                        
                    elif len(tokens) >= 6: #if assignment with operation
                            if tokens[3] in self.arithmetic: 
                                tokens[3] = self.arithmetic[tokens[3]](tokens) 
                                self.variables[tokens[1]] = tokens[3]
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
                value = input("SNOL> Please enter value for ["+ tokens[1] + "]\nInput: ")
                value = self.numConvert(value)
                if value[1]:
                    self.variables[tokens[1]] = str(value[0])
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
            if len(tokens) == 3 or len(tokens) == 6:
                if tokens[-1] in self.variables:
                    tokens[-1] = self.variables[tokens[-1]]
                if tokens[-2] in self.variables:
                    tokens[-2] = self.variables[tokens[-2]]
                numChecker = self.numberChecker(tokens)
                if numChecker:
                    return tokens[-1] + tokens[-2]
            else:
                self.error('cmdErr')

        except IndexError:
            self.error('cmdErr')
   
    def sub(self, tokens):
        try:
            if len(tokens) == 3 or len(tokens) == 6:
                if tokens[-1] in self.variables:
                    tokens[-1] = self.variables[tokens[-1]]
                if tokens[-2] in self.variables:
                    tokens[-2] = self.variables[tokens[-2]]
                numChecker = self.numberChecker(tokens)
                if numChecker:
                    return tokens[-2] - tokens[-1]
            else:
                self.error('cmdErr')

        except IndexError:
            self.error('cmdErr')

    def mult(self, tokens):
        try:
            if len(tokens) == 3 or len(tokens) == 6:
                if tokens[-1] in self.variables:
                    tokens[-1] = self.variables[tokens[-1]]
                if tokens[-2] in self.variables:
                    tokens[-2] = self.variables[tokens[-2]]
                numChecker = self.numberChecker(tokens)
                if numChecker:
                    return tokens[-1] * tokens[-2]
            else:
                self.error('cmdErr')

        except IndexError:
            self.error('cmdErr')

    def div(self, tokens):
        try:
           
            if len(tokens) == 3 or len(tokens) == 6:
                if tokens[-1] in self.variables:
                    tokens[-1] = self.variables[tokens[-1]]
                if tokens[-2] in self.variables:
                    tokens[-2] = self.variables[tokens[-2]]
                numChecker = self.numberChecker(tokens)
                if numChecker:
                    return tokens[-2] / tokens[-1]
            else:
                self.error('cmdErr')

        except IndexError:
            self.error('cmdErr')

    def mod(self,tokens):
        try:
            if len(tokens) == 3:
                if tokens[-1] in self.variables:
                    tokens[-1] = str(self.variables[tokens[-1]])
                if tokens[-2] in self.variables:
                    tokens[-2] = str(self.variables[tokens[-2]])
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible:
                    if isinstance(tokens[-1], int) and isinstance(tokens[-2], int):
                        return tokens[-2] % tokens[-1]
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