import argparse
from datetime import datetime
from ExpenseTracker import ExpenseTracker

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Simple Expense Tracker"
    )
    subparsers = parser.add_subparsers(dest="command", help="Avaliable Commands")

    # -----------------
    # Add
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", required=True, help="Amount of the expense")
    add_parser.add_argument("--category", type=str, help="category of the expense")
    # -----------------
    # Update
    update_parser = subparsers.add_parser("update", help="Update an expense")
    update_parser.add_argument("--id", required=True, type=int, help="ID of the expense")
    update_parser.add_argument("--description", help="Description of the expense")
    update_parser.add_argument("--amount", help="Amount of the expense")
    update_parser.add_argument("--category", help="Category of the expense")

    # -----------------
    # list
    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.add_argument("--month", type=int, help="List filtered by month")
    list_parser.add_argument("--year", type=int, help="List filtered by year")
    list_parser.add_argument("--category", help="List filtered by category")

    # -----------------
    # summary
    summary_parser = subparsers.add_parser("summary", help="Show summary of an expense")
    summary_parser.add_argument("--month", type=int, help="Filter by month number (1-12)")

    # -----------------
    # delete
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, help="ID of the expense")

    # -----------------
    # set name
    set_name_parser = subparsers.add_parser('name', help='Set the name of a expense')
    set_name_parser.add_argument("--set", type=str, help="Name of the expense")

    # -----------------
    # set budget
    set_budget_parser = subparsers.add_parser('budget', help='Set the budget of an expense')
    set_budget_parser.add_argument("--amount", type=float, help="Budget of the expense")

    args = parser.parse_args()
    tracker = ExpenseTracker()

    # Execution of commands
    if args.command == "add":
        tracker.add_expense(args.description, args.amount, args.category)
    elif args.command == "delete":
        tracker.delete_expense(args.id)
    elif args.command == 'update':
        tracker.update_expense(args.id, description=None or args.description, amount=None or args.amount, category=None or args.category)
    elif args.command == "name":
        tracker.set_name(args.name)
    elif args.command == "budget":
        if args.amount:
            tracker.set_budget(args.amount)
        else:
            tracker.get_budget()
    elif args.command == "list":
        if args.category:
            tracker.show_expenses_by_category(args.category)
        elif args.month or args.year:
            month = args.month if args.month else datetime.today().month
            year = args.year if args.year else datetime.today().year
            tracker.show_expenses_by_month(month, year)
        else:
            tracker.show_expenses()
    elif args.command == "summary":
        if args.month:
            tracker.show_summary_by_month(args.month)
        else:
            tracker.show_summary()

if __name__ == "__main__":
    main()




