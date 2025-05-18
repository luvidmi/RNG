import random
import os
clear = lambda: os.system('cls')

def readFiles():
    names = [str(i).split() for i in open('names.txt','r',encoding='utf-8')]
    words = [str(i).split() for i in open('words.txt','r',encoding='utf-8')]
    return [names, words]

def main():
    print('Добро пожаловать в генератор никнеймов\n')
    while True:
        parameter = input('\n----------------------\n1 - Запуск генератора\n2 - Редактирование списков\n0 - Выход\n----------------------\nВвод: ')
        match parameter:
            case('0'):
                break
            case('1'):
                clear()
                amount = int(input('Введите желаемое количество никнеймов: '))
                print('\n')
                while amount!=0:
                    massNames = readFiles()[0][0]
                    massWords = readFiles()[1][0]

                    name = massNames[random.randint(0,len(massNames)-1)]

                    word = massWords[random.randint(0, len(massNames)-1)]

                    nickName = name + ' ' + word
                    print(nickName)
                    amount -= 1
            case('2'):
                clear()
                action = input('1 - Добавить имя в список\n2 - Добавить слово в список\nВвод: ')
                match action:
                    case('1'):
                        clear()
                        massNames = readFiles()[0][0]
                        massWords = readFiles()[1][0]
                        nameEdit = input('Введите имя, используя нижний регистр: ')
                        file = open('names.txt', 'a', encoding='utf-8')
                        if nameEdit in massNames:
                            clear()
                            print(f'\nИмя {nameEdit} уже есть в списке\n')
                        else:

                            file.write(' ' + nameEdit)
                            clear()
                            print(f'\nИмя {nameEdit} успешно добавлено\n')
                            file.close()
                            
                    case('2'):
                        clear()
                        wordEdit = input('Введите слово, используя нижний регистр: ')
                        file = open('words.txt', 'a', encoding='utf-8')
                        if wordEdit in massWords:
                            clear()
                            print(f'\nСлово {wordEdit} уже есть в списке\n')
                        else:
                            file.write(' ' + wordEdit)
                            clear()
                            print(f'\nСлово {wordEdit} успешно добавлено\n')
                            file.close()


    return

if __name__ == "__main__":
    main()