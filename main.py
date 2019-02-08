import sys
from words import D, E, A, L, W, I, T, H

def str2Class(str):
    return getattr(sys.modules[__name__], str)

class InputTaker:
    emoji = ""

    def run(self):
        if len(sys.argv) <= 2:
            print ("Please pass an emoji and a sentence to print: ")
            sys.exit(0)
        
        # Set up emoji to use, could be multiple
        emoji = sys.argv[1]

        # Append every word in array
        for words in sys.argv[2:]:
            # Process each character
            for character in words:
                class_name = character
                word = str2Class(class_name.upper())
                print (word(emoji=emoji).print())
            print ("\n")

if __name__ == "__main__":
    InputTaker().run()