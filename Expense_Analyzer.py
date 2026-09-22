# ========================================
#       SMART EXPENSE ANALYZER
# ========================================

expenses = []

while True:

    print("\n" + "=" * 40)
    print("       SMART EXPENSE ANALYZER")
    print("=" * 40)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Expense Summary")
    print("6. Category Analysis")
    print("7. Budget Status")
    print("8. Exit")

    choice = input("\nEnter your choice: ")


    # ========================================
    # 1. ADD EXPENSE
    # ========================================

    if choice == "1":

        category = input("Enter category: ")
        amount = int(input("Enter amount: "))

        expense = {
            "Category": category,
            "Amount": amount
        }

        expenses.append(expense)

        print("\nExpense added successfully!")


    # ========================================
    # 2. VIEW EXPENSES
    # ========================================

    elif choice == "2":

        if len(expenses) == 0:

            print("\nNo expenses available.")

        else:

            print("\n" + "-" * 40)
            print("           ALL EXPENSES")
            print("-" * 40)

            for i in range(len(expenses)):

                print(
                    f"{i + 1}. "
                    f"{expenses[i]['Category']} : "
                    f"₹{expenses[i]['Amount']}"
                )


    # ========================================
    # 3. SEARCH EXPENSE
    # ========================================

    elif choice == "3":

        if len(expenses) == 0:

            print("\nNo expenses available.")

        else:

            search_category = input(
                "Enter category to search: "
            )

            found = False
            category_total = 0

            print("\n" + "-" * 40)
            print(f"Expenses in '{search_category}'")
            print("-" * 40)

            for expense in expenses:

                if expense["Category"].lower() == search_category.lower():

                    print(
                        f"{expense['Category']} : "
                        f"₹{expense['Amount']}"
                    )

                    category_total += expense["Amount"]
                    found = True

            if found:

                print("-" * 40)
                print(
                    f"Total spent on {search_category}: "
                    f"₹{category_total}"
                )

            else:

                print(
                    f"No expenses found for "
                    f"'{search_category}'."
                )


    # ========================================
    # 4. DELETE EXPENSE
    # ========================================

    elif choice == "4":

        if len(expenses) == 0:

            print("\nNo expenses available.")

        else:

            print("\n" + "-" * 40)
            print("           ALL EXPENSES")
            print("-" * 40)

            for i in range(len(expenses)):

                print(
                    f"{i + 1}. "
                    f"{expenses[i]['Category']} : "
                    f"₹{expenses[i]['Amount']}"
                )

            delete_number = int(
                input("\nEnter expense number to delete: ")
            )

            if 1 <= delete_number <= len(expenses):

                deleted_expense = expenses.pop(
                    delete_number - 1
                )

                print(
                    f"\nDeleted: "
                    f"{deleted_expense['Category']} -> "
                    f"₹{deleted_expense['Amount']}"
                )

            else:

                print("\nInvalid expense number.")


    # ========================================
    # 5. EXPENSE SUMMARY
    # ========================================

    elif choice == "5":

        if len(expenses) == 0:

            print("\nNo expenses available.")

        else:

            total = 0
            highest = expenses[0]
            lowest = expenses[0]

            for expense in expenses:

                total += expense["Amount"]

                if expense["Amount"] > highest["Amount"]:
                    highest = expense

                if expense["Amount"] < lowest["Amount"]:
                    lowest = expense

            expense_count = len(expenses)
            average = total / expense_count

            print("\n" + "=" * 40)
            print("           EXPENSE SUMMARY")
            print("=" * 40)

            print(f"Number of Expenses : {expense_count}")
            print(f"Total Expenses     : ₹{total}")
            print(f"Average Expense    : ₹{average:.2f}")

            print(
                f"Highest Expense    : "
                f"{highest['Category']} -> "
                f"₹{highest['Amount']}"
            )

            print(
                f"Lowest Expense     : "
                f"{lowest['Category']} -> "
                f"₹{lowest['Amount']}"
            )


    # ========================================
    # 6. CATEGORY ANALYSIS
    # ========================================

    elif choice == "6":

        if len(expenses) == 0:

            print("\nNo expenses available.")

        else:

            category_totals = {}

            for expense in expenses:

                category = expense["Category"]
                amount = expense["Amount"]

                if category in category_totals:

                    category_totals[category] += amount

                else:

                    category_totals[category] = amount


            print("\n" + "=" * 40)
            print("          CATEGORY ANALYSIS")
            print("=" * 40)

            for category, amount in category_totals.items():

                print(
                    f"{category} : ₹{amount}"
                )


            # Highest spending category

            highest_category = ""
            highest_amount = 0

            for category, amount in category_totals.items():

                if amount > highest_amount:

                    highest_amount = amount
                    highest_category = category


            # Lowest spending category

            lowest_category = ""
            lowest_amount = float("inf")

            for category, amount in category_totals.items():

                if amount < lowest_amount:

                    lowest_amount = amount
                    lowest_category = category


            print("-" * 40)

            print(
                f"Highest Spending Category: "
                f"{highest_category} -> "
                f"₹{highest_amount}"
            )

            print(
                f"Lowest Spending Category: "
                f"{lowest_category} -> "
                f"₹{lowest_amount}"
            )


    # ========================================
    # 7. BUDGET STATUS
    # ========================================

    elif choice == "7":

        budget = int(
            input("Enter your monthly budget: ₹")
        )

        total = 0

        for expense in expenses:

            total += expense["Amount"]


        remaining = budget - total

        print("\n" + "=" * 40)
        print("           BUDGET STATUS")
        print("=" * 40)

        print(f"Budget          : ₹{budget}")
        print(f"Total Spent     : ₹{total}")

        if remaining > 0:

            print(f"Remaining       : ₹{remaining}")
            print("Status          : Within Budget")

        elif remaining == 0:

            print("Remaining       : ₹0")
            print("Status          : Budget Fully Used")

        else:

            print(f"Over Budget     : ₹{abs(remaining)}")
            print("Status          : Budget Exceeded")


    # ========================================
    # 8. EXIT
    # ========================================

    elif choice == "8":

        print("\nThank you for using Smart Expense Analyzer!")
        print("Goodbye!")

        break


    # ========================================
    # INVALID OPTION
    # ========================================

    else:

        print("\nInvalid choice. Please enter 1-8.")
