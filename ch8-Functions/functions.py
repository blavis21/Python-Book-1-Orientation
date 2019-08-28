# PRACTICE: Activities for Kids
running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]


def run(kids):
    for name in kids:
        print(f"{name} ran like a fool!")


def swing(kids):
    for name in kids:
        print(f'{name} had fun on the swings!')


def slide(kids):
    for name in kids:
        print(f'{name} slid down the slide!')


def hide(kids):
    for name in kids:
        print(f'{name} played hide and seek!')


run(running_kids)
swing(swinging_kids)
slide(sliding_kids)
hide(hiding_kids)


# PRACTICE: ChickenMonkey
# for num in range(1, 100):
#     if num % 5 == 0 and num % 7 == 0:
#         print("ChickenMonkey")
#     elif num % 5 == 0:
#         print("Chicken")
#     elif num % 7 == 0:
#         print("Monkey")
#     else:
#         print(num)
