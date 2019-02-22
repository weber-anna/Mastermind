import model as m
import os

def rules():
    print("""\n---------------------------------------\nSPIELREGELN FÜR DAS MASTERMIND: \n---------------------------------------\n
    Ziel des Spiels ist es, eine zufällig generierte 4-stellige Zahlenkombination aus den Zahlen 1-6 zu erraten. \n
    Du hast dafür 10 Rateversuche. 
    Für jeden deiner 4-stelligen Rateversuche, erhälst du Feedback. 
    Wie viele Zahlen bereits an der richtigen Stelle stehen, wird dir in der Spalte 'rot' angezeigt.
    Hast du Zahlen richtig erraten, jedoch nicht an die richtige Stelle gestellt, wird dir in der Spalte 'weiss' angezeigt, auf wie viele Zahlen das zutrifft.
    Es werden nur Zahlen zwischen 1 und 6 akzeptiert. Alle anderen Eingaben führen zu einer Fehlermeldung und fordern dich zu einer korrekten Eingabe auf.
    """)
    starten=input("Bist du bereit? \nGib 'OK' ein, um das Spiel zu starten! > ")
    if starten == "OK" or "ok":
        start_game()
    else:
        rules()


def start_game():
    m.random_combination()

    while m.current_guess!=m.random_list and len(m.all_guess) <10:
        os.system("cls")
        print_gameboard()
        m.user_guess()
        m.check_userguess()

    if m.current_guess != m.random_list and len(m.all_guess) == 10:
        print_gameboard()
        print_seperator()
        print("Du hast nur 10 Versuche. Loser! Leider verloren! Die richtige Lösung wäre {} \n".format(m.random_list))
    elif m.current_guess== m.random_list:
        print_gameboard()
        print_seperator()
        print("Woohoo! Gewonnen! Die richtige Lösung ist {} \n".format(m.random_list))


def print_gameboard():
    print("\n    M A S T E R M I N D - L O T T O\n")
    print_seperator()
    print(" | Nr || Rateversuche  ||  rot  | weiss |")
    print_seperator()
    for m.current_guess in m.all_guess:
        print_turn()

def print_seperator():
    print( " +" + (("-")*4) + "||" + (("-")*3) + "+" + (("-")*3) + "+" +
                (("-")*3) + "+" + (("-")*3) + "||" + (("-") * 7) + "+" + (("-") * 7) + "+ ")

def print_turn():
    print(" |" +"{:^4}||{:^3}|{:^3}|{:^3}|{:^3}||{:^7}|{:^7}|".format((m.all_guess.index(m.current_guess)+1), m.current_guess[0], m.current_guess[1],
                                                     m.current_guess[2], m.current_guess[3],m.all_red_counts[m.all_guess.index(m.current_guess)], m.all_white_counts[m.all_guess.index(m.current_guess)]))



#print_gameboard()




