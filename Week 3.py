# This one's a doozie.
# These ask to input a value for these variables.
x = input("Input a maximum: ")  # Note to self: 'a' in the equation is 'x'.

x = int(x)  # Converts 'x' to an integer.


for c in range(0, x):  # This tells us that the maximum amount will be 'x', and the minimum 0.
    for x in range(0, x):
        for b in range(0, x):
            c = x + b
            c = int(c)
            print(x, c, b)




