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
        args = line.split()

        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]: #Initial check for keywords
                    Commands[c](command, args)
                    print(Commands[c])
                    commandFound = True
            if not commandFound:
                print('can\'t understand')
                
if __name__ == "__main__":
    main()