#ISSUES: Takes float with .0 as data typpe int. It should take 0 to 9

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
        status = False #status if succesfully converted 
        undefined_variable = False #if the variable is undefined
        try:
            result = [int(float(x)) if int(float(x)) == float(x) else float(x)  for x in tokens[-2:]] #convert last 2 tokens to int/float
            # print(result)

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
                                    print("Invalid number format")
                        
                    elif len(tokens) == 6: #if assignment with operation
                            for keyword in self.arithmetic: # IF expression (ADD,SUB..) is encountered
                                if tokens[3] == keyword: 
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
                                    else:
                                        print("Incompatible data type")
                else:
                    self.error(2)

            else:
                print("Unknown word " + str(tokens[1]))

        except IndexError:
            self.error(2)

    def beg(self, tokens):
        # tokens = ['BEG', 'value'/'assigned_variable_name']
        try:
            if self.varNameChecker(tokens[1]):
                value = input("SNOL> Please enter value for "+ tokens[1] + "\nInput: ")
                value = self.numConvert(value)
                if value[1]:
                    self.variables[tokens[1]] = value[0]
                else:
                    print("Invalid number format")
            
            else:
                print("Unknown Command " + str(tokens[1]))
            
        except IndexError:
            self.error(1)

    def print(self, tokens):
        # tokens = ['PRINT', 'assigned_variable_name']

        try:
            if len(tokens) == 1 and tokens[0] in self.variables:
                print("")
            elif tokens[1] in self.variables:
                print("SNOL> " + "[" + tokens[1]+ "]" + " = " + str(self.variables[tokens[1]]))
            else:
                print("SNOL> " + tokens[1])
        except IndexError:
            self.error(1)

    def add(self, tokens):
        try:
            # tokens = ['ADD', 'value'/'variable_name', 'value'/'variable_name']
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
         
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]

                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                  
                    return tokens[1] + tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        print("Operands not of the same type")
                        
            else:
                return tokens[4] + tokens[5]
        except IndexError:
            self.error(1)

    def sub(self, tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    return tokens[1] - tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    if typeCompatible[0]:
                        self.error(3)
                         
            else:
                return tokens[4] - tokens[5] 
        except IndexError:
            self.error(1)

    def mult(self,tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    return tokens[1] * tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        self.error(3)
            else:
                return tokens[4] * tokens[5] 
        except IndexError:
            self.error(1)
        
    def div(self,tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    return tokens[1] / tokens[2]
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        self.error(3)
            else:
                return tokens[4] / tokens[5] 
        except IndexError:
            self.error(1)

    def mod(self,tokens):
        try:
            if len(tokens) <= 3:
                if tokens[1] in self.variables:
                    tokens[1] = self.variables[tokens[1]]
                if tokens[2] in self.variables:
                    tokens[2] = self.variables[tokens[2]]
                typeCompatible = self.numberChecker(tokens)
                if typeCompatible[0]:
                    if isinstance(tokens[1], int) and isinstance(tokens[2], int):
                        return tokens[1] % tokens[2]
                    else:
                        print("MOD operation only allows integer type")
                else:
                    if typeCompatible[1]:
                        None
                    else:
                        self.error(2)
                        None 
            else:
                if isinstance(tokens[4], int) and isinstance(tokens[4], int):
                    return tokens[4] % tokens[5]
                else:
                    print("MOD operation only allows integer type")
        except IndexError:
            self.error(1)
    # Mutates exit variable to 1, to exit the loop
    def error(self, errcode):
        keywords = {
            1: 'Unknown command',
            2: 'Unknow command language blabla',
            3: 'Error! Operands must be of the same type in an arithmetic operation!'
        }
        print(keywords[errcode])
        
    def exit(self, tokens):
        print("Interpreter is now terminated...")
        self.exit = 1

    


    