from operation import Operation

def main():

    Commands = {
    'INTO': Operation.into,
    'BEG': Operation.beg,
    'PRINT': Operation.print,
    'ADD': Operation.add,
    'SUB': Operation.sub,
    'MULT': Operation.mult,
    'DIV': Operation.div,
    'MOD': Operation.mod,
    'EXIT!': Operation.exit
    }

    command = Operation()

    while (command.exit == 0):
        line = input("Command: ")
        tokens = line.split()

        if len(tokens) > 0:
            commandFound = False
            for c in Commands.keys():
                if tokens[0] == c[:len(tokens[0])]: #Initial check for keywords
                    Commands[c](command, tokens)
                    commandFound = True
            if not commandFound:
                if len(tokens) == 1: #If simple expression
                    Commands['PRINT'](command, tokens)
                else:
                    print('Unknown Command')
                
if __name__ == "__main__":
    main()