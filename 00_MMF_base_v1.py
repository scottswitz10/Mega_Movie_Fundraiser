#  import statements


# functions go here

# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name blank, show error (& repeat loop)
        else:
            print("sorry - this can't be blank")


# ********** Main Routine **********

# set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # Get age (between 12 and 130

    # Calculate ticket price

    # Loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharde if necessary)


# Calculate Total sales and profit

# Out put data to text file

