class Operation:
    def __init__(self):

        self.variables = {
            "sample": 1964
        }

        self.arithmetic = {
            'ADD': self.add,
            'SUB': self.sub,
        }

        self.exit = 0

    def into(self, args):
        #args = ['INTO', 'variable name', 'IS', 'EXPRESSION/value']
        #args[1] is the variable name
        #args[3] is the value to be assigned
        valType = self.numberChecker(args)
        print(valType)
        for keyword in self.arithmetic: # IF expression is encountered
            if args[3] == keyword: 
                #if variables find if it is in dictionary
                if args[4] in self.variables:
                    args[4] = self.variables[args[4]]
                if args[5] in self.variables:
                    args[5] = self.variables[args[5]]

                #check if compatible
                if valType != 'incompatible':
                    print('allow filetype')
                    args[3] = self.arithmetic[keyword](args,valType)
                    self.variables[args[1]] = args[3]
        

        if args[3] in self.variables:
            self.variables[args[1]] = args[3]
        else:
            print("invalid")
        print(self.variables)

    def beg(self, args):
        if args[1] in self.variables:
            value = input("INPUT: ")
            self.variables[args[1]] = value
            print(self.variables)

    def print(self, args):
        if args[1] in self.variables:
            print(self.variables[args[1]])
        else:
            print("Undeclared Variable")

    def add(self, args, valueType):
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
        filetype = None
        try:
            # Convert it into integer
            args[4] = int(args[4])
            args[5] = int(args[5])
            print("Both Input is an integer number")
            filetype = 'int'
        except ValueError:
            try:
                # Convert it into float
                args[4] = float(args[4])
                args[5] = float(args[5])
                print("Both Input is an float number")
                filetype = 'float'
            except ValueError:
                print("No.. input is not a number. It's a string")
                filetype = 'incompatible'
        return filetype

    def typeErrorchecker(self):
        print("Suri can't do that")
    # https://stackoverflow.com/questions/36330860/pythonically-check-if-a-variable-name-is-valid
#       User this for typchecking
#         >>> 'X'.isidentifier()
#               True
