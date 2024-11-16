"""
11.1 Create a file called zoo.py. In it, define a function called hours() that prints the string 'Open 9-5 daily'.
Then, use the interactive interpreter to import the zoo module and call its hours() function.

11.2 In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
"""

import zoo
print("This is the 11.1 exercise")
zoo.hours()

import zoo as menagerie

print(f"\nThis is the 11.2 exercise")
menagerie.hours()

