print("Larry: What\'s ye name, Hunter?")
name = input()
print("Larry: Is", "'" + name + "'", "a name I can pronounce?")

is_valid_length = 1 <= len(name) <= 9

if is_valid_length:
      print ('It has a length of', len(name) ,'which is between 1 to 9 characters?', 'True!')
else:
      print('It has a length of', len(name) ,'which is between 1 to 9 characters?', 'False!')

is_valid_start = name[0].isalpha()

if is_valid_start:
      print('It starts with an alphabet?', 'True')
else:
      print('It starts with an alphabet?', 'False')

is_one_word = len(name.strip(' ')) > 1 + int(name.find(' ')) == 0

if is_one_word:
      print('It is a single word?', 'True')
else:
      print ('It is a single word?', 'False')

is_valid_name = is_valid_length and is_valid_start and is_one_word

if is_valid_name:
      print('Larry: I can pronounce this name ---', 'True')
else:
      print('Larry: I can pronounce this name ---', 'False')

