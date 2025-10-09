from datetime import datetime
import csv
import json
import os
import calendar

class ExpenseTracker:

    def __init__(self, name="MyExpenseTracker", filename=None):
        self.filename = os.path.join(os.path.dirname(__file__), '..', f'{name}.csv')
        self.filename = os.path.abspath(self.filename)
        self.config_file = os.path.join(os.path.dirname(__file__), '..', 'config.json')
        self.config_file = os.path.abspath(self.config_file)
        self.expenses = self.load_from_csv()
        self.name, self.budget, self.next_id = self.load_config()


    def set_name(self, name):
        """Set the name of this ExpenseTracker"""
        self.name = name
        self.save_config()

    def save_config(self):
        """Save the name, budget and the next_id"""
        data = {"name": self.name, "budget": self.budget, "next_id": self.next_id}
        with open(self.config_file, "w") as f:
            json.dump(data, f)

    def load_config(self):
        """Load the name, budget and the next_id from the config file"""
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                data = json.load(f)
                name = data.get("name", 'MyExpenseTracker')
                budget = data.get("budget", 0.0)
                next_id = data.get("next_id", 1)
                return name, budget, next_id
        return 'MyExpenseTracker', 0.0, 1


    def set_budget(self, amount):
        """Set the budget for this expense"""
        self.budget = amount
        self.save_config()
        print(f"Setting budget for this month in {self.budget}")

    def get_budget(self):
        print(f"Budget: {self.budget}")

    def check_budget(self, month=None, year=None):
        """Check if this month is in the budget"""
        if not self.budget:
            print("No budget set")
            return

        now = datetime.now()
        if month is None:
            month = now.month
        if year is None:
            year = now.year

        total = sum(
            float(expense['amount']) for expense in self.expenses
            if datetime.strptime(expense['date'], "%Y-%m-%d %H:%M:%S").month == month and
            datetime.strptime(expense['date'], "%Y-%m-%d %H:%M:%S").year == year
        )

        if total > self.budget:
            print("🚨 ALERT: You exceeded your monthly budget!")
        else:
            remaining = self.budget - total
            print(f"✅ You still have U${remaining:.2f} left in your budget.")

    def add_expense(self, description, amount, category="Others"):
        """Add an expense to the expenses list"""
        expense_id = self.next_id
        self.next_id += 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expenses.append(dict(id=expense_id, description=description, amount=amount, date=date, category=category))
        self.save_to_csv()
        self.save_config()
        print(f"Added {amount} to {description}")
        self.check_budget()

    def update_expense(self, id_expense, description=None, amount=None, category=None):
        """Update an expense"""
        for expense in self.expenses:
            if expense['id'] == id_expense:
                if description is not None:
                    expense['description'] = description
                if amount is not None:
                    expense['amount'] = amount
                if category is not None:
                    expense['category'] = category
                self.save_to_csv()
                return print(f"Updated {expense['description']} to {expense['amount']} of category {expense['category']}")
        return print(f"Expense {id_expense} does not exist.")

    def delete_expense(self, id_expense):
        """Delete an expense"""
        for expense in self.expenses:
            if expense['id'] == id_expense:
                self.expenses.remove(expense)
                print(f"Deleted '{expense['description']}' from id {id_expense} of {self.name}")
                self.save_to_csv()
                return None
        return f"Expense {id_expense} does not exist"

    def show_summary(self):
        """Print a summary of all expenses"""
        summary = 0
        for expense in self.expenses:
            summary += expense['amount']
        print(f"Summary of {self.name} expenses: ${summary}")

    def show_summary_by_month(self, month):
        """Print a summary filtered by month"""
        expenses_filtered_by_month = []
        summary = 0
        for expense in self.expenses:
            expense_date = datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')
            if expense_date.month == month:
                expenses_filtered_by_month.append(expense)
        if not expenses_filtered_by_month:
            print("No expenses filtered by month")
        else:
            for exp in expenses_filtered_by_month:
                summary += exp['amount']
            print(f'Total expenses for {calendar.month_name[month]}: U${summary}')

    def show_expenses(self, expenses=None):
        """List all expenses"""
        data = expenses or self.expenses

        if len(data) == 0:
            print(f"No expenses found")
            return

        print(f"{'ID':<5}{'Category':<15}{'Description':<20}{'Amount (U$)':<12}{'Data'}")
        print("-"*80)

        for expense in data:
            print(f"{expense['id']:<5}{expense['category']:<15}{expense['description']:<20}{expense['amount']:<12.2f}{expense['date']}")

    def show_expenses_by_month(self, month, year):
        """List all expenses by month"""
        expenses_filtered = []
        for expense in self.expenses:
            expense_date = datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')
            if month == expense_date.month and year == expense_date.year:
                expenses_filtered.append(expense)
        if not expenses_filtered:
            print(f"No expenses found for month {month} of {year}")
        else:
            print(f"Month {month} of {year} expenses: ")
            self.show_expenses(expenses_filtered)

    def show_expenses_by_category(self, category):
        """List all expenses by category"""
        expenses_filtered = []
        for expense in self.expenses:
            if expense['category'].lower() == category.lower():
                expenses_filtered.append(expense)
        if not expenses_filtered:
            print(f"No expenses found for category {category}")
        else:
            print(f"Category {category}: ")
            self.show_expenses(expenses_filtered)

    def save_to_csv(self):
        """Save all expenses to a csv file"""
        with open(self.filename, 'w', newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "category", "description", "amount", "date"])
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)

    def load_from_csv(self):
        """Load all expenses from a csv file"""
        try:
            expenses = []
            if os.path.exists(self.filename):
                with open(self.filename, mode="r", newline="", encoding="utf-8") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        expenses.append({
                            "id": int(row["id"]),
                            "category": row["category"],
                            "description": row["description"],
                            "amount": float(row["amount"]),
                            "date": row["date"]
                        })

            return expenses
        except FileNotFoundError:
                print(f"⚠️ Arquivo '{self.filename}' não encontrado. Nenhum dado carregado.")