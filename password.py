import random


banner = r'''
 ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ ____
||P |||a |||s |||s |||w |||o |||r |||d |||       |||G |||e |||n |||e |||r |||a |||t |||o |||r ||
||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|


'''


def generator(pass_number, pass_length):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    for pq in range(pass_number):
        password = ''
        for i in range(pass_length):
            password += random.choice(chars)
        print("Password generated: {}".format(password))


def main():
    print(banner)
    pass_number = int(input("Number of passwords: "))
    pass_length = int(input("Number of characters: "))
    print('')
    generator(pass_number, pass_length)
    print('\nNote: Save the password so you do not forget!')


if __name__ == '__main__':
    main()
