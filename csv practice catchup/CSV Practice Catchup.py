file = open("gamerscore.csv", "r")
line = file.readline()

while(line):
    data = line.split(",")
    searchscore=int(data[1])
    if searchscore == 7963:
        print("Handle:  ", data[0], "--- Gamerscore:  ", data[1])
        line = file.readline()
    else:
        line = file.readline()

file.close
