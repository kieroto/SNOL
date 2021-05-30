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
        tokens = line.split() #Tokenize the string input
        

        if len(tokens) > 0:
            commandFound = False

            # Initial check: Checks if the first token is in Commands dict, and then will proceed to the function. 
            # Example:
            #     Input: BEG var1
            #     BEG here is token[0] and will be checked if valid command  in Commands Dict
            #     If valid, it will execute the beg function with tokens taken as input
            if tokens[0] in Commands:
                Commands[tokens[0]](command, tokens)
                commandFound = True
            if not commandFound:
                if len(tokens) == 1: #If the first token is not a valid function(Commands dict) but is a valid simple expression.
                    Commands['PRINT'](command, tokens)
                else:
                    print('Unknown Command Does not match any valid command of the language')
                
if __name__ == "__main__":
    main()