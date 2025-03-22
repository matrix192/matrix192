def siske(size):
    x = f'{' '*(size-1)}'
    string_siske = f'({x}.{x})({x}.{x})'
    print(string_siske)
    print("Сиськее")

def penis(size):
    x = f'{'='*(size)}'
    string_penis = f'8{x}3'
    print(string_penis)
    print("Члеееен")

switch = int(input("Введите 1, чтобы увидеть сиськи. Введите 2, чтобы увидеть член: "))
if (switch == 1):
    user_input = int(input("Введите размер сисек: "))
    siske(user_input)
elif (switch == 2):
    user_input = int(input("Введите размер члена(в см): "))
    penis(user_input)
else:
    print("БЛя, какое еблан")
