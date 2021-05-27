# Morse Code Translator


# variables description
# morse: stores the morse translated form of the english string
# english: stores the english translated form of the morse string
# engtext: stores morse code of a single character
# i: keeps count of the spaces between morse characters
# message: stores the string to be encoded or decoded


# Dictionary representing the morse code chart
morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    """
    function to encrypt the string according to the morse code chart
    """
    morse = ''
    for letter in message:
        if letter != ' ':
            # looks up the dictionary and adds the corresponding morse code
            # along with a space to separate morse codes for different characters
            morse += morse_code_dict[letter] + ' '
        else:
            # 1 space indicates different characters & 2 indicates different words
            morse += ' '

    return morse


def decrypt(message):
    """
    function to decrypt the string from morse to english
    """
    # extra space added at the end to access the last morse code

    message += ' '
    english = ''
    engtext = ''

    for letter in message:

        # checks for space
        if letter != ' ':

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            engtext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                english += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                english += list(morse_code_dict.keys())[list(morse_code_dict
                                                             .values()).index(engtext)]
                engtext = ''

    return english


# Main function
def main():
    print("Do you want to translate your message 'to Morse Code' or 'to English'?")
    sel = input("Enter your selection - \n"
                "a: 'to Morse Code'\n"
                "b: 'to English'\n")
    message = input("Enter your message below:\n")
    if sel == "a":
        result = encrypt(message.upper())
        print("Your translated message in Morse Code:")
        print(result)
    else:
        result = decrypt(message)
        print("Your translated message in English:")
        print(result)


# Executes the main function
if __name__ == '__main__':
    main()
