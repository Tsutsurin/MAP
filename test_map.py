from map import node

map_ = node(0,0)

buffer = True
while(buffer == True):
    _ = input('1: Конструкторв\n'
              '2: Удаление\n'
              '3: Сказать пару\n'
              '4: Удалить все\n'
              '5: Выйти\n')
    match _:
        case '1':
            key = int(input('Введите ключ '))
            data = input('Введите данные ')
            map_.add(key, data)
        case '2':
            key = int(input('Введите ключ '))
            map_.delete(key)
        case '3':
            key = int(input('Введите ключ '))
            print(map_.get(key))
        case '4':
            map_.clear()
        case '5':
            buffer = False