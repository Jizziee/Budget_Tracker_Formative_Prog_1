from budget_tracker import BudgetTracker

bt = BudgetTracker()

while True:
    print("\n=== Budget Tracker Menu ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. List Transactions")
    print("4. Filter Transactions")
    print("5. Show Summary")
    print("6. Delete a Transaction")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bt.add_income()
    elif choice == "2":
        bt.add_expense()
    elif choice == "3":
        bt.list_transactions()
    elif choice == "4":
        bt.filter_transactions()
    elif choice == "5":
        bt.show_summary()
    elif choice == "6":
        bt.delete_transaction()
    elif choice == "0":
        print("Goodbye! See you soon!")
        break
    else:
        print("Invalid option!")
