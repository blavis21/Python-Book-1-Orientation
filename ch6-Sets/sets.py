#     Create an empty set named showroom.
#     Add four of your favorite car model names to the set.
showroom = {"skyline", "280z", "wrangler", "mustang", "skyline"}
print(showroom)

#     Print the length of your set.
print(len(showroom))

#     Pick one of the items in your show room and add it to the set again.
#     Print your showroom. Notice how there's still only one instance of that model in there.
#     Using update(), add two more car models to your showroom with another set.
showroom.update({"civic", "integra"})
print(showroom)

#     You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("civic")
print(showroom)

# Acquiring more cars

#     Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"taurus", "prelude", "camaro", "taurus", "f150", "f150", "mustang", "wrangler"}

#     Use the intersection method to see which cars exist in both the showroom and that junkyard.
cars_in_both = showroom.intersection(junkyard)
print(cars_in_both)

#     Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
combine = showroom.union(junkyard)
print(combine)

#     Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
combine.discard("camaro")
combine.discard("prelude")
print(combine)
