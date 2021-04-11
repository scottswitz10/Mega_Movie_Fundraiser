import re 
 
# function goes here
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
 
# regular expression to find if the item starts with a number
number_regex = "^[1-9]"

# valid snacks hold lists of all snacks
# each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# , and possible abbreviations etc
valid_snacks = [
["popcorn", "p", "corn", "a"],
["M&M's", "m&m's", "mms", "m", "b"], # first item is M&M
["pita chips", "chips", "pc", "pita", "c"],
["water", "fiji water", "fiji", "w", "d"],
["xxx"]
]

# valid options for free / no questions
yes_no = [
["yes", "y"],
["no", "n"]
]

# holds snack order for a single user
snack_order = []
 
# aks user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
 want_snack = input("Do you want to order snack? ").lower()
 check_snack = string_check(want_snack, yes_no)
 
print("check snack", check_snack)
 
# if they say yes, ask what snacks they want (and add to our snack list)
if check_snack == "Yes":
 
  desired_snack = ""
  while desired_snack != "xxx" :
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

    #check snack amount is avlid (less than 5)
    if amount >= 5:
      print ("sorry - we have a four snack maximum")
      snack_choice = "invalid choice"

    # add snack AND amount to list...
    amount_snack = "{} {}". format(amount, snack_choice)

    # check that the snack is not an exit code before adding
    if snack_choice != "xxx" and snack_choice != "invalid choice":
      snack_order.append(amount_snack)

# show snack oreders
print()
if len(snack_order) == 0:
    print("snacks oredered: none")

else:
  print("snacks ordred:")
 
for item in snack_order:
     print(item)
 
print ("you are done")










