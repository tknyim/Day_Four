my_num = 10
my_sec_num = 5

while my_num > 0:
    print("First num = %s" % my_num)
    my_num -= 2
    while my_sec_num <= 20:
        print("Second Numb %s" % my_sec_num)
        my_sec_num += 5
        #break
    print('Done with nested loop')
    my_sec_num = 5

print("When is this going to print?")