import sys, getopt, os, platform
from characters import *

HELP_MESSAGE = "Please pass an emoji and a sentence to print. \n\n" \
               "Format: python ./main.py {SLACK_EMOJI} {WORDS_OR_SENTENCE_YOU_WANT_TO_PRINT} \n\n" \
               "For example: python ./main.py :dealwithit: DEAL with it \n\n" \
               "To print the word in the same line, do: python ./main.py -s :dealwithit: DEAL with it \n\n" \
               "Add flag -c to avoid the copy process(for your convenience :) " \
               "For example: python ./main.py -c {SLACK_EMOJI} {WORDS_OR_SENTENCE_YOU_WANT_TO_PRINT} \n\n" \
               ";-) \n"


def main(argv):
    """
    Main method to run, read command line argument
    :param argv:
    :return:
    """
    emoji = None
    # If print the word in same line
    if_same_line = False
    # If copy to clipboard automatically
    if_copy_to_clipboard = False

    # Check if argument is enough
    if len(argv) <= 1:
        print(HELP_MESSAGE)
        sys.exit(0)

    # Read options
    try:
        opts, args = getopt.getopt(argv, "chs")
    except getopt.GetoptError as error:
        print(HELP_MESSAGE)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(HELP_MESSAGE)
            sys.exit(0)
        elif opt == "-s":
            if_same_line = True
        elif opt == "-c":
            if_copy_to_clipboard = True

    # Set up emoji to use, could be multiple
    # Todo: Add validation maybe
    emoji = args[0]

    # Generate output
    if if_same_line is False:
        output = __process_each_character_per_line(emoji=emoji, sentence=args[1:])
    else:
        output = __process_each_character_same_line(emoji=emoji, sentence=args[1:])

    if if_copy_to_clipboard is True:
        add_to_clipboard(output)
    print(output)

def add_to_clipboard(output):
    # TODO: Fix this method.
    if platform.system() == 'Windows':
        command = 'echo ' + output.strip() + '| clip'
        os.system(command)
    else:
        os.system("echo '%s' | pbcopy" % output)

def __str_to_class(class_name: str):
    """
    Convert string of class name to class
    :param str:class_name
    :return: class
    """
    try:
        return getattr(sys.modules[__name__], class_name)
    except AttributeError:
        print("The character {character} is not implemented yet :( ".format(character=class_name))
        return None


def __process_each_character_per_line(emoji: str, sentence: list) -> str:
    """
    Process each word, and print out each character to per line
    :param emoji:
    :param sentence:
    :return:
    """
    output = "\n"
    # Append every word in array
    for words in sentence:
        # Process each character
        for character in words:
            class_name = character
            word = __str_to_class(class_name.upper())
            if word is not None:
                output = output + word(emoji=emoji).print() + "\n"
        output = output + "\n"
    return output


def __process_each_character_same_line(emoji: str, sentence: list):
    """
    Process each word, and print out each character for a word on the same line
    :param emoji:
    :param sentence:
    :return:
    """
    return "This is not done yet :("


if __name__ == "__main__":
    main(sys.argv[1:])
