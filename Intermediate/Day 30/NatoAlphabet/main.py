import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    input_word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()
