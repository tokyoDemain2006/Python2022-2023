answer = input("what is the capital of thailand")
answer = answer.title()
counter = 1

while answer != "Bangkok":
    answer = input("incorrect, try again: ")
    answer = answer.title()
    counter = counter + 1
print("correct! you had", counter,"attempts.!")
