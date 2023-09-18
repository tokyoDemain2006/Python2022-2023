def areaOfATriangle():
    input1 = int(input("What is the base of the triangle"))
    input2 = int(input("What is the height of the triange"))
    print((input1 * input2) / 2)

def PowerCalculator():
    input1 = int(input("What is the volts"))
    input2 = int(input("What is the current"))
    print(input1*input2)

def AdditionCalc():
    input1 = int(input("What is the first number"))
    input2 = int(input("What is the second number"))
    print(input1 + input2)

def CalcAge():
    inputYears = int(input("What is your age"))
    print(inputYears*365)

def MorseCode():
    char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
    word = input("what would you like to convert to morse")
    length = len(word)
    char = [word]
    x = 0
    while x <= length:
        print(char_to_dots[x])
        x = x + 1
            
        
    

choice = input("what do you want to do \n1. Calculate area of a triangle\n2. Calculate Power of a circuit\n3. Addition Calc\n4. Calculate age in days")
if choice == "1":
    areaOfATriangle()
elif choice == "2":
    PowerCalculator()
elif choice == "3":
    AdditionCalc()
elif choice == "4":
    CalcAge()
elif choice == "5":
    MorseCode()
