import re 



# Function goes here
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
        