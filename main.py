def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return "Shift must be an integer value."

    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def menu():
    print("=" * 70)
    anwser = input("Select an option: 1 for encrypt, 2 for decrypt or 'q' to quit: ")
    if anwser == "1":
        message = input("Type your message for encryption: ")
        shift = int(input("Type the shift: "))
        encrypted_text = encrypt(message, shift)
        print(encrypted_text)
    elif anwser == "2":
        message = input("type your cipher for decryption: ")
        shift = int(input("Type the shift: "))
        encrypted_text = decrypt(message, shift)
        print(encrypted_text)
    elif anwser == "q":
        print("bye ;)")
    else:
        print("Please select a valid value")
        return menu()
    print("=" * 70)


menu()
