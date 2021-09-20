# parsing json files
import json

with open("menu_items_source.json", mode='r') as f:
    data = json.load(f)


# print(data)

# checking the categories and printing them
def checking_categories():
    for cat in data:
        if cat["name"]:
            print("-->", cat["name"].upper())
        else:
            print("NO")


# checking whether menuitems is present or not in categories
def checking_menuitems_in_categories():
    for cat in data:
        print("---->\t\t", cat["name"].upper())
        print()
        if cat["menuItems"]:

            for items in cat["menuItems"]:
                print(">>", items["name"])

            print()
        else:
            print("Menu items are not present")
            print()


# checking whether there are subcategories in the categories
def checking_subcategories():
    for cat in data:
        print("---->\t", cat["name"].upper())
        print()
        if cat["subCategories"]:
            print("Sub-Categories ----> YES")
        else:
            print("Sub-Categories ----> NO")
        print()


# checking the menuitems in the subcategories
def subcategories_menuitems():
    for cat in data:
        print("---->\t", cat["name"].upper())
        print()
        if cat["subCategories"]:

            for item in cat["subCategories"]:
                print(">>", item["name"])

        else:
            print("NO Menuitems")
        print()


# printing an overview all the menuitems in the restaurent
def all_menuitems():
    for cat in data:
        print("---->\t", cat["name"].upper())
        print()
        if cat["menuItems"]:

            for item in cat["menuItems"]:
                print(">>", item["name"])
            print()

        for sub_cat in cat["subCategories"]:
            print("Sub ==>>", sub_cat["name"].upper())
            print()

            if sub_cat["menuItems"]:

                for items in sub_cat["menuItems"]:
                    print("->>", items["name"])
                print()

# checking the categories and printing them
# checking_categories()

# checking whether menuitems is present or not in categories
# checking_menuitems_in_categories()

# checking whether subcategories is present or not
# checking_subcategories()

# checking the subcategory menuitems
# subcategories_menuitems()

# printing an overview of all the items in the restaurent
# all_menuitems()