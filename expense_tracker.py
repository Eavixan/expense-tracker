import argparse
import json
import os

def load_expenses(): # this function will load the expenses from a file called "expenses.json"
    if not os.path.exists("expenses.json"): # if the file does not exist, return an empty list
        return []
    
    with open("expenses.json", "r") as file: # open the file in read mode
        return json.load(file) # read the contents of the file and convert it from JSON format to a Python list, then return it

def save_expenses(expenses): # this function will save the expenses to a file called "expenses.json"
    with open("expenses.json", "w") as file: # open the file in write mode
        json.dump(expenses, file, indent=4) # convert the expenses list to JSON format and write it to the file, with an indentation of 4 spaces for readability



def main():
    parser = argparse.ArgumentParser(description="Expense Tracker") #creates the command-line "reader."
    subparsers = parser.add_subparsers(dest="command") # create a subparser for each command (add, list, delete)
    
    add_parser = subparsers.add_parser("add") # create a subparser for the "add" command
    add_parser.add_argument("--description", required=True) # add an argument for the description of the expense, make it required
    add_parser.add_argument("--amount", required=True, type=float) # add an argument for the amount of the expense, make it required and convert it to a float
    

    args = parser.parse_args() # look what the user typed in the command line and make it available as "args"
                               # understand it using the rules i gave you
                               # store the results in a variable called "args"

    if args.command == "add": # if the user typed "add" as the command
        expenses = load_expenses() # load the existing expenses from the file  
        
        if len(expenses) == 0: # if there are no expenses in the list, start the id from 1
            new_id = 1
        else:
            new_id = expenses[-1]["id"] + 1 # get the id of the last expense in the list and add 1 to it to create a new unique id for the new expense
        
        expense = {
            "id": new_id,
            "description": args.description,
            "amount": args.amount
        }

        expenses.append(expense)
        save_expenses(expenses)

        print(f"Expense added successfully (ID: {new_id})")

if __name__ == "__main__":
    main()