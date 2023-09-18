numberOfPeople = int(input("how many people does the recipe serve"))
name = input("what is the name of the recipe")
recipe = []
nowServes = input("how many people do you want to serve")
check = True

while check == True:
    ingredient = input("enter an ingridient")
    amount = int(input("enter how much of the ingredient is needed"))
    amount = amount * (int(nowServes) / int(numberOfPeople))
    unit = input("enter the unit, e.g. Grams")
    temp = (ingredient, amount, unit)
    recipe.extend(temp)
    checkTemp = input("would you like to add another ingredient")
    if checkTemp == "Y" or checkTemp == "y":
        check = True
    else:
        check = False

print(recipe)
print(name)
print("revised recipe for ", nowServes, "people.")
