from art import logo


def caesar(message, shift_number, action):
    cipher_message = ""
    if action == "decode":
        shift_number *= -1
    for char in message:
        if char in alphabet:
            current_pos = alphabet.index(char)
            new_pos = (current_pos + shift_number) % 26
            cipher_message += alphabet[new_pos]
        else:
            cipher_message += char
    print(f"Here's the {direction}d result: {cipher_message}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    print(logo)
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    if input("Type 'yes' to continue the game, or 'no' to end game:\n") != 'yes':
        should_continue = False

