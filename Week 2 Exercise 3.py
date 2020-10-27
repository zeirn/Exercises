# In these columns, I'm asking the user to give me inputs on these questions.
P0 = input('Give me a value for P0. ')
r = input('Input an annual interest rate. ')
n = input('Input the compounding frequency. ')
t = input("What's the total number of years? ")
# These are here to tell the program that these letters are numbers.
t = int(t)
n = int(n)
r = float(r)
P0 = int(P0)

#t = 1  # This tells us that the t is equal to one.
while t < 6:  # This is here to make sure we get five results.
    P = P0 * (1 + (r / n)) ** (n * t)  # This is our equation!
    print(f"After year {t}, the amount in the account is: {P:.2f}")  # This gives us the text when we get out results.
    t = t + 1  # This is here to make sure that t doesn't always come out the same.
