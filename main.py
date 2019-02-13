from util import Util
from format_factory import process_each_character_per_line, process_each_word_per_line, post_format
import sys, getopt

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
    emoji = ':dealwithit:'
    padding = ':white_large_square:'
    input = 'DEAL with it'
    # If print the word in same line
    if_same_line = False
    # If copy to clipboard automatically
    if_copy_to_clipboard = False
    # If reverse the white board and emoji
    if_reverse = False

    # Read options
    try:
        opts, args = getopt.getopt(argv, "chsrp:e:i:", ["padding=","emoji=","input="])
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
        elif opt == "-r":
            if_reverse = True
        elif opt in ("-p", "--padding"):
            padding = arg
        elif opt in ("-e", "--emoji"):
            emoji = arg
        elif opt in ("-i", "--input"):
            input = arg

    # Generate output format
    if if_same_line is False:
        output = process_each_character_per_line(emoji=emoji, sentence=input.split(' '))
    else:
        output = process_each_word_per_line(emoji=emoji, sentence=input.split(' '))

    # Format output
    output = post_format(output=output, padding=padding, emoji=emoji, if_reverse=if_reverse)
    if if_copy_to_clipboard is True:
        Util.add_to_clipboard(output)
    print(output)


if __name__ == "__main__":
    main(sys.argv[1:])
