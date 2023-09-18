import random
count = 1
correct = False
answer = random.randint(1,100)
while correct == False:
    guess = int(input("make your guess: "))
    if guess == answer:
        print("you guessed correct")
        correct = True
        print(count, "attempts")
    elif guess > answer:
        print("too high")
        count = count + 1
    else:
        print("too low")
        count = count + 1

amount = 0
added = 0.01
for count in range(1,52):
    print("week", count)
    added = added * 2
    amount = amount + added
    print (added)
    print (amount)
