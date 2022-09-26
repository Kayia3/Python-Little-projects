# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 
                    'B':'-...',
                    'C':'-.-.', 
                    'D':'-..', 
                    'E':'.',
                    'F':'..-.',
                    'G':'--.', 
                    'H':'....',
                    'I':'..', 
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--', 
                    'N':'-.',
                    'O':'---', 
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.', 
                    'S':'...', 
                    'T':'-',
                    'U':'..-', 
                    'V':'...-', 
                    'W':'.--',
                    'X':'-..-', 
                    'Y':'-.--', 
                    'Z':'--..',
                    '1':'.----', 
                    '2':'..---', 
                    '3':'...--',
                    '4':'....-', 
                    '5':'.....', 
                    '6':'-....',
                    '7':'--...', 
                    '8':'---..', 
                    '9':'----.',
                    '0':'-----', 
                    ', ':'--..--', 
                    '.':'.-.-.-',
                    '?':'..--..', 
                    '/':'-..-.', 
                    '-':'-....-',
                    '(':'-.--.', 
                    ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letters in message:
        if letters != ' ':
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letters] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
    return cipher

def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            # counter to keep track of space
            counter = 0
            # storing morse code of a single character
            citext += letter
        else:
            # if i = 1 that indicates a new character
            counter +=1
            # if i = 2 that indicates a new word
            if counter == 2:
                 # adding space to separate words
                decipher += ' '
            else:
                 # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

def main():
    choice = int(input("1 - to encode\n2 - to decrypt\tChoice: "))
    if choice == 1:
        messagetoencrypt= str(input("Please enter your sentence:"))#"Ana are mere"
        result = encrypt(messagetoencrypt.upper())
        print(result)
    elif choice == 2:
        messagetodecrypt = str(input("Please enter sentence in Morse code")) #".- -. .-  .- .-. .  -- . .-. ."
        result2 = decrypt(messagetodecrypt)
        print(result2)
    else: 
        print("Please enter a valid choice")

if __name__ == '__main__':
    main()