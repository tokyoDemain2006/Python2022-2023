villains = ["The Joker","Magneto","Red Mist","Doc Ock"]
wages = [21,17,3,5]
for counter in range(4):
    print(villains[counter])
totalWage = 0
for counter in range(4):
    print(villains[counter],": £",wages[counter]," million")
    totalWage = (totalWage + wages[counter])

print("Wage Bill: £",totalWage," million")
