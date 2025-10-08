# Task
# 1: Users can add an expense with a description and amount. ok
# 2: Users can update an expense. ok
# 3: Users can delete an expense.ok
# 4: Users can view all expenses. ok
# 5: Users can view a summary of all expenses. ok
# 6: Users can view a summary of expenses for a specific month (of current year). ok
# 7 : Add expense categories and allow users to filter expenses by category. ok
# 8: Allow users to set a budget for each month and show a warning when the user exceeds the budget.
# 9: Allow users to export expenses to a CSV file.
from datetime import datetime

class ExpenseTracker:

    def __init__(self, name):
        self.name = name
        self.expenses = []
        self.next_id = 1

    def get_expenses(self):
        """return expenses"""
        return self.expenses

    def add_expense(self, description, amount, category="Others"):
        """Add an expense to the expenses list"""
        expense_id = self.next_id
        self.next_id += 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expenses.append(dict(id=expense_id, description=description, amount=amount, date=date, category=category))

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
                return print(f"Updated {expense['description']} to {amount} of category {category}")
        return f"Expense {expense['id']} does not exist"

    def delete_expense(self, id_expense):
        """Delete an expense"""
        for expense in self.expenses:
            if expense['id'] == id_expense:
                self.expenses.remove(expense)
                return print(f"Deleted '{expense['description']}' from id {id_expense} of {self.name}")
        return f"Expense {id_expense} does not exist"

    def summary(self):
        """Print a summary of all expenses"""
        summary = 0
        for expense in self.expenses:
            summary += expense['amount']
        return print(f"Summary of {self.name} expenses: ${summary}")

    def show_expenses(self, expenses=None):
        """List all expenses"""
        data = expenses if expenses is not None else self.expenses

        if not data:
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
            print()
            print(f"Category {category} expenses: ")
            self.show_expenses(expenses_filtered)




joao = ExpenseTracker('joao')
joao.add_expense(description='curso python', amount=100)
joao.add_expense('livro', 155.15)
joao.add_expense('cafe da manhã', 25.50, 'Alimentação')
joao.add_expense('Curso de vendas', 1000)
joao.add_expense('Tênis', 200, 'Vestimenta')
joao.add_expense('Bolo de maracuja', 25, 'Alimentação')
joao.add_expense('Cinema', 50, 'lazer')
joao.update_expense(1, amount=50.55)
joao.delete_expense(2)
joao.show_expenses_by_month(9, 2025)
joao.show_expenses()
joao.show_expenses_by_category('alimentação')

