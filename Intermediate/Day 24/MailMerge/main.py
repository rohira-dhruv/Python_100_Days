PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    recipient_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_template_file:
    letter_template = letter_template_file.read()
    for name in recipient_list:
        name = name.strip()
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as mail:
            send_letter = letter_template.replace(PLACEHOLDER, name)
            mail.write(send_letter)
