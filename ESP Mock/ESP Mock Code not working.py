houses = [['LONDON','Terraced', 3, 735000], ['CARDIFF', 'Semi-Detached', 2, 100000], ['LEEDS','Terraced', 3, 245000],['LONDON','Semi-Detatched', 1, 240000]]
sales = []
ourregions = ['LONDON', 'LEEDS', 'CARDIFF', 'BRISTOL']    
property_types =  ['TERRACED', 'SEMI-DETATCHED','DETATCHED']

def add_property():
    location = input("what property location would you like to put for sale?\n1: LONDON\n2: LEEDS\n3: CARDIFF\n4: BRISTOL\n\n")
    if location == "1":
        location = "LONDON"
    elif location == "2":
        location = "LEEDS"
    elif location == "3":
        location = "CARDIFF"
    elif location == "4":
        location = "BRISTOL"
    else:
        print("enter a valid location")
        add_property()
    
    houseType = input("is the property \n1: Terraced\n2: Semi-detached\n     or\n3:detatched\n\n")
    if houseType == "1":
        houseType = "terraced"
    elif houseType == "2":
        houseType = "Semi-Detached"
    elif houseType == "3":
        houseType = "Detached"
    else:
        print("enter a valid house type")
        add_property()
        
    bedrooms = input("how many bedrooms does the house have?")
    cost = input("how much does the house cost in  the format 'XXXXXX'")

    print("the house is located in", location, "is", houseType, "has", bedrooms, "bedrooms and is selling for",cost)
    check = input("Y or N")

    newHouse = [location, houseType, bedrooms, cost]
    
    if check == "Y" or check == "y":
        houses.append(newHouse)
        print(houses)
    elif check == "N" or check == "n":
        add_property()
    else:
        print("input Y or N")

    
    
    

def return_stock():
    print("CURRENT HOUSES FOR SALE \n\n REGION - HOUSE TYPE - BEDROOMS - COST")
    for i in houses:
        print (i)

def unique_regions():
    unique_list = []
    existing_regions = [item[0] for item in houses]
    for x in existing_regions:
        if x in unique_list:       
            unique_list.append(x)
    print(unique_list)


def region_search():
    print("Available Regions")
    unique_regions()
    r_check = False

    while not r_check:
        region_select= input("Please enter region: ").capitalize()

        for x in houses:
            if region_select.upper() == x[0].upper():
                r_check = True
                if x[0] == region_select.upper():
                    print(x)

        if r_check == False:
            print("Entered region is not valid")



def show_sales():
    if len(sales) > 0:    
        print("Forename  Surname Property cost  Total")
        for i in sales:
            print(i)
    else:
        print('no sales')


def house_sale():
    count = 0
    sale = []
    customer_forename = input('Please enter customer forename:')
    customer_surname = input('Please enter customer surname:')
    for i, item in enumerate(houses, 1):
        count = count + 1
        print(i, item)
        next
    
    sel_check = False
    while sel_check != True:
        select = int(input('Please select a purchase'))
        if select > 0 and select < count:
            sel_check = True
        else:
            print('ERROR PLEASE ENTER A VALID PROPERTY')
            

    sub_total = houses[select-1][3]
    print(sub_total)
    total_fees = 0


    if sub_total > 100000:
        total_fees += 3000+(sub_total-100000) * 0.2
    else:
        total_fees += sub_total *0.3

    

    final_total = sub_total+total_fees
    sale.append(customer_forename)
    sale.append(customer_surname)
    sale.append(sub_total)
    sale.append(final_total)
    sales.append(sale)

    print('Customer Receipt\n\n  FORENAME:{}  SURNAME: {}  PROPERTY COST:  {}  WITH STAMP DUTY:   {}'.format(*sales[-1]))
    print('\nTRANSACTION COMPLETE - PROPERTY REMOVED FROM SALES DATABASE\n')
    print (houses[select])
    del houses[select] 


while True:
    menuselection = int(input(" WELCOME TO THE NEWHAVEN DASHBOARD \n\n Please select from the following menu options \n\n"
                              " 1: View current houses on market \n 2: Search for available houses in a region \n 3: Record"
                              " a sale \n 4: Add a new property for sale \n 5:Show Sales \n 6: Exit"))


    if menuselection == 1:
        return_stock()
    if menuselection == 2:
        region_search()
    if menuselection == 3:
        house_sale()
    if menuselection == 4:
        add_property()
    if menuselection == 5:
        show_sales()
    if menuselection == 6:
        quit()

         
