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


def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
                    "and {}".format(low_num, high_num)

    valid = False
    while not valid:

                # ask user for number and check it is valid
                try:
                    response = int(input(question))

                    if low_num <= response <= high_num:
                        return response
                    else:
                        print(error)

                # if an integer is not entered, display an error
                except ValueError:
                    print(error)

# ********** Main Routine **********

# set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name.lower() != "xxx" and count < MAX_TICKETS:

    # Get details...
    name = not_blank("Name: ")

    if name.lower() == "xxx":
        break

    age = int_check("How old? ", 11, 131)

    count += 1
    print()

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats left".format(MAX_TICKETS - count))

    # Warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

    if count == MAX_TICKETS:
        print("You have sold all the available tickets!")

    else:
        print("You have sold {} ticket/s.  \n"
              "There are {} place/s still available".format(count, MAX_TICKETS - count))

    # Get name (can't be blank)


    # Get age (between 11 and 131

    # Calculate ticket price

    # Loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharde if necessary)


# Calculate Total sales and profit

# Out put data to text file

