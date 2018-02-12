from random import random


# Parameter des Spielfeldes
number_player = 2
size = 9
number_of_ships = 10
win_count = 3

# -------------------------------------------------------
a = [[" " for j in range(size)] for i in range(size)]
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
positions = []

bombed_ships = [0 for k in range(number_player)]
rounds = 0


def label_to_integer(key):
    return labels.index(key.upper())


def print_game():
    print("")
    print("   1 2 3 4 5 6 7 8 9 ")
    for i in range(len(a)):
        print("  +-+-+-+-+-+-+-+-+-+")
        print("{} |{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(labels[i], a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5],
                                                       a[i][6], a[i][7], a[i][8]))
    print("  +-+-+-+-+-+-+-+-+-+")
    print("")
    print("")


def turn(n, m):
    global rounds
    a[n][m] = "X"
    print_game()

    if [n, m] in positions:
        current = rounds % number_player
        bombed_ships[current] += 1
        print("Treffer: Spieler {} hat {} Schiffe versenkt.".format(current + 1, bombed_ships[current]))

        if bombed_ships[current] == win_count:
            print("Spieler {} hat nach {} Runden gewonnen!".format(current + 1, rounds + 1))
            return False

    rounds += 1
    return True


def run_game():
    run = True
    print_game()

    while run:
        cmd = input('Spieler {}>'.format((rounds % number_player) + 1))

        if cmd == "exit":
            run = False
        else:
            try:
                n = label_to_integer(cmd[0])
                m = int(cmd[1]) - 1

                if a[n][m] == "X":
                    print("Position already attacked!")
                else:
                    run = turn(n, m)

            except ValueError:
                print("Wrong command!")
            except IndexError:
                print("Invalid position!")


def init_game():
    while len(positions) < number_of_ships:
        n = int(round(random() * (size - 1)))
        m = int(round(random() * (size - 1)))
        if [n, m] not in positions:
            positions.append([n, m])


if __name__ == "__main__":
    init_game()
    run_game()
