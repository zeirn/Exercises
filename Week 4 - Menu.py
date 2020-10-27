d = input('Which day are you interested in? ')  # I'm asking the user to input a day of the week.

# I made 2 dictionaries - weekdays and menu.
weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
menu = {1: 'Spaghetti bolognese', 2: 'Cheese Burger', 3: 'Chow mein', 4: 'Pizza', 5: 'Grilled Salmon'}

if d == weekdays[1]:  # If this statement is true,
    print('On Monday, we\'ll be serving', menu[1], '!')  # then the program will print this.

elif d == weekdays[2]:
    print('On Tuesday, we\'ll be serving', menu[2], '!')

elif d == weekdays[3]:
    print('On Wednesday, we\'ll be serving', menu[3], '!')

elif d == weekdays[4]:
    print('On Thursday, we\'ll be serving', menu[4], '!')

elif d == weekdays[5]:
    print('On Friday, we\'ll be serving', menu[5], '!')

elif d:
    print(weekdays.get(9, 'We\'re not open on that day!'))
