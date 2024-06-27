from random import randint

number = randint(1,100)


def main():
    while True:
        userNumber = int(input('Введите число: '))
        if userNumber < number:
            print('Число меньше')
        elif userNumber > number:
            print('Число больше')
        elif userNumber == userNumber:
            break

    print('Отличная интуиция!')


main()