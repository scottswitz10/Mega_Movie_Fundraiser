# import statments
import re
import pandas 


# functions go here

# checks the ticket nmame is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input (question)

        # if name is not blank, program continues
        if response != "":
            return response
        # if name is blank, show error (& repeat loop)
        else:
            print("sorry - write your name")


# checks for an integer more than 0
def int_check(question):

    error = "please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int (input(question))

            if response <=0:
                print (error)
            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)


# Checks user enters valid choice based on a list
def string_check(choice, options):
 
  for var_list in options:
 
    # if the snack is one of the lists, return the filter
    if choice in var_list:
 
      # get full name of snack and put it
      # in title case so it looks nice when outputted
      chosen = var_list[0].title()
      print(chosen)
      is_valid = "yes"
      break
 
    # if the chosen option is not valid, set is_valid to no
    else:
      is_valid = "no"
 
  # if the snack is not OK - ask question again.
  if is_valid == "yes":
    return chosen
  else:
    return "invalid choice"
 

def get_ticket_price():
# Get Ticket Price

    response = ""
    while response == "":
        age = int_check("age: ")

        # check that age is valid...
        if age < 12:
            print ("sorry you are too young for this movie")
            ticket_price = "invalid ticket price"
        elif age > 130:
            print("I don't think your that old - It looks like a mistake")
            ticket_price = "invalid ticket price"

        # get the price for the user's age
        elif age < 16:
            ticket_price = 7.5
        elif age <65:
            ticket_price = 10.5
        else:
            ticket_price = 6.5

        return ticket_price


def get_snacks(valid_snacks):

    # holds snack order for a single user
    snack_order = []

    number_regex = "^[1-9]"
    
    # aks user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snack? ").lower()
        check_snack = string_check(want_snack, yes_no)
        
        print("check snack", check_snack)
        
        # if they say yes, ask what snacks they want (and add to our snack list)
        if check_snack == "No":
            return []

        else:
        
            desired_snack = ""
            while desired_snack != "xxx" :

                snack_row = []

                # ask user for desired snack and put it in in lowercase
                desired_snack = input("snack: ").lower()

                if desired_snack == "xxx":
                    break

                # if item has a number, sperate into two (number )
                if re.match(number_regex, desired_snack):
                    amount = int(desired_snack[0])
                    desired_snack = desired_snack[1:]

                else:
                    amount = 1
                    desired_snack = desired_snack

                # remove white spaces around snack
                desired_snack = desired_snack.strip()

                # check if snack is valid
                snack_choice = string_check(desired_snack, valid_snacks)
                if snack_choice == "invalid choice":
                    print("Please enter a valid snack choice")

                #check snack amount is avlid (less than 5)
                if amount >= 5:
                    print ("sorry - we have a four snack maximum")
                    snack_choice = "invalid choice"

                    # add snack AND amount to list...
                    amount_snack = "{} {}". format(amount, snack_choice)

                # check that the snack is not an exit code before adding
                if snack_choice != "xxx" and snack_choice != "invalid choice":
                
                # create mini-list (amount and item)
                    snack_row.append(amount)
                    snack_row.append(snack_choice)

                    # add mini-list to master list
                    snack_order.append(snack_row)

        return snack_order



# main routine goes here

# ********** Main Routine **********
print("main routine has started")


number_regex = "^[1-9]"
 
# valid snacks hold lists of all snacks
# each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# , and possible abbreviations etc
valid_snacks = [
["popcorn", "p", "pop", "corn", "a"],
["M&M's", "m&m's", "mms", "m", "b"], # first item is M&M
["pita chips", "chips", "pc", "pita", "c"],
["water", "Fiji", "w", "d"],
["orange juice", "oj", "e"],
["oreo's", "o", "f"],
["xxx"]
]

# valid options for free / no questions
yes_no = [
  ["yes", "y"], ["no", "n"]
  ]


# ask user if they have used the program before & show instructions if necessary

# initiate loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []


#data frame dictionary
movie_data_dict = {
  'Name': all_names,
  'Ticket': all_tickets
}

profit = 0
count = 0
ticket_sales = 0


name = ""
# Get name and age
while name != "xxx" and count < MAX_TICKETS:

    # get name (cant be blank
    name = not_blank("name: ")

    # exit loop if name is 'xxx'
    if name.lower() == "xxx":
        break

    print()
    
    ticket_price = get_ticket_price()

    if ticket_price == "invalid ticket price":
        continue

    # Add name and ticket to lists...
    all_names.append(name)
    all_tickets.append(ticket_price)
    
    # get snacks for each person
    get_order = get_snacks(valid_snacks)
    print(get_order)

    # tells users how many seats are left
    if count < MAX_TICKETS - 1:
        print("you have {} seats left".format(MAX_TICKETS - count))

    # warns user that only one seat is left
    else:
        print("*** There is ONE seat left!! ***")

    # GET DETAILS...
    profit_made = ticket_price - 5
    profit += profit_made

    print("{} : ${:.2f}".format(name, ticket_price))


    # add sold ticket to count
    count += 1
 
    # End of tickets loop
    if count == MAX_TICKETS:
        print("you have sold all available tickets!")
    else:
        print(" you have sold {} ticket/s.  there are {} places still available".format(count, MAX_TICKETS - count))


# **** Printing area, done selling stuff ****
movie_fame = pandas.DataFrame(movie_data_dict)
print(movie_fame)

print()

# calculate total sales and profit
print("profit from tickets:  ${:.2f}".format(profit))

# out put data to text file


































































