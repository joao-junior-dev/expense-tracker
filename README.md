#  Expense Tracker

A simple and practical expense tracker built with Python, featuring:

- Add and list expenses
- Filter by category, month, or year
- Set a monthly budget
- Automatic storage in `.csv` files and configuration in `config.json`
- Intuitive and easy-to-use CLI (Command Line Interface)

---
# Example


#  Installation

### 1. Clone the repository:

```bash
git clone https://github.com/joao-junior-dev/expense-tracker.git
````
```bash
cd expense-tracker
``` 
### 2. Create a virtual environment (optional but recommended):
Windows:
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
``` 
Linux / macOS:
```bash
python -m venv venv
```
```bash
source venv/bin/activate
``` 
### 3. Install the package locally:
```bash
pip install -e .
```
**This will create the expense-tracker command in your terminal, which you can use anywhere.**

#  CLI Usage
Set monthly budget
```bash
expense-tracker budget --amount 1500.00
```

Add an expense
```bash
expense-tracker add --description 'Cinema' --amount 15.00 --category 'Leisure'
```

Update an expense
```bash
expense-tracker update --id 1 --amount 10.00
```
delete an expense
```bash
expense-tracker delete --id 1 
```

list all expenses
```bash
expense-tracker list
```

list all expenses by category
```bash
expense-tracker list --category 'Leisure'
```

list all expenses by month
```bash
expense-tracker list --month 10
```

show summary of all expenses
```bash
expense-tracker summary
```

show summary by month
```bash
expense-tracker summary --month 10
```

