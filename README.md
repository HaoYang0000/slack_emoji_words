# slack_words
The aim of the repo is converting words to emoji and printing out to slack


# Installation
No need to install at this point.

# Running
1. Go to the repo
2. python ./main.py {SLACK_EMOJI} {WORDS_OR_SENTENCE_YOU_WANT_TO_PRINT}

Example: python ./main.py :dealwithit: DEAL with it

# Future work
I am trying to find a library which could convert the string character into a 2d grip array. So the word could be automatically generated without manully create the formating.

# Known issues:
1. Slack doesn't like space at the first line of the sentence, so you may see on the first line, the emoji are shift to the left for character: A, C, J, H, I, J, K, M, O, Q, S. Try to avoid using those leter as start character on first line should be fine. 
