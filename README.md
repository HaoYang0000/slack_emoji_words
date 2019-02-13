# slack_words
The aim of the repo is converting words to emoji and printing out to slack
![alt text](http://haostool.appspot.com/static/deal_with_it.png)

# Prerequisite
No need to install at this point.

# Running
1. Go to the repo
2. python ./main.py {SLACK_EMOJI} {WORDS_OR_SENTENCE_YOU_WANT_TO_PRINT}
3. add flag -c to copy it automatically, (works for mac), not sure on windows.

# Example: 
1. python ./main.py :dealwithit: DEAL with it
2. python ./main.py -c :ship_it_down: ship

# Future work
I am trying to find a library which could convert the string character into a 2d grip array. So the word could be automatically generated without manully create the formating.

# Known issues:
