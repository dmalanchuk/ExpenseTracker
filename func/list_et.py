from func.load_json import load_json


def list_et():
    expenses = load_json('data/expense.json')
    
    max_desc_len = max(len(item['description']) for item in expenses)
    max_cost_len = max(len(str(item['ammout'])) for item in expenses)
    max_date_len = max(len(item['data']) for item in expenses)
    
    header = f"{'Description'.ljust(max_desc_len)} | {'Cost'.ljust(max_cost_len)} | {'Date'.ljust(max_date_len)}"
    print(header)
    print("-" * len(header))
    
    for item in expenses:
        print(f"{item['description'].ljust(max_desc_len)} | {str(item['ammout']).ljust(max_cost_len)} | {item['data'].ljust(max_date_len)}")