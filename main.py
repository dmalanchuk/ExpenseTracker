from func import add_ex_tracker
from func import del_et_func
from func import list_et
from func import sum_list
from func import up_list

if __name__ == '__main__':
    while True:
        choose = input('\n(add/a), \n(del/d), \n(list/l), \n(sum/s), \n(update/u), \n(exit/e) \nSelect an action:').strip().lower()
        
        if choose in ('add', 'a'):
            add_ex_tracker()
        elif choose in ('del', 'd'):
            del_et_func()
        elif choose in ('list', 'l'):
            list_et()
        elif choose in ('sum', 's'):
            sum_list()
        elif choose in ('update', 'u'):
            up_list()
        elif choose in ('exit', 'e'):
            print('The program has completed its work')
            break
        else:
            print('incorrect choose')