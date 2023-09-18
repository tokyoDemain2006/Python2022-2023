superheroes = ["Batman", "Green lantern", "Superman", "Spiderman"]

print("current pilot: ",superheroes[0])
print("current co-pilot: ",superheroes[1])
superheroes[2] = "Hit Girl"
hero1 = input("What hero do you want to add to the team:   ")
hero2 = input("What other hero do you want to add to the team:   ")
superheroes.append(hero1)
superheroes.append(hero2)
print(superheroes)
