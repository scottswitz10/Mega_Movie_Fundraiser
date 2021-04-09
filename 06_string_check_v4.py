import re

# functions go here
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
  
# Valid snacks hold list of all snacks
# Each item in valid snacks is a list with
# Valid options for each snack <full name, full letter (a - e)
# , and possible abbreviations etc>

number_regex = "^[1-9]"

valid_snacks = [
 ["Popcorn", "p", "corn", "a"],
["M&M's", "m&m's", "mms", "m", "b"], # first item is M&M
 ["Pita Chips", "chips", "pc", "pita", "c"],
 ["Water", "w", "water", "d", "Aqua"]
]
 
yes_no = [
 ["yes", "y"],
 ["no", "n"] 
]
 

# holds snack order for all clients
snack_order = []

#ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snack? ").lower()
    check_snack = string_check(want_snack, yes_no)
    if check_snack == "invalid choice":
        print("Please enter yes / no")
 

#If they say yes, ask what snacks they want(and add to our snack list)
if check_snack == "Yes":
    desired_snack = ""
else:
    desired_snack = "xxx"

while desired_snack != "xxx":

    snack_row = []

    # ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ").lower()

    if desired_snack == "xxx":
      break

    if re.match(number_regex, desired_snack):
        amount = int(desired_snack[0])
        designed_snack = desired_snack[1:]

    else:
        amount = 1
        desired_snack = desired_snack

    # remove white space around snack
    desired_snack = desired_snack.string()

    # check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)

    # check snack amount is valid (less than 5)
    if amount >= 5:
        print("Sorry - we have a four snack maximum")
        snack_choice = "invalid choice"

    # add snack AND amount to list...
    amount_snack = "{} {}".format(amount, snack_choice)

    #check that snack is not the exit code before adding
    if snack_choice != "xxx" and snack_choice !="invalid choice"
    snack_order.append(amount_snack)

# Show snack open
print()
if len(snack_order) ==0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered:")

    for item in snack_order:
        print(item)






    # check if snack is valid 
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)

    # add snack to list...

    # check the snack is not the exit code before adding
    if snack_choice == "xxx":
      break
    elif snack_choice != "invalid choice":
      snack_order.append(snack_choice)
    else:
      print("Please enter a valid snack choice \n")

# show snack orders
print()

if len(snack_order) == 0:
  print("Snack Ordered: None")

else:
  print("Snack Ordered:")

for item in snack_order:
  print(item)


print()
print("you are done")