zoo = ("lizard", "fox", "giraffe", "goat", "red panda", "flamingo", "monkey", "elephant", "kangaroo", "Joe")

fav_animal = zoo.index("fox") # OR fav_animal = zoo[1] displays fox
print(fav_animal) 

find_animal = "goat"
if find_animal in zoo:
    print("find animal:", find_animal)
    
(lizard, fox, giraffe, goat, red_panda, flamingo, monkey, elephant, kangaroo, Joe) = zoo

print(lizard)
print(fox)
print(giraffe)
print(goat)
print(red_panda)
print(flamingo)
print(monkey)
print(elephant)
print(kangaroo)
print(Joe)

zoo_list = list(zoo)

zoo_list.extend(["beaver", "antelope", "gazelle"])
print(zoo_list)

zoo_tuple = tuple(zoo_list)
print(zoo_tuple)