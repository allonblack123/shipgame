from random import random

# Parameter des Spielfeldes
number_player = 2
size = 9
number_of_ships = 10
win_count = 3

# -------------------------------------------------------
# Variablen
a = [[" " for j in range(size)] for i in range(size)]
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
positions = []
names = []

bombed_ships = [0 for k in range(number_player)]
rounds = 0


def label_to_integer(key):
    """
    Gibt die Position des Labels als Integer zurück.
    :param str key: Name des Labels
    """
    return labels.index(key.upper())


def get_current_player():
    """
    Gibt den Namen des aktuellen Spielers zurück.
    """
    return names[rounds % number_player]


def print_game():
    """
    Gibt das Spielfeld in der Konsole aus.
    """
    print("")
    print("   1 2 3 4 5 6 7 8 9 ")
    for i in range(len(a)):
        print("  +-+-+-+-+-+-+-+-+-+")
        print("{} |{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(labels[i], a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5],
                                                       a[i][6], a[i][7], a[i][8]))
    print("  +-+-+-+-+-+-+-+-+-+")
    print("")


def turn(n, m):
    """
    Macht einen gültigen Zug am Spielfeld
    :param int n: horizontale Position am Spielfeld
    :param int m: vertikale Position am Spielfeld
    """
    global rounds
    a[n][m] = "X"

    if [n, m] in positions:
        current = rounds % number_player
        bombed_ships[current] += 1
        print("Treffer: {} hat {} Schiffe versenkt.".format(get_current_player(), bombed_ships[current]))

        if bombed_ships[current] == win_count:
            print("{} hat nach {} Runden gewonnen!".format(get_current_player(), rounds + 1))
            exit(0)

    rounds += 1


def computer_turn():
    """
    Simuliert einen gültigen Zug
    """
    n = int(round(random() * (size - 1)))
    m = int(round(random() * (size - 1)))
    while a[n][m] == "X":
        n = int(round(random() * (size - 1)))
        m = int(round(random() * (size - 1)))
    turn(n, m)
    return n, m


def player_turn():
    """
    Nimmt Spielerinput entgegen, überprüft diesen auf seine Gültigkeit, und führt Zug aus.
    """
    turn_done = False
    while not turn_done:
        cmd = input('{}>'.format(get_current_player()))

        if cmd == "exit" or cmd == "ende":
            exit(0)

        try:
            if len(cmd) == 3:
                raise IndexError()

            n = label_to_integer(cmd[0])
            m = int(cmd[1]) - 1

            if a[n][m] == "X":
                print("Position wurde bereits angegriffen!\n")
                continue
            else:
                turn(n, m)
                turn_done = True
        except ValueError:
            print("Unbekannter Befehl!")
        except IndexError:
            print("Ungültige Position!")


def run_game(single_player):
    """
    Startet das Spiel, und lässt Spieler abwechselnd setzen.
    :param bool single_player: True wenn der Singelplayer-Modus gespielt wird
    """
    print_game()
    while True:
        player_turn()

        if single_player:
            n, m = computer_turn()
            print_game()
            print("Computer hat {}{} angegriffen.\n".format(labels[n], m + 1))
        else:
            print_game()


def init_game(single_player):
    """
    Initalisiert das Spielfeld, und die Spielernamen
    :param bool single_player: True wenn der Singelplayer-Modus gespielt wird
    """
    if single_player:
        names.append("Spieler")
        names.append("Computer")
    else:
        names.append("Spieler 1")
        names.append("Spieler 2")

    while len(positions) < number_of_ships:
        n = int(round(random() * (size - 1)))
        m = int(round(random() * (size - 1)))
        if [n, m] not in positions:
            positions.append([n, m])


def get_mode():
    """
    Gibt zurück, ob der Singelplayer-Modus, oder der Multiplayer-Modus gestartet werden soll.
    """
    while True:
        print("Wähle einen Modus:")
        print("1: Einspieler-Modus")
        print("2: Zweispieler-Modus")
        imode = input()

        if imode == "exit" or imode == "ende":
            exit(0)

        if imode == "1" or imode == "2":
            return imode

        print("Falscher Wert für den Modus!\n")


if __name__ == "__main__":
    single_player_mode = (get_mode() == "1")
    init_game(single_player_mode)
    run_game(single_player_mode)