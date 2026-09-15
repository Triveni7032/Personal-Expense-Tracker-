# Personal Expense Tracker

expenses = []
categories = set()


def add_expense():
    print("\n===== Add Expense =====")

    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    # Dictionary
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    # Add dictionary to list
    expenses.append(expense)

    # Add category to set
    categories.add(category)

    print("Expense added successfully!")


def view_expenses():
    print("\n===== All Expenses =====")

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            "|",
            expense["name"],
            "| ₹", expense["amount"],
            "|",
            expense["category"]
        )


def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Spending: ₹", total)


def view_categories():
    print("\n===== Expense Categories =====")

    if not categories:
        print("No categories found.")
        return

    for category in categories:
        print("-", category)


def category_summary():
    print("\n===== Category Summary =====")

    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

    for category, amount in summary.items():
        print(category, ":", "₹", amount)


def delete_expense():
    view_expenses()

    if not expenses:
        return

    number = int(input("\nEnter expense number to delete: "))

    if 1 <= number <= len(expenses):
        removed_expense = expenses.pop(number - 1)

        print(
            "Deleted:",
            removed_expense["name"]
        )

    else:
        print("Invalid expense number.")


def show_example_tuple():
    print("\n===== Tuple Example =====")

    expense_status = ("Food", "Completed")

    print("Expense Status:", expense_status)
    print("Expense Category:", expense_status[0])
    print("Status:", expense_status[1])


def main():
    while True:

        print("\n==============================")
        print("   PERSONAL EXPENSE TRACKER")
        print("==============================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. View Categories")
        print("5. Category Summary")
        print("6. Delete Expense")
        print("7. Tuple Example")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            view_categories()

        elif choice == "5":
            category_summary()

        elif choice == "6":
            delete_expense()

        elif choice == "7":
            show_example_tuple()

        elif choice == "8":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()