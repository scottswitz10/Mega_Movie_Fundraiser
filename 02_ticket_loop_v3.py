# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name.lower() != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
    print("You have {} seats left".format(MAX_TICKETS - count))


    # Warns user that only one seat is left!
else:
    print("*** There is ONE seat left!! ***")

    # Get details...
    name = input("Name")

    if name.lower() == "xxx":
        break

    count += 1
    print()

    if count == MAX_TICKETS:
        print("You have sold all the available tickets!")
else:
    print("You have solid {} tickets.  \n"
          "There are {} places still available"
          .format(count, MAX_TICKETS - count))