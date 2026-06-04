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
    summary_parser.add_argument("--month", type=int) # add an optional argument for the month to filter the expenses by month, convert it to an integer

    delete_parser = subparsers.add_parser("delete") # create a subparser for the "delete" command
    delete_parser.add_argument("--id", required=True, type=int) # add an argument for
    
    update_parser = subparsers.add_parser("update") # create a subparser for the "update" command
    update_parser.add_argument("--id", required=True, type=int) # add an argument for the id of the expense to update, make it required and convert it to an integer
    update_parser.add_argument("--description") # add an optional argument for the new description of the expense
    update_parser.add_argument("--amount", type=float) # add an optional argument for the new amount of the expense, convert it to a float
    
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
        total = 0.0
        if args.month: # if the user provided a month to filter by
            for expense in expenses:
                expense_month = int(expense.get("date", "0000-00-00").split("-")[1]) # get the month from the date of the expense, if the date is not available, use "0000-00-00" as a default value to avoid errors
                if expense_month == args.month: # if the month of the expense matches the month provided by the user
                    total += expense["amount"] # add the amount of that expense to the total
            print(f"Total expenses for month {args.month}: ${total:.2f}")
        else: # if the user did not provide a month, calculate the total for all expenses
            for expense in expenses:
                total += expense["amount"] # add the amount of each expense to the total
            print(f"Total expenses: ${total:.2f}")

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

    elif args.command == "update": # if the user typed "update" as the command
        expenses = load_expenses()  # load the existing expenses from the file

        expense_found = False # initialize a variable to keep track of whether we found the expense to update, start with False (not found yet)

        for expense in expenses:
            if expense["id"] == args.id: # check if the id of the current expense matches the id provided by the user in the command line
                if args.description: # if the user provided a new description for the expense
                    expense["description"] = args.description # update the description of that expense with the new value provided by the user
                if args.amount is not None: # if the user provided a new amount for the expense (check for None to allow updating to 0)
                    expense["amount"] = args.amount # update the amount of that expense with the new value provided by the user
                expense_found = True # set the variable to True to indicate that we found and updated the expense
                break

        if expense_found:
            save_expenses(expenses) # save the updated list of expenses back to the file
            print(f"Expense updated successfully (ID: {args.id})")
        else:
            print(f"Expense with ID {args.id} not found.")

if __name__ == "__main__":
    main()