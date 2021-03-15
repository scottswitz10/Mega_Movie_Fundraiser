

#string checking functions, tasks input
# question and list of valid responses
def string_checker(question, to_check):

  error = "Please provide a valid response"
    
  valid = False
  while not valid:
         
      # ask question and put response in lowercase
      response = input(question).lower()

      if response in to_check:
        # checks if the response is the first letter of
        # an item in the list
        return response

      else:
        for item in to_check:
          if response == item[0]:
            # note: returns the entire response
            # rather than just the first letter
            return item

      print(error)

#main routine goes here

for item in range(0, 6):
    want_snacks = string_checker("Do you want snacks? ", ["yes", "no"])

    print("You chose", want_snacks)

