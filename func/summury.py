from func.load_json import load_json


def sum_list():
    expenses = load_json('data/expense.json')
    sum_item_list = []
    for i in expenses:
        sum_item_list.append(int(i['ammout']))
        
    print(sum(sum_item_list))
    
        