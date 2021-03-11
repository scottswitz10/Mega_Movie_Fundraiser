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


#checks for an integer more than 0
def int_check(question):

    error = "Please enter a whole number that is more than zero"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)


# ********** Main Routine **********

# set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# initialise loop so that it runs at least once
name = ""
ticket_count = 0
profit = 0
MAX_TICKETS = 5

while name.lower() != "xxx" and ticket_count < MAX_TICKETS:

    # Get details...
    name = not_blank("Name: ")

    if name.lower() == "xxx":
        break

    age = int_check("How old? ")

    if age < 12:
        print("sorry but you are too young for this movie")
        continue
    elif age > 130:
        print(
            "Sorry but you're too old for this movie - It looks like a mistake"
        )
        continue

    if age < 16:
      ticket_price = 7.5
    elif age <65:
      ticket_price = 10.5
    else:
        ticket_price = 6.5

    profit_made = ticket_price - 5
    profit += profit_made

    print("{} : $ {:.2f}" .format (name, ticket_price))

    print("profit from tickets: ${:.2f}".format (profit))

    ticket_count += 1
    print("Tickets sold: ", ticket_count)
    print()

    # tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    # Warns user that only one seat is left!
    elif ticket_count == MAX_TICKETS - 1:
        print("*** There is ONE seat left!! ***")

    # Loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharde if necessary)

# Calculate Total sales and profit
print("Ticket Profit: ${:.2f}".format(profit))

# Out put data to text file
