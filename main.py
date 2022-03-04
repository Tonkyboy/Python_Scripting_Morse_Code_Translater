""" Copyright Alexander Reute 2022

This Project is my first Protfolio Project for CommandLine based Python programming.

International Morse Code Converter function. Forward and backward encryption.

"""

import itertools

# Source for table: https://en.wikipedia.org/wiki/Morse_code
CONVERSION_TABLE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
                    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
                    "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
                    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
                    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
                    "7": "--...", "8": "---..", "9": "----.", "0": "-----", ", ": "--..--", ".": ".-.-.-",
                    "?": "..--..", "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-", " ": " "}


def word_to_morsecode():
    """Transforms words into morsecode whit triple space as break"""
    input_words = input("Insert your words for translation into morsecode here: ").upper()
    morse_code = ""

    splited_letters = [letter for letter in input_words]

    for letter in splited_letters:
        morse_code += " " + CONVERSION_TABLE[letter]
    return morse_code


def morsecode_to_word():
    """Transforms the morsecode in uppercase words with the original spaces"""
    input_morse_code = input("Insert your morse code  for translation into words here: ").upper().replace("   ",
                                                                                                        " / ").replace("  ",
                                                                                                        " / ").split(
        " ")
    splitted_letters = []
    for codes in input_morse_code:
        if codes == "/":
            letter = " "
            splitted_letters.append(letter)
        else:
            letter = [letter for letter, morse_code in CONVERSION_TABLE.items() if morse_code == codes]
            splitted_letters.append(letter)

    megred_list = list(itertools.chain.from_iterable(splitted_letters))
    words = "".join(megred_list)

    return words


def choose_way():
    """Choose the way of translation. Word to morse code or morse code to word"""
    choose_way: int = int(input("Translate from words to morse code type 1. "
                                "Translate from morse code to words type 2: "))
    return choose_way


def rerun():
    re_run: str = (input("Do another translation, type Y. Exit, type N: ")).upper()
    if re_run == "Y":
        run_translation()
    elif re_run == "N":
        print("Bye!")


def run_translation():
    """Run the translation Bot"""
    try:
        chosen_way = choose_way()
        if chosen_way == 1:
            print(word_to_morsecode())
            rerun()
        elif chosen_way == 2:
            print(morsecode_to_word())
            rerun()
        else:
            print("Typo? Try again pls.")
            run_translation()

    except KeyError:
        print("This program doesnt support special characters. Please just use numbers letters and numbers!")
        restart_input = input("Wanna restart? Type y or n? ").upper()
        if restart_input == "Y":
            print(word_to_morsecode())
        elif restart_input == "N":
            print("Bye!")


run_translation()
