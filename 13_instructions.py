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

# Functions to show instructions if necessary
def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions? ").lower
        show_help = string_check(show_help, options)


    if show_help == "Yes":
        print()
        print("**** Mega Movie Fundraiser Instructions ****")
        print()
        print("Instructions go here. They are brief but helpful")

    return ""
def currency(x):
    return "${:.2f}".format(x)


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
["M&Ms", "m&m's", "mms", "m", "b"], # first item is M&M
["pita chips", "chips", "pc", "pita", "c"],
["water", "w", "d"],
["orange juice", "oj", "e"],
["xxx"]
]

# valid options for free / no questions
yes_no = [
  ["yes", "y"], 
  ["no", "n"]
  ]

#list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
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

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice,]

surcharge_mult_list= []

# Lists to store summary data...
summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]
summary_data = []

#data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Ticket': all_tickets,
    'Surcharge_Multiplier': surcharge_mult_list
}

# Summary Dictionary
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# cost of each snack 
price_dict = {
    'Popcorn': 2.5, 
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3, 
    'Orange Juice': 3.25
}

#Ask

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

    ticket_count += 1
    ticket_sales += ticket_price

    # Add name and ticket to lists...
    all_names.append(name)
    all_tickets.append(ticket_price)
    
    # Get snacks
    snack_order = get_snacks(valid_snacks)

    # get snacks for each person
    # get_order = get_snacks(valid_snacks)
    # print(get_order)

    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict [to_find]
            add_list [-1] = amount

    # Get payment method and apply surcharge if necessary
    # Ask for payment method 
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash /credit)?") . lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multipier = 0.05
    else:
        surcharge_multipier = 0

    surcharge_mult_list.append(surcharge_multipier)

    # 

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




print("all_names", all_names)
print("popcorn", popcorn)
print("water", water)
print("pita_chips", pita_chips)
print("mms", mms)
print("orange_juice", orange_juice)
print("all_tickets", all_tickets)

# **** Printing area, done selling stuff ****
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)

movie_frame ["Snacks"] = \
    movie_frame ['Popcorn']*price_dict['Popcorn'] + \
    movie_frame ['Water']*price_dict['Water'] + \
    movie_frame ['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame ['M&Ms']*price_dict['M&Ms'] + \
    movie_frame ['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame["Surcharge"]=\
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# shorten column names
movie_frame = movie_frame.rename(columns={'orange juice': 'oj',
'pita chips': 'chips', 'Surcharge_Multiplier': 'SM'})

# Set up Summary dataframe
# populate snack items...
for item in snack_lists:
    # sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2

# Calculate ticket profit & total profit
ticket_profit = ticket_sales - (5 * ticket_count)
total_profit = snack_profit + ticket_profit

# format dollar amounts and add to list...
dollar_amounts = [snack_profit, ticket_profit, total_profit]
for item in dollar_amounts:
    item = "${:.2f}".format(item)
    summary_data.append(item)


# Create summary frame 
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# Set up columns to be printed
pandas.set_option('display.max_columns', None)

# *** Pre Printing / Export ***
# Format currency values so they have $'s

# Ticket Details Formatting (uses currency function)
add_dollars = ['Ticket', 'Snacks', 'Surcharge', 'Total', 'Sub Total']
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

# Write each frame to a serperate cvs files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")

print()
print("*** Ticket / Snack Information ***")
print("Note: for full details, please see the excel file called")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total',
                    'Surcharge', 'Total']])

print()
print()

print("*** Snack / profit Summary ****")
print()
print(summary_frame)

# Tell useer if they have unsold tickets...
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("you have sold {} tickets. \n"
        "There are {} places still available"
        .format(ticket_count, MAX_TICKETS - ticket_count))


print_all = input("print all columns?? (y) for yes ")
if print_all =="y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total',
                        'Surcharge', 'Total']])

print()

# calculate total sales and profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("profit from tickets:  ${:.2f}".format(profit))

# Tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")

# out put data to text file
