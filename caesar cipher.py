letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
        else:
            plaintext += ' '
    return plaintext

# Main loop to ask if user wants to run again
while True:
    print('------ CAESAR CIPHER PROGRAM -----')
    print()

    user_input = input('Do you want to encrypt or decrypt? (e/d): ').lower()

    if user_input == 'e':
        print('ENCRYPTION MODE SELECTED')
        key = int(input('Enter the key (1 through 26): '))
        text = input('Enter the text to encrypt: ')
        ciphertext = encrypt(text, key)
        print(f'CIPHERTEXT: {ciphertext}')

    elif user_input == 'd':
        print('DECRYPTION MODE SELECTED')
        key = int(input('Enter the key (1 through 26): '))
        text = input('Enter the text to decrypt: ')
        plaintext = decrypt(text, key)
        print(f'PLAINTEXT: {plaintext}')

    else:
        print('Invalid option. Please select either "e" for encrypt or "d" for decrypt.')

    # Ask if the user wants to run the program again
    run_again = input('Do you want to run again? (yes/no): ').lower()
    if run_again != 'yes':
        print('Exiting program. Goodbye!')
        break
