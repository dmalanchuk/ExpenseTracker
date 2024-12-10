from func.load_json import load_json
import json


def del_et_func():
    del_in = input('Enter the ID to be deleted: ')
    expenses = load_json('data/expense.json')
    
    try:
        del_in = int(del_in)
    except ValueError as ve:
        print(f'error: {ve}')
        
    if not expenses['id']:
        print('ID is not')
        
    for item in expenses:
        if item['id'] == del_in:
            expenses.remove(item)
        
    with open('data/expense.json', 'w') as file:
        json.dump(expenses, file, indent=4)
        
        
        