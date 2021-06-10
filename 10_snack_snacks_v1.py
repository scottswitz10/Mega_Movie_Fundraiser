import pandas

# Initialise snack lists...


#data frame dictionary

all_names = ['Scott', 'Luke', 'Monty', 'Zav', 'Wyatt']
all_tickets = []

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
 
snack_lists = [popcorn, mms, pita_chips, water]

snack_menu_dict = {
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms
}

movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
}

test_data =[
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Pita chips'], [1, 'Orange Juice']],
    [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0
for client_order in test_data:

    # Assume no snacks have been bought...
    for item in test_data:
        item.append(0)

    # print(snack_lists)

    # get order(hard coded for easy testing)...
    snack_order = test_data[count]
    count += 1


for item in snack_order:
    if len(item) > 0:
        to_find = (item[1])
        amount = (item[0])
        add_lists = snack_menu_dict[to_find]
        add_lists[-1] = amount


print()
print("Names:", all_names)
print("Popcorn: ", snack_lists[0])
print("M&M's:", snack_lists[1])
print("Pita Chips:", snack_lists[2])
print("Water:", snack_lists[3])
print("Orange Juice:", snack_lists[4])

# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)