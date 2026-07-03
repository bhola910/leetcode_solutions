try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("That wasn't a valid number.")