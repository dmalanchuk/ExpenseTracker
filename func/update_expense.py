from func.load_json import load_json
import json


def up_list():
    expenses = load_json('data/expense.json')
    up_inp = input('Enter the ID to update: ')
    
    next_up_ex = next((exp for exp in expenses if exp['id'] == int(up_inp)), None)
    
    if not next_up_ex:
        print('Not found ID')
        return
    
    upd_desc = input('Enter new description: ')
    upd_cost = input('Enter new cost: ')
    
    if upd_desc:
        next_up_ex['description'] = upd_desc
    
    if upd_cost:
        next_up_ex['ammout'] = upd_cost
        
    with open('data/expense.json', 'w') as file:
        json.dump(expenses, file, indent=4)