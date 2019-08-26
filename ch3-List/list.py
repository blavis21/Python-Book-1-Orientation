# PRACTICE: Random Numbers
# import random

# my_randoms = list()
# for i in range(10):
#     my_randoms.append(random.randrange(1, 6, 1))

# for number in range(1, 6):
#     if number in my_randoms:
#         print(f"my_randoms contains{number}")
#     else:
#         print(f"my_randoms does not contain {number}")
    

#  PRACTICE: Planet List
planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Jupiter", "Saturn"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

print(planet_list)

rocky_planets = slice(4)
print(planet_list[rocky_planets])

rocky_planets = planet_list[0:4]
print(rocky_planets)

del planet_list[8]
print(planet_list)