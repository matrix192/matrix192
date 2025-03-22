def siske(size):
    x = f'{' '*(size-1)}'
    string_siske = f'({x}.{x})({x}.{x})'
    print(string_siske)

def penis(size):
    x = f'{'='*(size)}'
    string_penis = f'8{x}3'
    print(string_penis)
    
user_input = int(input("Введите число, не переборщите: "))
siske(user_input)
penis(user_input)
