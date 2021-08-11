def input_data():
    length = []
    width = []
    cost = []
    i = 0

    while i < 5:
        print('Enter length of room {} in ft: '.format(i+1), end = "")
        l = input()
        print('Enter width of room {} in ft: '.format(i+1), end = "")
        w = input()
        if l.isnumeric() and w.isnumeric():
            length.append(float(l))
            width.append(float(w))
        else: 
            print('Invalid option was entered!')
            length.append(0)
            width.append(0)
        print('Enter type of floor of room {}: '.format(i+1), end = "")
        t = input()
        t = t.strip()
        if t.lower() == 'hardwood':
            cost.append(1.39)
        elif t.lower() == 'carpet':
            cost.append(3.99)
        elif t.lower() == 'tile':
            cost.append(4.99)
        else:
            print('Invalid option was entered!')
            cost.append(0)
        i += 1
    return length, width, cost

length, width, cost = input_data()
total = 0
for i in range(5):
    print('The cost of flooring of room {} is Rs. {}.'.format(i+1, round(length[i]*width[i]*cost[i], 2)))
    total += length[i]*width[i]*cost[i]
print('The total cost of flooring of all rooms is Rs. {}.'.format(round(total,2)))


