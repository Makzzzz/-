import random
user =  input('Введите то, что вы хотите показать (камень, ножницы или бумага): ')
possible_moves = ['камень', 'ножницы', 'бумага']
computer = random.choice(possible_moves)
print(f'\nВы выбрали {user}, компьютер выбрал {computer}. \n')


if user == computer:
    print('Ничья!')
elif user == 'камень':
    if computer == 'ножницы':
        print('Повезло!')
    else:
        print('Лошара!')
elif user == 'бумага':
    if computer == 'камень':
        print('Повезло!')
    else:
        print('Лошара!')
elif user == 'ножницы':
    if computer == 'бумага':
        print('Повезло!')
    else:
        print('Лошара!')