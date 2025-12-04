

                                            Budget Tracker 

This project is a simple command-line budget tracker written in Python.
It allows a user to record income and expenses, view all transactions, filter them, and see a financial summary.

The project uses Object-Oriented Programming and stores each transaction as an object.

1. Project Overview

The goal of this project is to help users track how they spend and earn money.
The program runs in the terminal and lets the user enter the date, amount, category, and a small description for every transaction.

I followed a day-by-day plan to build the project gradually (classes first, features later, then menu and documentation).

2. Features

- Add income

- Add expenses

- View all transactions

- Filter transactions: by type (income/expense), by category, and by month

- View summary

- total income

- total expenses

- balance

- totals per category

3. How to Run the Program

- Open the project folder in PyCharm.

- Make sure all files are in the same directory:main.py, budget_tracker.py, transaction.py

Run the program using: python main.py or press Run inside PyCharm.

4. Menu Structure

After running the program, you get the following menu:

1) Add Income
2) Add Expense
3) List All Transactions
4) Filter Transactions
5) Show Summary
0) Exit


Each option requests the necessary inputs and then displays results in the terminal.

5. Sample Interaction

Example of adding income:

--- Add Income ---

Enter date (YYYY-MM-DD): 2025-03-01

Enter amount: 1500

Enter category: salary

Enter description: March salary

✔ Income added successfully!


Example of the summary:

Total Income: 1500.0

Total Expense: 300.0

Balance: 1200.0

6. Screenshots

Screenshots are in the /screenshots folder:

add_income.png

list_transactions.png

filter_category.png

summary.png

7. Project Status : All core features have been implemented successfully, and the project is fully functional in the terminal.