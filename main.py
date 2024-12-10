from func import add_ex_tracker
from func import del_et_func


if __name__ == '__main__':
    while True:
        choose = input('Select an action (add/a), (del/d), (exit): ').strip().lower()
        
        if choose in ('add', 'a'):
            add_ex_tracker()
        elif choose in ('del', 'd'):
            del_et_func()
        elif choose == 'exit':
            print('Thanks, Bye!')
            break
        else:
            print('incorrect choose')