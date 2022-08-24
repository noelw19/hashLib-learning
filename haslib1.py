import hashlib
import chardet


def main():

    passtocrack = input('Enter password to hash and crack: ')


    phash = hashlib.md5(passtocrack.encode('utf-8')).hexdigest()
    print(f'\n\nPassword to crack = {passtocrack}\nHash: {phash}\n\n')

    passwordhash = phash
    wordlist = input("Enter password list filename: ")
    if wordlist == '':
        wordlist = './lrgpasswordlist.txt'
    attempts = 0
    try:
        passwordfile = open(wordlist, 'r')
    except:
        print('No file found.')
        quit()

    try:
        flag = 0
        for word in passwordfile:
            # when you want to hash str in py it 
            # has to be of certain encoding which is utf-8

            # encodes the string obtained from word 
            # list and encodes it then returns res to var
            encoded_word = word.encode('utf-8')

            digest = hashlib.md5(encoded_word.strip()).hexdigest()

            if digest == passwordhash:
                print(f'Password found!!\nPassword: {word}\nAttempts: {attempts}')
                flag = 1
                break
            else:
                attempts += 1
        if flag == 0:
            print(f'No password found with given list')
    except BaseException as e:
        print(f'Error found! {e}\nAttempts: {attempts}')


if __name__ == '__main__':
    main()