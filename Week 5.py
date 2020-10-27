cities = open('cities.txt', 'r', encoding='latin_1')  # This opens the cities.txt file.
cities.readline()

x = input('Enter the city you\'re looking for: ')
x = str(x)
# In File: IF
IF = False

# Here, I'm splitting each of the rows in the file, and giving them specific values.
for row_num, line in enumerate(cities):
    values = line.strip().split('\t')  # This splits each line at the tabs.
    LatDeg = values[0].split('°')[0]  # This selects value 0, the latitude, then splits it at the '°'. Then, it selects
    LonDeg = values[1].split("°")[0]  # the first element of THAT split value, 0, which is the first two numbers - AKA
    LatMin = values[0].split("°")[1][0:2]  # the degree. Then, for the second one selects the second value, 1,
    LonMin = values[1].split('°')[1][0:2]  # longitude, and does basically the same thing.
    LatDir = values[0].split('°')[1][2:3]  # For the Minutes and Directions, we have to specifically split them, so we
    LonDir = values[1].split('°')[1][2:3]  # use [num:num] to split them to our needs.
    # In this case, it splits the minutes (the first two numbers) from the direction (the letter of the direction).
    city = values[2]  # This declares that city is the third value, 2 (because it starts at 0).

# If a city in the file is inputted, the code will detect it and print this out accordingly.
    if city == x:
        IF = True
        print(x, 'is', LatDeg, 'degrees', LatMin, 'minutes', LonDir, 'and', LonDeg, 'degrees', LonMin, 'minutes', LonDir)

# If it's not in the file, this will print.
# Can also be written as 'if IF == False:'
if not IF:
    print('City not found!')

cities.close()

