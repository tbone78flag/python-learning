"""
Learning about Lists
(Compressed for learning purposes)
"""

favorite_food = ["sushi", "cheeseburgers", "ramen"]
print(favorite_food)

print(favorite_food[0]) #Starting at 0

#Learning to add, edit, delete from lists

print(len(favorite_food)) #len find the length

favorite_food.append("ice cream") #Adds to a list at the end
print(favorite_food)
print(len(favorite_food))

favorite_food.insert(1, "crab legs") #Adds to a list where specified
print(favorite_food)
print(len(favorite_food))

del(favorite_food[4]) #Deletes from a specified spot in the list
print(favorite_food)
print(len(favorite_food))