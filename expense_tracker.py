import argparse

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker") #creates the command-line "reader."
    subparsers = parser.add_subparsers(dest="command") # create a subparser for each command (add, list, delete)
    
    add_parser = subparsers.add_parser("add") # create a subparser for the "add" command
    add_parser.add_argument("--description", required=True) # add an argument for the description of the expense, make it required
    add_parser.add_argument("--amount", required=True, type=float) # add an argument for the amount of the expense, make it required and convert it to a float
    
    
    args = parser.parse_args() # look what the user typed in the command line and make it available as "args"
                               # understand it using the rules i gave you
                               # store the results in a variable called "args"

if __name__ == "__main__":
    main()