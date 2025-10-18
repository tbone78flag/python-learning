"""
Learning Booleans and IF statements
(Compressed for learning)
"""

day = 17 #Int (Integer)
weight = 190.4 #Float
month = 'October' #String

light_is_on = True #Boolean

#Going rouge with only IF statements
if light_is_on:
    print("The light is on!")
    light_is_on = False
else:
    print("It's pretty dark in here.")
    light_is_on = True

if light_is_on:
    print("*Click*")
    print("Thank you for turning the light on.")
    light_is_on = False
else:
    print("*Click*")
    print("Why'd you turn the light off!?")
    light_is_on = True

#Using IF Statements to compare

weight = 190
goal_weight = 185
weight_sub = weight - goal_weight

if weight < 200:
    print("Keep up the good work")
else:
    print("It's ok. Let's work on that.")

if weight != 185: #!= is not equal to
    print(f"You're weight is {weight} not {goal_weight} it is {weight_sub} lbs away from your goal.")
if weight == 190: #== is equal to
    print(f"You are currently at {weight} lbs which is only {weight_sub} lbs from your goal weight of {goal_weight} lbs.")
#<= is equal to or less than and >= is equal to or greater than

"""
Challenge: Answering if a number is odd
"""
def your_code():
    number = 7

    result = number % 2 #Using a modulo to check if there is a remainder of 1

    if result == 0:
        return
    else: 
        return True
        
    return False