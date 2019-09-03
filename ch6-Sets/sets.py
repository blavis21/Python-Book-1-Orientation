# #     Create an empty set named showroom.
# #     Add four of your favorite car model names to the set.
# showroom = {"skyline", "280z", "wrangler", "mustang", "skyline"}
# print(showroom)

# #     Print the length of your set.
# print(len(showroom))

# #     Pick one of the items in your show room and add it to the set again.
# #     Print your showroom. Notice how there's still only one instance of that model in there.
# #     Using update(), add two more car models to your showroom with another set.
# showroom.update({"civic", "integra"})
# print(showroom)

# #     You've sold one of your cars. Remove it from the set with the discard() method.
# showroom.discard("civic")
# print(showroom)

# # Acquiring more cars

# #     Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
# junkyard = {"taurus", "prelude", "camaro", "taurus", "f150", "f150", "mustang", "wrangler"}

# #     Use the intersection method to see which cars exist in both the showroom and that junkyard.
# cars_in_both = showroom.intersection(junkyard)
# print(cars_in_both)

# #     Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# combine = showroom.union(junkyard)
# print(combine)

# #     Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
# combine.discard("camaro")
# combine.discard("prelude")
# print(combine)


# ADVANCED CHALLENGE: Matching Make & Models
makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)

