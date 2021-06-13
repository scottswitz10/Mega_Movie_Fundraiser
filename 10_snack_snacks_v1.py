import pandas

# Initialise snack lists...


#data frame dictionary

all_names = ['Scott', 'Luke', 'Monty', 'Zav', 'Wyatt']
all_tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
 
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
}


# snack_menu_dict = {
#     'Popcorn': popcorn,
#     'Water': water,
#     'Pita Chips': pita_chips,
#     'M&Ms': mms,
#     'Orange Juice': orange_juice
# }

price_dic = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}


test_data =[
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Pita Chips'], [1, 'Orange Juice']],
    [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0
for client_order in test_data:

    # Assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    # print(snack_lists)

    # get order(hard coded for easy testing)...
    snack_order = test_data[count]
    count += 1


    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_lists = movie_data_dict[to_find]
            add_lists[-1] = amount


# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)

movie_frame["Sub Total"] = \
    movie_frame['Ticket']