food_list = [
    ['Milk', 'Sugar', 'Vanilla'],
    ['Wings', 'Buffalo Sauce', 'Spices'],
    ['Chicken', 'Rice', 'Onions']
    ]
['Ice Cream', 'Chicken Wings', "Chicken Fried Rice"]

#print("Which item:\n Ice Cream :1 , \n Chicken Wings: 2, \n Chicken Fried Rice: 3")
idx = 0
# while idx < len(food_list):
for food in food_list:
    print('Food #%s has the following ingredients: ' % idx)
    # for i in food_list[idx]:
    for i in food:
        print("    %s" % i)
    idx += 1

