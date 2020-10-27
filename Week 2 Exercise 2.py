# I made the computer ask the user for three separate numbers.
x = input('Give me a number. ')
y = input('Give me another number. ')
z = input('Give me one more number. ')

x = int(x)
y = int(y)
z = int(z)

if y < x and z < x:
    print(int(x), 'is the largest!')  # If x is the largest, then the computer will tell us.
elif z < y:
    print(int(y), 'is the largest!')  # If y is the largest, it will tell us.
else:
    print(int(z), 'is the largest!')  # If neither x or y are the largest, then z has to be.
