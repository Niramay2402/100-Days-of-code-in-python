# Organised Caesar Cipher code...

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_l, c_direction):
    text_input = ""

    if c_direction == "encode":
        for letter in text:
            index = alphabet.index(letter)
            index += shift_l
            if index >= 25:
                index -= 26
            text_input += alphabet[index]
        return print(f"The encrypted text is {text_input}.")
    elif c_direction == "decode":
        for letter in plain_text:
            index = alphabet.index(letter)
            index -= shift_l
            if index >= 25:
                index += 26
            text_input += alphabet[index]
        return print(f"The decrypted text is {text_input}.")
    else:
        print("Please enter a valid input.")


caesar(text, shift, direction)
