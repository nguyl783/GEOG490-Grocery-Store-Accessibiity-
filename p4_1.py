# Implement your solution here. Remember to follow the 210 Style and PEP8.
# Include doctests whenever appropriate. Feel free to delete these comments.
# To run doctests, at the "Console" below, type: python -m doctest p4_1.py -v


def encrypt(msg: str) -> str:
    '''
    takes a given string (msg) and encrypts the string

    Args:
    msg = a string 

    Returns
    a string with the inputted message encrypted

    >>> encrypt('0123')
    '1302'

    >>> encrypt('012')
    '102'
    '''
    even_char = ''    # Initialize string of even characters
    odd_char = ''     # Initialize string of odd characters 
    char_counter = 0      # Intialize counter of all characters

    for char in msg:
        if char_counter % 2 == 0:   # % 2 will detect odd or even
            even_char = even_char + char
        else:
            odd_char = odd_char + char
        char_counter = char_counter + 1

    encrypted_text = odd_char + even_char
    return encrypted_text


def decrypt(msg: str) -> str:
    '''
    takes a give string that is encrypted and decrypts it

    Args:
    msg = an inputted string

    Return:
    a string of the msg decrypted

    >>> decrypt('102')
    '012'

    >>> decrypt('1302')
    '0123'
    '''
    half_length = len(msg) // 2
    even_char = msg[half_length:]  # the last half are the even char
    odd_char = msg[:half_length]   # first half are the odd char
    decrypted_text = ''

    for i in range(half_length):
        decrypted_text = decrypted_text + even_char[i]
        decrypted_text = decrypted_text + odd_char[i]

    if len(odd_char) < len(even_char):
        decrypted_text = decrypted_text + even_char[-1]

    return decrypted_text

def main():
    """Main program to run our encryption/decryption process."""

    which = input('Do you wish to encrypt or decrypt a message [E/D]? ')
    if which.upper() == 'E':
        text = input('Enter a line of text to encrypt: ')
        print("Encrypted text:")
        print(encrypt(text))
    elif which.upper() == 'D':
        text = input('Enter encrypted text to decrypt: ')
        print("Decrypted text:")
        print(decrypt(text))
    else:
        raise ValueError("Invalid option, I only know E and D!")


if __name__ == '__main__':
    main()
