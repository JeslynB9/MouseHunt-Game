'''
Answer for Question 2 - What's ye called?

Name: Jeslyn Joylie Bowman
SID: 530481526
unikey: jbow2146

'''
# USYD CODE CITATION ACKNOWLEDGEMENT
# This file contains acknowledgements for ideas and/or code

print("Larry: What\'s ye name, Hunter?")
name = input()
print("Larry: Is", "'" + name + "'", "a name I can pronounce?")

# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the majority of the following code has been taken
# from the websited titled: "Check Length of User Input" and is not my
# own work.
#
# Original URL
# https://stackoverflow.com/questions/27651772/check-length-of-user-input
# Last access March 2023

is_valid_length = 1 <= len(name) <= 9

if is_valid_length:
      print ('It has a length of', len(name) ,'which is between 1 to 9 characters?', 'True!')
else:
      print('It has a length of', len(name) ,'which is between 1 to 9 characters?', 'False!')
# End of copied code

# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the majority of the following code has been taken
# from the websited titled: "Check is String starts with a Letter in Python" 
# and is not my own work.
#
# Original URL
# https://thispointer.com/check-if-string-starts-with-a-letter-in-python/
# Last access March 2023

is_valid_start = name[0].isalpha()
# End of copied code

if is_valid_start:
      print('It starts with an alphabet?', 'True')
else:
      print('It starts with an alphabet?', 'False')

# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the parts of the following code has been taken
# from the websited titled: "Determine Whether there is more than one word in a string" 
# and is not my own work.
#
# Original URL
# https://stackoverflow.com/questions/27280791/determine-whether-there-s-more-than-one-word-in-a-string
# Last access March 2023

is_one_word = len(name.strip(' ')) > 1 + int(name.find(' ')) == 0
# End of copied code

if is_one_word:
      print('It is a single word?', 'True')
else:
      print ('It is a single word?', 'False')

is_valid_name = is_valid_length and is_valid_start and is_one_word

if is_valid_name:
      print('Larry: I can pronounce this name ---', 'True')
else:
      print('Larry: I can pronounce this name ---', 'False')

