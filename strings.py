"""
Learning Basic Strings
Compressed for space while learning
"""
age = 29
shirt = 'black' #Utilizing single quotes
store = "Arby's" #Utlizing double quotes
quote = 'Arby\'s, "we have the meats"' #Utlizing backslash for single and double quotes

print(shirt)
print(store)
print(quote)

movie = 'The Bob\'s Burgers Movie'
print("The last movie I watched = ", movie)

"""
Using strings in variables
"""
day = 17
temp = 49
month = 'October'

print("Without using variables: Today is October 17th and it is currently 49 degrees outside.") #Without using variables
print(f"With using variables: Today is {month} {day}th and it is currently {temp} degrees outside.") #With using variables (allows for customizing efficiently.)

day_name = 'Friday' #Good practice to use underscore between words in variable names.

print(f"Today is {day_name}, {month} {day}th and it is currently {temp} degrees outside.")