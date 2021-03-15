#TO DO

class Operation:
    def __init__(self):

        self.variables = {
            #sample dummy variables
            "num1": 4,
            "num2": 3,
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

    def into(self, args):
        # args = ['INTO', 'new_variable_name', 'IS', 'value'/'assigned_variable_name']
        # args = ['INTO', 'new_variable_name', 'IS', 'OPERATION', 'value'/'assigned_variable_name', 'value'/'assigned_variable_name']

        #check syntax error
        if self.varNameChecker(args[1]):
            if args[2] == 'IS':
                if len(args) == 4: #If No operation like ADD, SUB, MULT, ETC...
                    #check if valid variablename
                        print("valid word")
                        if args[3] in self.variables: #check if in variables dictionary, then assign
                            print("arg[3] is in variables")
                            self.variables[args[1]] = self.variables[args[3]]
                        else: #if not, treat args[3] as a value and assign to variable
                            args[3] = self.numConvert(args[3])
                            self.variables[args[1]] = args[3][0]
                    
                elif len(args) == 6:
                        for keyword in self.arithmetic: # IF expression (ADD,SUB..) is encountered
                            if args[3] == keyword: 
                                #Check if it is in dictionary
                                if args[4] in self.variables:
                                    args[4] = self.variables[args[4]]
                                    print(args)
                                if args[5] in self.variables:
                                    args[5] = self.variables[args[5]]
                                    print(args)
                                #check if datatypecompatible
                                typeCompatible = self.numberChecker(args)
                                if typeCompatible:
                                    args[3] = self.arithmetic[keyword](args) 
                                    self.variables[args[1]] = args[3]
                                else:
                                    print("Incompatible data type")

                print(self.variables)

            else:
                print("Unknown command")

        else:
            print("Unknown word " + str(args[1]))

    def beg(self, args):
        # args = ['BEG', 'value'/'assigned_variable_name']
        try:
            if self.varNameChecker(args[1]):
                value = input("SNOL> Please enter value for "+ args[1] + "\nInput: ")
                value = self.numConvert(value)
                if value[1]:
                    self.variables[args[1]] = value[0]
                    
                    print(self.variables)
                else:
                    print("Invalid number format")
            
            else:
                print("Unknown word " + str(args[1]))
            
        except IndexError:
            print("Unknown Command")

    def print(self, args):
        # args = ['PRINT', 'assigned_variable_name']
        try:
            if args[0] in self.variables:
                print("SNOL> " + str(self.variables[args[0]]))
            elif args[1] in self.variables:
                print("SNOL> " + str(self.variables[args[1]]))
            else:
                print("Undeclared Variable")
        except IndexError:
            print("Undeclared Variable")

    def add(self, args):
        try:
            # args = ['ADD', 'value'/'variable_name', 'value'/'variable_name']
            if len(args) <= 3:
                if args[1] in self.variables:
                    args[1] = self.variables[args[1]]
                    print(args)
                if args[2] in self.variables:
                    args[2] = self.variables[args[2]]
                    print(args)
                typeCompatible = self.numberChecker(args)
                if typeCompatible:
                    print(args[1] + args[2])
                    return args[1] + args[2]
                else:
                    print("operands not of the same type")  
            else:
                return args[4] + args[5]
        except IndexError:
            print("Unknown command") 

    def sub(self, args):
        try:
            if len(args) <= 3:
                if args[1] in self.variables:
                    args[1] = self.variables[args[1]]
                    print(args)
                if args[2] in self.variables:
                    args[2] = self.variables[args[2]]
                    print(args)
                typeCompatible = self.numberChecker(args)
                if typeCompatible:
                    print(args[1] - args[2])
                    return args[1] - args[2]
                else:
                    print("operands not of the same type")  
            else:
                return args[4] - args[5] 
        except IndexError:
            print("Unknown command") 
    def mult(self,args):
        try:
            if len(args) <= 3:
                if args[1] in self.variables:
                    args[1] = self.variables[args[1]]
                    print(args)
                if args[2] in self.variables:
                    args[2] = self.variables[args[2]]
                    print(args)
                typeCompatible = self.numberChecker(args)
                if typeCompatible:
                    print(args[1] * args[2])
                    return args[1] * args[2]
                else:
                    print("operands not of the same type")  
            else:
                return args[4] * args[5] 
        except IndexError:
            print("Unknown command") 
        
    def div(self,args):
        try:
            if len(args) <= 3:
                if args[1] in self.variables:
                    args[1] = self.variables[args[1]]
                    print(args)
                if args[2] in self.variables:
                    args[2] = self.variables[args[2]]
                    print(args)
                typeCompatible = self.numberChecker(args)
                if typeCompatible:
                    print(args[1] / args[2])
                    return args[1] / args[2]
                else:
                    print("operands not of the same type")  
            else:
                return args[4] / args[5] 
        except IndexError:
            print("Unknown command") 

    def mod(self,args):
        try:
            if len(args) <= 3:
                if args[1] in self.variables:
                    args[1] = self.variables[args[1]]
                    print(args)
                if args[2] in self.variables:
                    args[2] = self.variables[args[2]]
                    print(args)
                typeCompatible = self.numberChecker(args)
                if typeCompatible:
                    print(args[1] % args[2])
                    return args[1] % args[2]
                else:
                    print("operands not of the same type")  
            else:
                return args[4] % args[5]
        except IndexError:
            print("Unknown command") 

    def exit(self, args):
        print("Interpreter is now terminated...")
        self.exit = 1

    def numConvert(self, args):
        try:
            try:
                return int(args), True
            except ValueError:
                return float(args), True
        except ValueError:
            return args, False

    #convert string to float or int for operations
    def numberChecker(self, args):
        status = False
        try:
            result = [int(float(x)) if int(float(x)) == float(x) else float(x)  for x in args[-2:]] #convert last 2 tokens to int/float
            print(result)

            if len(args) <= 3:
                token1 = 1
                token2 = 2
            else:
                token1 = 4
                token2 = 5

            if isinstance(result[0], int) and isinstance(result[1], int):
                args[token1] = result[0]
                args[token2] = result[1]
                status = True

            elif isinstance(result[0], float) and isinstance(result[1], float):
                args[token1] = result[0]
                args[token2] = result[1]
                status = True
            return status

        except ValueError as e:
            e = str(e).split()
            print("Undefined Variable " + str(e[-1:])) 
            return status


    def varNameChecker(self, args):
        return str(args).isidentifier() and not (args in self.keywords)
    # https://stackoverflow.com/questions/36330860/pythonically-check-if-a-variable-name-is-valid
#       User this for typchecking
#         >>> 'X'.isidentifier()
#               True