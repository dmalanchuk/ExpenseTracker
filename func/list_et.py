from func.load_json import load_json

def list_et():
    expenses = load_json('data/expense.json')
    
    for item in expenses:
        print(f'Description: "{item['description']}", Cost: "{item['ammout']}", Date: "{item['data']}"')