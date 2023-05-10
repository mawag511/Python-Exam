"""
    Python Shop Program
    Exam -> Python Programming Language
    Maria Ginaldi
    18/04/2023

"""

import re
import os


# Classes of objects (items) sold in the shop
class Phone:
    def __init__(self, item_code, description, price):
        self.item_code = item_code
        self.description = description
        self.price = price

    def __repr__(self): 
        return "Phone % s -> Description: % s, Price: $% s" % (self.item_code, self.description, self.price) 

class Tablet:
    def __init__(self, item_code, description, price):
        self.item_code = item_code
        self.description = description
        self.price = price

    def __repr__(self): 
        return "Tablet % s -> Description: % s, Price: $% s" % (self.item_code, self.description, self.price) 

class Sim_Card:
    def __init__(self, item_code, description, price):
        self.item_code = item_code
        self.description = description
        self.price = price

    def __repr__(self): 
        return "SIM Card % s -> Description: % s, Price: $% s" % (self.item_code, self.description, self.price) 

class Case:
    def __init__(self, item_code, description, price):
        self.item_code = item_code
        self.description = description
        self.price = price

    def __repr__(self): 
        return "Case % s -> Description: % s, Price: $% s" % (self.item_code, self.description, self.price) 

class Charger:
    def __init__(self, item_code, description, price):
        self.item_code = item_code
        self.description = description
        self.price = price

    def __repr__(self): 
        return "Charger % s -> Description: % s, Price: $% s" % (self.item_code, self.description, self.price) 



item_info_holder, sim_info_holder, case_info_holder = [], [], []
charger_info_holder, cart_info_holder = [], []

clear = lambda: os.system('cls')


def main():

    print("\nWelcome to Python Shop! Please select what you're interested in buying\n")
    shop()


# shop
def shop():
    
    # phones and tablets storage
    item1 = Phone("BPCM", "Compact", 29.99)
    item2 = Phone("BPSH", "Clam shell", 49.99)
    item3 = Phone("RPSS", "Robo phone - 5inch screen, 64GB memory", 199.99)
    item4 = Phone("RPLL", "Robo phone - 6inch screen, 256GB memory", 499.99)
    item5 = Phone("YPLS", "Y-phone standard - 6inch screen, 64GB memory", 549.99)
    item6 = Phone("YPLL", "Y-phone deluxe - 6inch screen, 256GB memory", 649.99)
    item7 = Tablet("RTMS", "RoboTab - 8inch screen, 64GB memory", 149.99)
    item8 = Tablet("RTML", "RoboTab - 10inch screen, 128GB memory", 299.99)
    item9 = Tablet("YTML", "Y-tab standard - 10inch screen, 128GB memory", 499.99)
    item10 = Tablet("YTLL", "Y-tab deluxe- 10inch screen, 256GB memory", 599.99)

    phones = [item1, item2, item3, item4, item5, item6]
    tablets = [item7, item8, item9, item10]

    # sims storage
    sim1 = Sim_Card("SMNO", "Sim free (no SIM card)", 0.00)
    sim2 = Sim_Card("SMPG", "Pay as you go (with SIM card)", 9.99)

    # cases storage
    case1 = Case("CSST", "Standard", 0.00)
    case2 = Case("CSLX", "Luxury", 50.00)

    # chargers storage
    charger1 = Charger("CGCR", "Car", 19.99)
    charger2 = Charger("CGHM", "Home", 15.99)

    # displaying store items
    options = phones + tablets
    index = 0
    option_holder = []
    for option in options:
        index += 1
        print(str(index) + ")", option)
        option_holder.append(option)
    print("\n0) Checkout")

    choice = input("\nItem: ")

    try:
        # choosing item
        if 1 <= int(choice) <= 10:
            item_info_holder.append(option_holder[(int(choice)-1)])

            # choosing sim
            if 1 <= int(choice) <= 6:
                sim_validated = False
                print("\nPlease choose a SIM model:")
                print("1)" + str(sim1))
                print("2)" + str(sim2))
                while sim_validated is False:
                    sim_choice = input("Choice: ")
                    sim_choice = int(sim_choice)
                    if sim_choice == 1:
                        sim_info_holder.append(sim1)
                        sim_validated = True
                        break
                    elif sim_choice == 2:
                        sim_info_holder.append(sim2)
                        sim_validated = True
                        break
                    else:
                        print("Please select an existing option")

            # choosing case
            case_validated = False
            print("\nPlease choose a case:")
            print("1)" + str(case1))
            print("2)" + str(case2))
            while case_validated is False:
                case_choice = input("Choice: ")
                case_choice = int(case_choice)
                if case_choice == 1:
                    case_info_holder.append(case1)
                    case_validated = True
                    break
                elif case_choice == 2:
                    case_info_holder.append(case2)
                    case_validated = True
                    break
                else:
                    print("Please select an existing option")

            # choosing charger
            charger_validated = False
            print("\nPlease choose a charger:")
            print("1)" + str(charger1))
            print("2)" + str(charger2))
            print("3) Both")
            print("4) None")
            while charger_validated is False:
                charger_choice = input("Choice: ")
                charger_choice = int(charger_choice)
                if charger_choice == 1:
                    charger_info_holder.append(charger1)
                    charger_validated = True
                    break
                elif charger_choice == 2:
                    charger_info_holder.append(charger2)
                    charger_validated = True
                    break
                elif charger_choice == 3:
                    charger_info_holder.append(charger1)
                    charger_info_holder.append(charger2)
                    charger_validated = True
                    break
                elif charger_choice == 4:
                    charger_validated = True
                    break
                else:
                    print("Please select an existing option")

            # back to shopping / checkout
            print("\nGo back to shopping? (Y/N)")
            go_back = input("Answer:")
            if go_back == "Y" or go_back == "y" or go_back == "yes" or go_back == "Yes":
                clear()
                shop()
            else:
                clear()
                cart()

        # checkout
        elif int(choice) == 0:
            clear()
            cart()

        else:
            print("Item does not exist")
            
    except:
        print("Something went wrong")


# cart
def cart():

    total_sum = []

    # summing the cost of items (with separation of duplicates and calculation of discounts)
    duplicate_check = []
    for item in item_info_holder:
        cost = re.findall(r"[-+]?\d*\.\d+|\d+", str(item)[-10:])
        duplicate_check.append(cost)

    final_item_list = []
    for item_list in duplicate_check:
        for item in item_list:
            final_item_list.append(item)

    duplicate, unique = [], []
    for item in final_item_list:
        if item not in unique:
            unique.append(item)
        else:
            duplicate.append(item)

    discounted, discount_list = [], []
    total_discount = 0

    for item in duplicate:
        discount = round(float(item) * 10 / 100, 2)
        discount_list.append(discount)
        discounted_price = float(item) - discount
        discounted.append(discounted_price)
        
    for number in discount_list:
        total_discount = total_discount + float(number)

    # summing the cost of sim cards
    for sim in sim_info_holder:
        cost = re.findall(r"[-+]?\d*\.\d+|\d+", str(sim)[-10:])
        total_sum.append(cost)


    # summing the cost of cases
    for case in case_info_holder:
        cost = re.findall(r"[-+]?\d*\.\d+|\d+", str(case)[-10:])
        total_sum.append(cost)


    # summing the cost of chargers
    for charger in charger_info_holder:
        cost = re.findall(r"[-+]?\d*\.\d+|\d+", str(charger)[-10:])
        total_sum.append(cost)


    # summing all of the above
    total_price_list = []
    for price_list in total_sum:
        for price in price_list:
            total_price_list.append(price)
    final_price = 0
    joined_price_list = total_price_list + unique + discounted
    for number in joined_price_list:
        final_price = final_price + float(number)


    # displaying results
    print("Receipt:")
    print("\n===============================\n")
    duplicate_holder = []
    for item in item_info_holder:
        if str(item) not in duplicate_holder:
            duplicate_holder.append(str(item))
            print(str(item))
        else:
           print(str(item) + " + (discount 10%)")
    for sim in sim_info_holder:
        print(str(sim))
    for case in case_info_holder:
        print(str(case))
    for charger in charger_info_holder:
        print(str(charger))
    if(len(discounted) > 0):
        print("\nTotal: $" + str(final_price))
        print("\nTotal discount: $" + str(total_discount))
    else:
        print("\nTotal: " + str(final_price))
    print("\n===============================")



if __name__ == "__main__":
    main()
