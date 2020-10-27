x = input('How many days do you want to work out for? ')  # This is what we're asking the user.
x = int(x)

# These are our lists.
strength = ['Pushups', 'Squats', 'Chinups', 'Deadlifts', 'Kettlebell swings']
cardio = ['Running', 'Swimming', 'Biking', 'Jump rope']
workout = []

for d in range(0, x):  # This is so that 'd' (the day) stays within the range of 0 and whatever x is.
    # 'z' and 'z2' are the exercises in the lists.
    z = strength[d % len(strength)]  # The number of days divided by the length of the number of items in the
    z2 = cardio[d % len(cardio)]  # list strength/cardio. z is the answer to the first equation. z2 is answer to other.
    workout.append(z + ' and ' + z2)  # This adds these two answers to the end of the workout list.
    print('On day', d+1, (workout[d]))
