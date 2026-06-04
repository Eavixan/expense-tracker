import argparse
import json
import os
from datetime import date

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
    
    list_parser = subparsers.add_parser("list") # create a subparser for the "list" command

    summary_parser = subparsers.add_parser("summary") # create a subparser for the "summary" command

    delete_parser = subparsers.add_parser("delete") # create a subparser for the "delete" command
    delete_parser.add_argument("--id", required=True, type=int) # add an argument for
    
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
            "date": str(date.today()),
            "description": args.description,
            "amount": args.amount
        }

        expenses.append(expense) # add the new expense to the list of expenses
        save_expenses(expenses) # save the updated list of expenses back to the file

        print(f"Expense added successfully (ID: {new_id})")

    elif args.command == "list": # if the user typed "list" as the command
        expenses = load_expenses() # load the existing expenses from the file
        print("Expenses:")
        for expense in expenses:
            print(f"  ID: {expense['id']}, Date: {expense.get('date', 'N/A')}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}")

    elif args.command == "summary": # if the user typed "summary" as the command
        expenses = load_expenses()  # load the existing expenses from the file

        total = 0
        for expense in expenses:
            total = total + expense["amount"] # add up the amounts of all the expenses to get the total
        print(f"Total expenses: ${total:.2f}") # print the total expenses in a formatted way with 2 decimal places

    elif args.command == "delete": # if the user typed "delete" as the command
        expenses = load_expenses()  # load the existing expenses from the file
        expense_to_delete = None # initialize a variable to keep track of the expense that we want to delete, start with None (no expense found yet)
        for expense in expenses: 
            if expense["id"] == args.id: # check if the id of the current expense matches the id provided by the user in the command line
                expense_to_delete = expense # if we find a match, store that expense in the variable "expense_to_delete" and
                break
        if expense_to_delete: # if we found an expense to delete (the variable is not None)
            expenses.remove(expense_to_delete) # remove that expense from the list of expenses
            save_expenses(expenses) # save the updated list of expenses back to the file
            print(f"Expense deleted successfully (ID: {args.id})")
        else:
            print(f"Expense with ID {args.id} not found.") # if we did not find an expense with the given id, print a message saying it was not found

if __name__ == "__main__":
    main()