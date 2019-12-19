import json
import os

####################################
### print, concat.               ###
####################################


# print('sam')
# print('hello world')

# print('hello'+' '+'world')

# h = 'hello'
# w = 'world today'

# print('{} {}'.format(h,w))

# # PRINT YOUR NAME WHERE FIRST NAME AND LAST NAME ARE VARIABLES

####################################
### if, else.                    ###
####################################

# weather = 'rainy and stormy'


# if weather == 'sunny':
#         print('today will be good')
# elif weather == 'snowy':
#         print('today will be fun')
# else:
#         print('today may be slow')

# name = 'samuel'

# if len(name) > 3:
# 	print('YOUR NAME IS TOO LONG, SORRY!')
# else:
# 	print(name)


# WRITE AN IF STATEMENT WHERE
# IF YOUR NAME HAS MORE THAN 3 LETTERS IT PRINTS 'YOUR NAME IS TOO LONG, SORRY!'
# ELSE IT PRINTS YOUR NAME


####################################
### if, else, functions.         ###
####################################

# def today(weather):
#     if weather == 'sunny':
#             print('today will be good')
#     elif weather == 'snowy':
#             print('today will be fun')
#     else:
#             print('today may be slow')


# weather_today = 'rainy'

# today(weather_today)


# # WRITE A VARIABLE THAT IS YOUR (my_name) NAME AND ONE THAT IS YOUR AGE (my_age)
# # CREATE A FUNCTION THAT WILL PRINT YOUR NAME IF YOU PARSE IT WITH YOUR CORRECT AGE




# my_age = 26
# my_name = 'Sam'

# def naming(age=26):
# 	new_age = 20
# 	if age == my_age:
# 		print(my_name)

# naming()
# print(new_age)


####################################
### list indicies.             ###
####################################

weather_array = ['snowy', 'sunny', 'rainy']

# print(weather_array)

# print(weather_array[1])

# weather_array.append('cloudy')

# print(weather_array)

# name_array = ['sam', 'mike', 'amy', 'ubaldo']

# print(name_array)


# # CREATE AN ARRAY WITH PEOPLES NAMES

####################################
### list methods0.  .            ###
####################################

# print(weather_array)

# weather_array.clear()



# count = weather_array.count('snowy')
# print(count)

# snowy_index = weather_array.index('rainy')
# print(snowy_index)

# weather_array.pop()
# print(weather_array)
# weather_array.pop()

# weather_array.remove('snowy')

# print(weather_array)

####################################
### for loop.                    ###
####################################

# print(len(weather_array))

# print(range(5))

# for i in range(len(weather_array)):
# 	print(weather_array[i])

# for i in weather_array:
# 	print(i)


# # CREATE A FUNCTION THAT WILL PRINT EVERYONE'S NAME IF YOU PARSE IT WITH YOUR CORRECT AGE


####################################
### dictionaries.                ###
####################################

weather_dictionary = {'snowy': 'today will be fun', 'sunny': 'today will be good', 'rainy': 'today may be slow'}

weather_dictionary['misty'] = 'today will be hard to see'

# print(weather_dictionary)

weather_dictionary['snowy'] = 'today will be awesome'

# print(weather_dictionary)

# print(weather_dictionary['snowy'])

# for i in weather_dictionary:
	# print(i)
	# print(weather_dictionary[i])
	# print('if the weather today is {}, then {}'.format(i, weather_dictionary[i]))

# # as an function

def today_dict(weather_dict):
	for i in weather_dict:
		print('if the weather today is {}, then {}'.format(i, weather_dict[i]))

# today_dict(weather_dictionary)

# # CREATE A DICTIONARY WITH PEOPLES NAMES AS THE KEY AND THEIR AGE AS THE VALUE
# # CREATE A FUNCTION THAT WILL PRINT SOMEONE'S NAME IF THE AGE IS THE MORE THAN YOURS

# people_dict = {'sam': 26, 'ubaldo': 76}

# def name_game():
# 	for i in people_dict:
# 		if people_dict[i] > 26:
# 			print(i)

# name_game()

# print(people_dict)
# from json import loads

####################################
### with.                        ###
####################################

weather_file = 'weather.json'

with open(weather_file, 'r') as f:
	weather_dictionary_from_json = json.loads(f.read())

# print(weather_dictionary_from_json)

# weather_array = []

# print(weather_array)

# for i in weather_dictionary_from_json:
# 	print(i)
# 	weather_array.append(i)

# print(weather_array)

# today_dict(weather_dictionary_from_json)

####################################
### creds file.                  ###
####################################

# CREATE A CREDS.JSON FILE USED TO ACCESS EMBED
# import os

name = 'lookerembed'
cred_file = os.path.join(os.path.expanduser('~'),'.creds','creds.json')

# print(cred_file)

with open(cred_file, 'r') as f:
  data = json.loads(f.read())

# print(data)

print(data['lookerembed']['client_secret'])

# secret = data['{}'.format(name)]['client_secret']

# print(secret)

with open('data/users.json', 'r') as f:
        data = json.loads(f.read())

user_array = []
for i in data:
	user_array.append(i)

print(user_array)




####################################
### nested dictionaries.         ###
####################################

# day_outcome
# is_work_closed
# chance_of_moaning

# nested_weather_dictionary = {"snowy":{"day_outcome": "today will be fun", "is_work_closed": "yes", "chance_of_moaning": 0.3},
# "sunny":{"day_outcome": "today will be good", "is_work_closed": "no", "chance_of_moaning": 0},
# "rainy":{"day_outcome": "today may be slow", "is_work_closed": "no", "chance_of_moaning": 0.9}}

# print(nested_weather_dictionary['snowy']['chance_of_moaning'])

# for i in nested_weather_dictionary:
# 	print("today is {}, so there is a {}% chance of someone at work moaning".format(i,nested_weather_dictionary[i]['chance_of_moaning']))
# 	if nested_weather_dictionary[i]['is_work_closed'] == 'yes':
# 		print("but wait, work is closed!!".format(i))
# 	print(nested_weather_dictionary[i]['day_outcome'])
# 	print("")


# EXCERCISES

# CREATE A NESTED DICTIONARY (JSON FILE) THAT HOLDS USER INFORMATION THAT YOUR PBL DEMO WILL USE

# CREATE AN BLANK ARRAY
# FILL THE ARRAY WITH THE USERS



