class Operation:
    def __init__(self):

        self.variables = {
            "num1": 4,
            "num2": 3,
        }

        self.arithmetic = {
            'ADD': self.add,
            'SUB': self.sub,
        }

        self.exit = 0

    def into(self, args):
        #args = ['INTO', 'variablename', 'IS', 'EXPRESSION/token', (token, token)]
        #args[1] is the variablename
            # Need checking
        # IS keyword also need checking
        #args[3] is the value to be assigned
        if len(args) == 4:
            if args[3] in self.variables:
                print("arg[3] is in variables")
                self.variables[args[1]] = self.variables[args[3]]
            else:
                self.variables[args[1]] = args[3]
        else:
            for keyword in self.arithmetic: # IF expression (ADD,SUB..) is encountered
                if args[3] == keyword: 
                    #check if adding variables, find if it is in dictionary
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
                        print("invalid")
        
        print(self.variables)

    def beg(self, args):
        # args = [BEG '<varname>']
        if args[1] in self.variables:
            value = input("INPUT: ")
            self.variables[args[1]] = value
            print(self.variables)

    def print(self, args):
        if args[1] in self.variables:
            print(self.variables[args[1]])
        else:
            print("Undeclared Variable")

    def add(self, args):
       return args[4] + args[5]

    def sub(self, args):
        return args[4] - args[5]

    def mult(self):
        print("multing")
        
    def div(self):
        print("dividing")

    def mod(self):
        print("modingg")

    def exit(self, args):
        self.exit = 1

    def numberChecker(self, args):
        status = False
        result = [int(float(x)) if int(float(x)) == float(x) else float(x)  for x in args[-2:]]
        print(result)
        if isinstance(result[0], int) and isinstance(result[1], int):
            args[4] = result[0]
            args[5] = result[1]
            status = True
        if isinstance(result[0], float) and isinstance(result[1], float):
            args[4] = result[0]
            args[5] = result[1]
            status = True
        return status

    def varNameChecker(self):
        print("Suri can't do that")
    # https://stackoverflow.com/questions/36330860/pythonically-check-if-a-variable-name-is-valid
#       User this for typchecking
#         >>> 'X'.isidentifier()
#               True