import json
from datetime import datetime
from func.load_json import load_json


def add_ex_tracker():
    desc = input('enter description: ')
    cost = input('enter cost: ')
    date_now = datetime.now().strftime('%c') 
    
    name_json = 'data/expense.json'
    expenses = load_json(name_json)
    
    try:
        cost = int(cost)
        
        id = max((expense['id'] for expense in expenses), default=0)
        
        if isinstance(desc, str) and isinstance(cost, int):
            print("Умови виконано успішно.")
        else:
            raise ValueError("desc має бути рядком, а ammout — цілим числом.")
        
        new_expense = {
            'id':  id + 1,
            'description': f'{desc}',
            'ammout': f'{cost}',
            'data':  f'{date_now}'
        }
        
        expenses.append(new_expense)
        
        with open(name_json, 'w') as file:
            json.dump(expenses, file, indent=4)
        
    except ValueError as ve:
        print(f'error: {ve}')
        