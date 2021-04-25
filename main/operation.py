#TO DO

class Operation:
    def __init__(self):

        self.variables = {
        }

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

    def into(self, tokens):
        # tokens = ['INTO', 'new_variable_name', 'IS', 'value'/'assigned_variable_name']
        # tokens = ['INTO', 'new_variable_name', 'IS', 'OPERATION', 'value'/'assigned_variable_name', 'value'/'assigned_variable_name']

        #check syntax error
        if self.varNameChecker(tokens[1]):
            if tokens[2] == 'IS':
                if len(tokens) == 4: #If No operation like ADD, SUB, MULT, ETC...
                    #check if valid variablename
                        # print("valid word")
                        if tokens[3] in self.variables: #check if in variables dictionary, then assign
                            # print("arg[3] is in variables")
                            self.variables[tokens[1]] = self.variables[tokens[3]]
                        else: #if not, treat tokens[3] as a value and assign to variable
                            tokens[3] = self.numConvert(tokens[3])
                            self.variables[tokens[1]] = tokens[3][0]
                    
                elif len(tokens) == 6:
                        for keyword in self.arithmetic: # IF expression (ADD,SUB..) is encountered
                            if tokens[3] == keyword: 
                                #Check if it is in dictionary
                                if tokens[4] in self.variables:
                                    tokens[4] = self.variables[tokens[4]]
                                    print(tokens)
                                if tokens[5] in self.variables:
                                    tokens[5] = self.variables[tokens[5]]
                                    print(tokens)
                                #check if datatypecompatible
                                typeCompatible = self.numberChecker(tokens)
                                if typeCompatible[0]:
                                    tokens[3] = self.arithmetic[keyword](tokens) 
                                    self.variables[tokens[1]] = tokens[3]
                                else:
                                    print("Incompatible data type")

                print(self.variables)

            else:
                print("Unknown command")

        else:
            print("Unknown word " + str(tokens[1]))

    def beg(self, tokens):
        # tokens = ['BEG', 'value'/'assigned_variable_name']
        try:
            if self.varNameChecker(tokens[1]):
                value = input("SNOL> Please enter value for "+ tokens[1] + "\nInput: ")
                value = self.numConvert(value)
                if value[1]:
                    self.variables[tokens[1]] = value[0]
                    
                    print(self.variables)
                else:
                    print("Invalid number format")
            
            else:
                print("Unknown Command " + str(tokens[1]))
            
        except IndexError:
            print("Unknown Command")

    def print(self, tokens):
        # tokens = ['PRINT', 'assigned_variable_name']
        try:
            if tokens[0] in self.variables:
                print("SNOL> " + str(self.variables[tokens[0]]))
            elif tokens[1] in self.variables:
                print("SNOL> " + str(self.variables[tokens[1]]))
            else:
                print("Undeclared Variable")
        except IndexError:
            print("Undeclared Variable")

    def add(self, tokens):
        try:
            # tokens = ['ADD', 'value'/'variable_name', 'value'/'variable_name']
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                    print(tokens)
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                    print(tokens)
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print(tokens[1] + tokens[2])
                    return tokens[1] + tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        print("Operands not of the same type")
                        
            else:
                return tokens[4] + tokens[5]
        except IndexError:
            print("Unknown Command") 

    def sub(self, tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                    print(tokens)
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                    print(tokens)
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print(tokens[1] - tokens[2])
                    return tokens[1] - tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    if typeCompatible[0]:
                        print("Operands not of the same type")
                         
            else:
                return tokens[4] - tokens[5] 
        except IndexError:
            print("Unknown Command") 
    def mult(self,tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                    print(tokens)
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                    print(tokens)
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print(tokens[1] * tokens[2])
                    return tokens[1] * tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        print("Operands not of the same type")
            else:
                return tokens[4] * tokens[5] 
        except IndexError:
            print("Unknown command") 
        
    def div(self,tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                    print(tokens)
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                    print(tokens)
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print(tokens[1] / tokens[2])
                    return tokens[1] / tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        print("Operands not of the same type")
            else:
                return tokens[4] / tokens[5] 
        except IndexError:
            print("Unknown command") 

    def mod(self,tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                    print(tokens)
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                    print(tokens)
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    print(tokens[1] % tokens[2])
                    return tokens[1] % tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        print("Operands not of the same type")
                        None 
            else:
                return tokens[4] % tokens[5]
        except IndexError:
            print("Unknown command") 

    def exit(self, tokens):
        print("Interpreter is now terminated...")
        self.exit = 1

    def numConvert(self, tokens):
        try:
            try:
                return int(tokens), True
            except ValueError:
                return float(tokens), True
        except ValueError:
            return tokens, False

    #convert string to float or int for operations
    def numberChecker(self, tokens):
        status = False
        undefined_variable = False
        try:
            result = [int(float(x)) if int(float(x)) == float(x) else float(x)  for x in tokens[-2:]] #convert last 2 tokens to int/float
            print(result)

            if len(tokens) <= 3:
                token1 = 1
                token2 = 2
            else:
                token1 = 4
                token2 = 5

            if isinstance(result[0], int) and isinstance(result[1], int):
                tokens[token1] = result[0]
                tokens[token2] = result[1]
                status = True

            elif isinstance(result[0], float) and isinstance(result[1], float):
                tokens[token1] = result[0]
                tokens[token2] = result[1]
                status = True
            return status, undefined_variable

        except ValueError as e:
            e = str(e).split()
            print("Undefined Variable " + str(e[-1:])) 
            undefined_variable = True
            return status, undefined_variable


    def varNameChecker(self, tokens):
        return str(tokens).isidentifier() and not (tokens in self.keywords)
    # https://stackoverflow.com/questions/36330860/pythonically-check-if-a-variable-name-is-valid
#       User this for typchecking
#         >>> 'X'.isidentifier()
#               True