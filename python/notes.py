"""
    Unfunctional vs Function
"""

""" Unfunctional function """

a = 0
def increment1():
    global a
    a + a = 1

""" Functional Program """

def increment2(a):
    return a + 1

"""
    Don't iterate over lists. Use map
    and reduce.
"""

name_lengths = map(len, ["Mary", "Isla", "Sam"])

print(name_lengths)
# => [4, 4, 4]

squares = map(lambda x: x * x, [0, 1, 2, 3, 4])

print(squares)
# => [0, 1, 4, 9, 16]

"""
    Unfunctional vs Functional use of map

    map(func, seq)
"""

""" Unfunctional """

import(random)

names = ["Mary", "Isla", "Sam"]
code_names = ["Mr. Pink", "Mr. Orange", "Mr. Blonde"]

for i in range(len(names)):
    names[i] = random.choice(code_names)

print(names)
# => ["Mr. Blonde", "Mr. Blonde", "Mr. Blonde"]

""" Functional """

names = ["Mary", "Isla", "Sam"]

secret_names = map(lambda x: random.choice(["Mr. Pink", "Mr. Orange", "Mr. Blonde"]), names)

"""
    Reduce

    reduce(func, seq)
"""
from functools import reduce

sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])

print(sum)
# => 10

""" Unfunctional """

sentences = ["Mary read a story to Sam and Isla.",
             "Isla cuddled Sam.,
             "Sam chortled."]

sam_count = 0
for sentence in sentences:
    sam_count = sam_count + sentence.cont("Sam")

print(sam_count)
# => 3

""" Functional (using reduce) """

sentences = ["Mary read a story to Sam and Isla.",
             "Isla cuddled Sam.,
             "Sam chortled."]

sam_count = reduce(lambda a, x: a + x.count("Sam"), sentences, 0)
