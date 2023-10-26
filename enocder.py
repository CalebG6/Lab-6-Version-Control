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


def decode(p):

    decoded_string = ""
    decoded_value = 0
    for i in range(len(p)):

        decoded_value = int(p[i])-3
        if decoded_value < 0:
            decoded_value += 10
        decoded_string += str(decoded_value)

    return decoded_string

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
            if encoded_p is not None:
                decoded = decode(encoded_p)
                print(f'The encoded password is {encoded_p}, the original password is {decoded}')
            else:
                print('m')
        if(user_choice==3):
            break

if __name__ == '__main__':
    main()

