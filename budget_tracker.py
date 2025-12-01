from transaction import Income, Expense

class BudgetTracker:

    def __init__(self):
        self.transactions = []

    # ------------------------------
    # Add Income
    # ------------------------------
    def add_income(self):
        print("\n--- Add Income ---")

        date = input("Enter date (YYYY-MM-DD): ")
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")

        # Validation
        try:
            amount = float(amount)
        except ValueError:
            print("❌ Invalid amount! Must be a number.")
            return

        if category.strip() == "":
            print("❌ Category cannot be empty.")
            return

        income = Income(date, amount, category, description)
        self.transactions.append(income)
        print("✔ Income added successfully!")

    # ------------------------------
    # Add Expense
    # ------------------------------
    def add_expense(self):
        print("\n--- Add Expense ---")

        date = input("Enter date (YYYY-MM-DD): ")
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")

        try:
            amount = float(amount)
        except ValueError:
            print(" Invalid amount! Must be a number.")
            return

        if category.strip() == "":
            print(" Category cannot be empty.")
            return

        expense = Expense(date, amount, category, description)
        self.transactions.append(expense)
        print("✔ Expense added successfully!")

    # ------------------------------
    # List All Transactions
    # ------------------------------
    def list_transactions(self):
        print("\n--- All Transactions ---")
        if not self.transactions:
            print("No transactions recorded.")
            return
        for t in self.transactions:
            print(t)

    # ------------------------------
    # Filter Transactions
    # ------------------------------
    def filter_transactions(self):
        print("\n--- Filter Options ---")
        print("1. By Type (income/expense)")
        print("2. By Category")
        print("3. By Month (YYYY-MM)")
        choice = input("Choose filter: ")

        if choice == "1":
            ttype = input("Enter type (income/expense): ").lower()
            results = [t for t in self.transactions if t.type == ttype]

        elif choice == "2":
            cat = input("Enter category: ").lower()
            results = [t for t in self.transactions if t.category == cat]

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            results = [t for t in self.transactions if t.date.startswith(month)]

        else:
            print("Invalid filter option!")
            return

        if not results:
            print("No matching transactions.")
        else:
            print("\n--- Filter Results ---")
            for r in results:
                print(r)

    # ------------------------------
    # Summary Report
    # ------------------------------
    def show_summary(self):
        print("\n--- Summary ---")

        total_income = sum(t.amount for t in self.transactions if t.type == "income")
        total_expense = sum(t.amount for t in self.transactions if t.type == "expense")
        balance = total_income - total_expense

        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Balance: {balance}")

        print("\nPer-Category Totals:")
        category_totals = {}

        for t in self.transactions:
            if t.category not in category_totals:
                category_totals[t.category] = 0
            category_totals[t.category] += t.amount

        for cat, amt in category_totals.items():
            print(f"{cat.title()}: {amt}")
