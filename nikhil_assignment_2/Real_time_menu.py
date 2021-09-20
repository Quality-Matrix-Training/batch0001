def menu_categories():
    import json

    f = open("menu.json", "r")
    q = json.load(f)

    for i in range(0, len(q)):
        print(q[i].get('name'))  # To avoid key errors.

    f.close()


def menu_items_present_or_not():
    import json

    d = {}

    f = open("menu.json", "r")

    q = json.load(f)

    # print(data[0])

    for i in range(0, len(q)):
        if q[i]['menuItems'] != None:
            d[q[i]['name']] = "yes"
        else:
            d[q[i]['name']] = 'no'

    print(d)

    f.close()


def sub_categories_present_or_not():
    '''
    Watch carefully for None value it can be 0/ False/ None/ []....and mention the appropriate
    term or symbol.

    '''

    import json

    d = {}

    f = open("menu.json", "r")

    q = json.load(f)

    for i in range(0, len(q)):
        if q[i]['subCategories'] != []:
            d[q[i]['name']] = "yes"
        else:
            d[q[i]['name']] = 'no'

    print(d)

    f.close()


def menu_categories_and_items():
    import json

    f = open("menu.json", "r")

    d = {}

    data = json.load(f)

    for i in range(0, len(data)):
        e = data[i]['menuItems']
        if e != None:
            for j in range(0, len(e)):
                if data[i]['name'] not in d:
                    d[data[i]['name']] = [e[j]['name']]

                else:
                    d[data[i]['name']].append(e[j]['name'])

    # print(data[5]['menuItems'][3]['name'])

    print(d)
    f.close()


def sub_categories_and_items():
    import json

    d1 = {}
    d2 = {}

    f = open("menu.json", "r")

    q = json.load(f)

    for i in range(0, len(q)):
        e = q[i]['subCategories']
        if e != []:
            for j in range(0, len(e)):
                e1 = e[j]['menuItems']
                if e1 != None:
                    for k in range(0, len(e1)):
                        if e[j]['name'] not in d1:
                            d1[e[j]['name']] = [e1[k]['name']]
                        else:
                            d1[e[j]['name']].append(e1[k]['name'])

    # print(q[3]['subCategories'][1]['menuItems'][1]['name'])

    print(d1)
    f.close()


def overview_of_menu():
    import json

    d1 = {}
    d2 = {}
    d3 = {}

    f = open("menu.json", "r")

    q = json.load(f)

    for i in range(0, len(q)):
        e = q[i]['subCategories']
        if e != []:
            for j in range(0, len(e)):
                e1 = e[j]['menuItems']
                if e1 != None:
                    for k in range(0, len(e1)):
                        if e[j]['name'] not in d1:
                            d1[e[j]['name']] = [e1[k]['name']]

                        else:
                            d1[e[j]['name']].append(e1[k]['name'])

    for i in range(0, len(q)):
        s1 = q[i]['subCategories']
        if s1 != []:
            for j in range(0, len(s1)):
                if q[i]['name'] not in d2:
                    d2[q[i]['name']] = [s1[j]['name']]

                else:
                    d2[q[i]['name']].append(s1[j]['name'])

    # print(q[3]['subCategories'][1]['menuItems'][1]['name'])

    # print(d1)
    # print()
    # print(d2)

    for i in d2:
        s1 = d2[i]
        print(i.upper())
        print('-' * 9)
        for j in range(0, len(s1)):
            print(s1[j])
            if s1[j] in d1:
                print('--->', end='')
                print(d1[s1[j]])
                print()

    f.close()


'''
Uncomment each one of the following to get the answer for the queries.

'''

# menu_categories()

# menu_items_present_or_not()

# sub_categories_present_or_not()

# menu_categories_and_items()

# sub_categories_and_items()

# overview_of_menu()