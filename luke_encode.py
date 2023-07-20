#  luke moshos encoder
#  7/19/2023

def print_menu():
    options = ['Encode', 'Decode', 'Quit']
    print('Menu')
    print('------------')
    for index, item in enumerate(options):
        print(f'{index + 1}. {item}')
    print()


def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode_pass(encoded_password):
    password = ""
    for digit in encoded_password:
        new_digit = str((int(digit) - 3) % 10)
        password += new_digit
    return password

def main():
    while True:
        print_menu()

        option = int(input('Please enter an option: '))
        if option == 1:
            password = int(input('Please enter your password to encode here: '))
            password = encode(str(password))
            print('Your password has been encoded and stored!')
        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decode_pass(password)}.")
        elif option == 3:
            exit()
        else:
            print("Invalid Option. Please try again.")


if __name__ == '__main__':
    main()
