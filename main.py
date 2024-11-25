from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(direction, original_text, shift_amount):
    if direction == 'encode':
        def encrypt(original_text, shift_amount):
            cipher_text = ""
            for letter in original_text:
                if letter not in alphabet:
                    cipher_text += letter
                else:
                    shifted_position = alphabet.index(letter) + shift_amount
                    shifted_position %= len(alphabet)
                    cipher_text += alphabet[shifted_position]
            print(f"Here is the encoded result: {cipher_text}")
        return encrypt(original_text, shift_amount)
    elif direction == 'decode':
        def decrypt(original_text, shift_amount):
            normal_text = ""
            for letter in original_text:
                if letter not in alphabet:
                    normal_text += letter
                else:
                    shifted_position = alphabet.index(letter) - shift_amount
                    shifted_position %= len(alphabet)
                    normal_text += alphabet[shifted_position]
            print(f"Here is the decoded result: {normal_text}")
        return decrypt(original_text, shift_amount)
    else:
        print("Please type 'encode' or 'decode':")


continue_program = True

while continue_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(direction, text, shift)

    ask_continue = input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()

    if ask_continue == "no":
        continue_program = False
        print("Thank you for Encoding/Decoding!")
