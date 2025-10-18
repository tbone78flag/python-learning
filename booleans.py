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
