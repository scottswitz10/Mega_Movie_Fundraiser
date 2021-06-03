# Initialise snack lists...

names = ['Scott', 'Luke', 'Monty', 'Zav', 'Wyatt']
 
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice,]

snack_menu_dict = {
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
}

test_data =[
    [[2, ' Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Pita chips'], [1, 'Orange Juice']],
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
        to_find = (item[1])
        amount = (item[0])
        add_lists = snack_menu_dict[to_find]
        add_lists[-1] = amount


print()
print("Popcorn: ", snack_lists[0])
print("M&Ms:", snack_lists[1])
print("Pita Chips:", snack_lists[2])
print("Water:", snack_lists[3])
print("Orange Juice:", snack_lists[4])
    




































