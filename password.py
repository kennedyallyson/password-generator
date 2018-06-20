import random


banner = r'''
 ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ ____
||P |||a |||s |||s |||w |||o |||r |||d |||       |||G |||e |||n |||e |||r |||a |||t |||o |||r ||
||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

'''
note = '\nNote: Save the password so you do not forget!'

def generator(pass_quantity, pass_len):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    for pq in range(pass_quantity):
        password = ''
        for i in range(pass_len):
            password += random.choice(chars)

        print("Password generated: {}".format(password))


if __name__ == '__main__':
    print(banner)
    pass_quantity = int(input("Quantidade de passwords: "))
    pass_len = int(input('Tamanho da senha: '))
    print('')
    generator(pass_quantity, pass_len)
    print(note)
