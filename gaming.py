unit = input("what is the unit you what to use? ")
amount = float(input("what amount do you have? "))
newUnit = input("what unit would you like to convert to? ")
conversion = float(input("what is the conversion rate? "))
newNumber = (amount * conversion)
print(newNumber, newUnit)