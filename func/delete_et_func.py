from func.load_json import load_json
import json


def del_et_func():
    del_in = input('Enter the ID to be deleted: ')
    expenses = load_json('data/expense.json')
    
    try:
        del_in = int(del_in)
    
    except ValueError as ve:
        print(f'incorrect value - {ve}')
        
    if not isinstance(expenses, list):
         print("Error: The data in 'expense.json' is not a valid list.")
         
    remove_id_expense = [i for i in expenses if i.get('id') == del_in]
    
    if not remove_id_expense:
        print(f'ID {del_in} not founded')
        
    expenses = [i for i in expenses if i.get('id') != del_in]
    
    with open('data/expense.json', 'w') as f:
        json.dump(expenses, f, indent=4)
        print(f'ID {del_in} Successfully deleted.')
        