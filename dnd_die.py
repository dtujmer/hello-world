import random

print "Which die do you use? Can be 20, 12, 8, or any other number."
x = int(raw_input(">>> "))
print "The die has been cast and the result is\n\n"
print random.randint(1, x - 1)

y = raw_input("Press enter to continue or type some stuff to exit app.\n>>>")

while y == "":
    print random.randint(1, x - 1), "\n"
    y = raw_input(">>> ")
