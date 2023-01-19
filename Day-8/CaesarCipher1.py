# Caesar Cipher program that can encode and decode text with the provided shifted number

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(plain_text, shift_letter):
    encryptedText = ""
    for letter in text:
        index = alphabet.index(letter)
        index += shift
        if index >= 25:
            index -= 26
        encryptedText += alphabet[index]
    return print(f"The encrypted text is {encryptedText}.")


def decrypt(plain_text, shift_letter):
    decryptedText = ""
    for letter in text:
        index = alphabet.index(letter)
        index -= shift
        if index >= 25:
            index += 26
        decryptedText += alphabet[index]
    return print(f"The decrypted text is {decryptedText}.")


if direction.lower() == "encode":
    encrypt(text, shift)
elif direction.lower() == "decode":
    decrypt(text, shift)
else:
    print("Please enter a valid text")
