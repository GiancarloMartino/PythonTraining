"""
This is a multi-line comment
You can use this kind of comment to
make longer notes as you are learning.
In python, these are often used as
docstrings.
"""

name = "Giancarlo Martino"
type_of_car = "Alfa Romeo"
school = "University of Life"

print(name + school)

print(name + " " + school)

print(name + " works at " + school + ".")

# python string.format()
print("{} works at {}.".format(name, school))

# python string format preferred version
print(f"{name} works at {school}.")
