"""
    Exercise 2. Try rewriting the code below using map,
    reduce and filter. Filter takes a function and a
    collection. It returns a collection of every item
    for which the function returned True.

    people = [{'name': 'Mary', 'height': 160},
              {'name': 'Isla', 'height': 80},
              {'name': 'Sam'}]

    height_total = 0
    height_count = 0

    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        print(average_height)
        # => 120
"""
from functools import reduce
from operator import add

people = [
    {"name": "Mary", "height": 160},
    {"name": "Isla", "height": 80},
    {"name": "Sam"}
]

heights = map(lambda x: x["height"], filter(lambda x: "height" in x, people))

if len(heights) > 0:
    average_height = reduce(add, heights) / len(heights)
