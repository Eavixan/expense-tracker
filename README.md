# Expense Tracker CLI

A simple command-line expense tracker built with Python.

This project allows users to add, update, delete, list, and summarize expenses using the terminal.

## Features

- Add an expense with a description and amount
- Automatically save expenses to a JSON file
- View all expenses
- View total expenses
- View expenses for a specific month
- Update an existing expense
- Delete an expense
- Basic error handling for invalid amounts and missing IDs

## Technologies Used

- Python
- argparse
- JSON file storage

## Project Structure

```text
expense-tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/expense-tracker.git
```

Go into the project folder:

```bash
cd expense-tracker
```

Run the app:

```bash
py expense_tracker.py
```

Or:

```bash
python expense_tracker.py
```

## Commands

### Add an Expense

```bash
py expense_tracker.py add --description "Lunch" --amount 20
```

Example output:

```bash
Expense added successfully (ID: 1)
```

### View All Expenses

```bash
py expense_tracker.py list
```

Example output:

```bash
Expenses:
  ID: 1, Date: 2026-06-04, Description: Lunch, Amount: $20.00
```

### View Total Summary

```bash
py expense_tracker.py summary
```

Example output:

```bash
Total expenses: $20.00
```

### View Monthly Summary

```bash
py expense_tracker.py summary --month 6
```

Example output:

```bash
Total expenses for month 6: $20.00
```

### Update an Expense

```bash
py expense_tracker.py update --id 1 --description "Dinner" --amount 25
```

Example output:

```bash
Expense updated successfully
```

### Delete an Expense

```bash
py expense_tracker.py delete --id 1
```

Example output:

```bash
Expense deleted successfully (ID: 1)
```

## Data Storage

Expenses are saved in a local JSON file called:

```text
expenses.json
```

Each expense is stored with:

- ID
- Date
- Description
- Amount

Example:

```json
[
    {
        "id": 1,
        "date": "2026-06-04",
        "description": "Lunch",
        "amount": 20.0
    }
]
```

https://roadmap.sh/projects/expense-tracker
