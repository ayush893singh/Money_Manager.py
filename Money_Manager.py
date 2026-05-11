trackers = []


def add_tracker():
    tracker_name = input("\nEnter tracker name: ")

    expenses = []

    print(f"\n{tracker_name} Tracker Started\n")

    for i in range(3):
        print(f"Expense {i + 1}")

        item = input("Enter item name: ")

        try:
            amount = float(input("Enter amount: "))

            expense = {
                "item": item,
                "amount": amount
            }

            expenses.append(expense)

            print("Expense added successfully!\n")

        except ValueError:
            print("Please enter numbers only.\n")

    tracker = {
        "name": tracker_name,
        "expenses": expenses
    }

    trackers.append(tracker)


def view_trackers():
    if len(trackers) == 0:
        print("\nNo trackers found.\n")
        return

    print("\n===== All Trackers =====")

    for tracker in trackers:

        print(f"\nTracker Name: {tracker['name']}")

        total = 0

        for index, expense in enumerate(tracker["expenses"], start=1):

            print(
                f"{index}. {expense['item']} - ₹{expense['amount']}"
            )

            total += expense['amount']

        print(f"Total = ₹{total}")


def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Tracker")
        print("2. View Trackers")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_tracker()

        elif choice == "2":
            view_trackers()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


menu()