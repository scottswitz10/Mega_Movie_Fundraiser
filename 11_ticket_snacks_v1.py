import pandas

# initialise snack lists

all_names = ['Scott', 'Luke', 'Monty', 'Zav', 'Wyatt']
all_tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

#data frame dictionary
movie_data_dict = {
    'name': all_names,
    'ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
}

# cost of each snack
price_dict = {
    'popcorn': 2.5,
    'water': 2,
    'pita chips': 4.5,
    'm&ms': 3,
    'orange juice': 3.25
}

test_data = [
    [[2, 'popcorn'], [1, 'pita chips'], [1, 'orange juice']],
    [[]],
    [[1, 'water']],
    [[1, 'popcorn'], [1, 'orange juice']],
    [[1, 'm&ms'], [1, 'pita chips'], [3, 'orange juice']]
]

count = 0
for client_order in test_data:

    # assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    # print (snack_lists)

    # get order (hard coded for easy testing)...
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict [to_find]
            add_list [-1] = amount

print ()

# create dataframe and set index to name column
movie_frame = pandas.DataFrame (movie_data_dict)
movie_frame = movie_frame.set_index ('name')

#create column called 'sub total'
#fill it price for snacks and ticket

movie_frame ["sub total"] = \
    movie_frame ['ticket'] + \
    movie_frame ['popcorn'] *price_dict ['popcorn'] + \
    movie_frame ['water'] *price_dict ['water'] + \
    movie_frame ['pita chips'] *price_dict ['pita chips'] + \
    movie_frame ['m&ms'] *price_dict ['m&ms'] + \
    movie_frame ['orange juice'] *price_dict ['orange juice']

# shorten column names
movie_frame = movie_frame.rename(columns={'orange juice': 'oj',
'pita chips': 'chips'})

print(movie_frame)