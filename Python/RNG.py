import random

def readFiles( ):
    names = [str(i).split() for i in open('names.txt','r',encoding='utf-8')]
    words = [str(i).split() for i in open('words.txt','r',encoding='utf-8')]
    return [names, words]

def main():
    print('Добро пожаловать в генератор никнеймов\n')
    while True:
        parameter = input('\n----------------------\n1 - Запуск генератора\n0 - Выход\n----------------------\nВвод: ')
        match parameter:
            case('0'):
                break
            case('1'):
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
    return

if __name__ == "__main__":
    main()