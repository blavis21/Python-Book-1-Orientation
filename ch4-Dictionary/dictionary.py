#  PRACTICE: Dictionary of Words
"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["testing"] = "this is me testing wtf is going on"
word_definitions["maybe"] = "idk if this is working"
word_definitions["hmm"] = "let's see"

"""
Use square bracket lookup to get the definition two
words and output them to the console with `print()`
"""
print(word_definitions["testing"])
print(word_definitions["maybe"])

"""
Loop over dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for key, value in word_definitions.items():
    print(f"The definition of {key} is {value}")


# PRACTICE: English Idioms
idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for key, value in idioms.items():
    val = " ".join(value)
    print(f'{key}: {val}')


# CHALLENGE: The Family Dictionary
my_family = {
    "sister": {
        "name": "Sarah",
        "age": 43
    },
    "mother": {
        "name": "Judy",
        "age": 76
    },
    "father": {
        "name": "Ray",
        "age": 79
    }
}

for fam_member, details in my_family.items():
    print(f'{details["name"]} is my {fam_member} and is {str(details["age"])} years old')
