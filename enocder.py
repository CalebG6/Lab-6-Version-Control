# Caleb Gottlieb


def encode(word):
    if(len(word)!=8):
        print('Password is not 8 characters long!')
        return None
    encoded_m=''
    for i in range(len(word)):
        if(not(word[i].isdigit())):
            print('All characters must be digits!')
            return None
        encoded_m+=str((int(word[i])+3)%10)
    return encoded_m


def main():
    user_choice = 0
    encoded_p = None
    while(user_choice!=3):
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        user_choice = int(input('Please enter an option: '))
        if(user_choice==1):
            while(encoded_p is None):
                password=input('Please enter a password to encode: ')
                encoded_p=encode(password)
            print('\nYour password has been encoded and stored!\n')
        if(user_choice==2):
            print('Placeholder')
            # print(f'The encoded password is {encoded_p}, the original password is {decode(encoded_p)}')
        if(user_choice==3):
            break


main()

