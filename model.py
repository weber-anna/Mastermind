
## Erzeugen der random-generierten Lösungskombination
random_list = []

import random

def random_combination():
     for number in range(4):
         random_list.append(random.randint(1,6))

all_guess=[]
current_guess = []

## Definieren der Funktion für die Benutzereingabe und deren Überprüfung
def user_guess(number=0):
    global current_guess
    current_guess = []
    number=0
    valid_numbers=[1,2,3,4,5,6]

    while number <4:
        current_guess.append(input("\n Gib eine Zahl für Stelle {} an: " .format(number+1)))
        try:
            current_guess[number]=int(current_guess[number])
            if current_guess[number] not in valid_numbers:
                print("--\n    Inkorrekte Eingabe: {} liegt nicht zwischen 1 und 6. \n    Bitte gib eine Zahl zwischen 1 und 6 an!\n--".format(current_guess[number]))
                current_guess.pop(number)
            else:
                number += 1
        except:
            print("--\n    Inkorrekte Eingabe: Du hast keine Nummer eingegeben \n    Bitte gib eine Zahl zwischen 1 und 6 an!\n--")
            current_guess.pop(number)

    if current_guess in all_guess:
        print("--\n Du hast diese Kombination schon einmal geraten. Bitte rate eine andere Kombination.\n--")
        return user_guess()
    else:
        all_guess.append(current_guess)


## Definieren der Funktion, die den Status wiedergibt
def check_winner():
    if current_guess != random_list and len(all_guess)<10:
        return "Rate weiter"
    elif current_guess!= random_list and len(all_guess)==10:
        return "Leider verloren"
    else:
        return "winner"


## Definieren der Funktion, die die aktuelle Benutzereingabe mit der Lösung vergleicht
## und das Feedback dabei erzeugt
all_red_counts=[]
all_white_counts=[]

def check_userguess():
    global red_count
    global white_count
    global red_list
    red_count = 0
    white_count = 0
    red_list = random_list.copy()

    for numbers in range(4):
        if current_guess[numbers] == random_list[numbers]:
            red_count += 1
            red_list.pop(numbers)
            red_list.insert(numbers,int(0))
        else:
            continue
    for numbers in range(4):
        if current_guess[numbers] in red_list and red_list[numbers] != 0 :
            white_count += 1
            white_list = red_list.copy()
            tmp = white_list.index(current_guess[numbers])
            white_list.pop(white_list.index(current_guess[numbers]))
            white_list.insert(tmp,int(0))
        else:
            continue

    global all_red_counts
    global all_white_counts

    all_red_counts.append(red_count)
    all_white_counts.append(white_count)

