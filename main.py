from time import sleep
from os import system

clear = lambda: system('cls')

weapons = {1:"Single Shot", 2:"Double Shot", 3:"Headshot", 4:"Grenade", 5:"Cannon", 6:"Double Headshot", 7:"Poison Shot", 8:"Double Grenade", 9:"Machine Gun", 10:"Double Cannon", 12:"Sniper", 14:"Double Poison", 16:"Zeus27", 18:"Double Machine Gun", 20:"Energy Laser", 25:"Nutrino Blast", 30:"Fowl Sock Smell"}
shields = {0:"No shield", 1:"Shield", 2:"Double Shield", 3:"Head Shield", 4:"Defuser", 5:"Rock Wall", 6:"Reinforced Head Shield", 7:"Immuner", 8:"Double Defuser", 9:"Metal Wall", 10:"Reinforced Rock Wall", 12:"Metal Kelvar", 14:"Double Immuner", 16:"Plasma Shield", 18:"Reinforced Metal Wall", 20:"Reinforced Plasma Shield", 25:"Heavy Immuner", 30:"Cover your nose"}
reloadcount = 1
players = []
playersafter = []
someonedied = False

class Player:
    def __init__(self, name, reloads=0, weapon=None, shield=0, who=None, who2=None, attackers=[]):
        self.reloads = reloads
        self.name = name
        self.weapon = weapon
        self.shield = shield
        self.who = who
        self.who2 = who2
        self.attackers = attackers

print("Welcome to Matrix by Shiv Patil.\n")

while True:
    try:
        playernum = int(input("How many players would be playing? : "))
        if playernum < 2:
            print("Minimum 2 players are necessary to play this game.\n")
            continue
        print()
        break
    except:
        print("Please enter a valid number.\n")

for i in range(1, playernum+1):
    name = input(f"Name of Player{i}: ")
    players.append(Player(reloads=0, name=name))

while True:
    try:
        level = str(input("\nLevel- Easy or Hard? : "))
        if level.upper() == "EASY":
            reloadcount = 1
            break
        elif level.upper() == "HARD":
            reloadcount = 10
            break
        else:
            print("Please enter either 'easy' or 'hard'.")
    except:
        print("Please enter a valid input.")

print("\n")
for t in range(5, 0, -1):
    print(f"The game will start in {t} seconds ", end = '\r')
    sleep(1)

rounds = 1
while True:
    print(f"\n--------ROUND {rounds}--------\n")
    for reloadprint in players:
        print(f"{reloadprint.name}: {reloadprint.reloads} reloads.")
    print()
    rounds += 1
    input("Press enter to continue.")
    clear()
    for turn in players:
        turn.weapon = None
        turn.shield = 0
        turn.who = None
        turn.who2 = None
        turn.attackers = []

        while True:
            decision = str(input(f"{turn.name}-- What do you want to do- Reload, Fire or Shield (1 or 2 or 3)? : "))
            if decision == "1":
                turn.reloads += reloadcount
                break
            elif decision == "2":
                if turn.reloads < 1:
                    print("You have insufficient reloads to fire any weapon.\n")
                    continue
                while True:
                    try:
                        weapon = int(input("How many reloads would you like to fire?: "))
                        if weapon > turn.reloads:
                            print(f"You have insufficient reloads. You have: {turn.reloads}")
                        else:
                            print(f"\nYour have chosen to fire {weapons[weapon]}.")
                            turn.reloads -= weapon
                            turn.weapon = weapon
                            break
                    except KeyError:
                        print("There is no weapon for that number of reloads.\n")
                    except ValueError:
                        print("Please enter a valid number.\n")
                while True:
                    if turn.weapon not in (2, 6, 14, 18):
                        try:
                            print("On which player do you want to fire on?")
                            opt = 1
                            for i in players:
                                print(f"\n{opt} = {i.name}", end="")
                                opt+=1
                            who = int(input("  :  "))
                            if players[who-1] != turn:
                                print(f"You have chosen to attack {players[who-1].name}.")
                                turn.who = players[who-1]
                                turn.who2 = None
                                break
                            else:
                                print("\nYour reloads have been wasted.\n")
                                turn.weapon = None
                                break
                        except IndexError:
                            print("\nThere is no player for that number.\n")
                        except ValueError:
                            print("Please enter a valid number.\n")
                    else:
                        try:
                            print("On which player do you want to fire one shot?")
                            opt = 1
                            for i in players:
                                print(f"\n{opt} = {i.name}", end="")
                                opt+=1
                            who = int(input("  :  "))
                            print("On which player do you want to fire another shot?")
                            opt = 1
                            for i in players:
                                print(f"\n{opt} = {i.name}", end="")
                                opt+=1
                            who2 = int(input("  :  "))
                            if who == who2:
                                if players[who-1] != turn:
                                    print(f"You have chosen to attack {players[who-1].name} with {weapons[turn.weapon]}.")
                                    turn.who = players[who-1]
                                    turn.who2 = None
                                    break
                                else:
                                    print("\nYour reloads have been wasted.\n")
                                    turn.weapon = None
                                    break
                            else:
                                if players[who-1] != turn:
                                    turn.weapon /= 2
                                    turn.who = players[who-1]
                                else:
                                    print("\nYour reloads have been wasted.\n")
                                    turn.weapon = None
                                    break
                                if players[who2-1] != turn:
                                    print(f"You have chosen to attack {players[who-1].name} and {players[who2-1].name} with {weapons[turn.weapon]}.")
                                    turn.who2 = players[who2-1]
                                    break
                                else:
                                    print("\nYour reloads have been wasted.\n")
                                    turn.weapon = None
                                    turn.who = None
                                    break
                        except IndexError:
                            clear()
                            print("\nThere is no player for that number.\n")
                        except ValueError:
                            clear()
                            print("Please enter a valid number.\n")
                break
            elif decision == "3":
                while True:
                    try:
                        shield = int(input(f"Which sheild would you like to use?\n1={shields[1]}\n2={shields[2]}\n3={shields[3]}\n4={shields[4]}\n5={shields[5]}\n6={shields[6]}\n7={shields[7]}\n8={shields[8]}\n9={shields[9]}\n10={shields[10]}\n12={shields[12]}\n14={shields[14]}\n16={shields[16]}\n18={shields[18]}\n20={shields[20]}\n25={shields[25]}\n30={shields[30]}  :   "))
                        print(f"\nYour have chosen to use {shields[shield]}")
                        turn.shield = shield
                        break
                    except KeyError:
                        print("\nThere is no shield for that number.\n")
                    except ValueError:
                        print("Please enter a valid number.\n")
                break
            else:
                print("Please enter either option 1, 2 or 3.")

        input("Press enter to end your turn.\n")
        clear()

    for player in players:
        if player.who != None:
            if player.who.who != player and player.who.who2 != player:
                player.who.shield-=player.weapon
                player.who.attackers.append(f"{player.name} with {weapons[player.weapon]}")
            else:
                if player.who.weapon == player.weapon:
                    pass
                elif player.who.weapon > player.weapon:
                    player.shield = player.weapon - player.who.weapon
                    player.attackers.append(f"{player.who.name} with {weapons[player.who.weapon]}")
                elif player.who.weapon < player.weapon:
                    player.who.shield = player.who.weapon - player.weapon
                    player.who.attackers.append(f"{player.name} with {weapons[player.weapon]}")

        if player.who2 != None:
            if player.who2.who != player and player.who2.who2 != player:
                player.who2.shield-=player.weapon
                if (f"{player.name} with {weapons[player.weapon]}") not in player.who2.attackers:
                    player.who2.attackers.append(f"{player.name} with {weapons[player.weapon]}")
            else:
                if player.who2.weapon == player.weapon:
                    pass
                elif player.who2.weapon > player.weapon:
                    player.shield = player.weapon - player.who2.weapon
                    if (f"{player.who2.name} with {weapons[player.who2.weapon]}") not in player.attackers:
                        player.attackers.append(f"{player.who2.name} with {weapons[player.who2.weapon]}")
                else:
                    player.who2.shield = player.who2.weapon - player.weapon
                    if (f"{player.name} with {weapons[player.weapon]}") not in player.who2.attackers:
                        player.who2.attackers.append(f"{player.name} with {weapons[player.weapon]}")

    playersafter[:] = []
    for someone in players:
        if someone.attackers == [] or someone.shield == 0:
            playersafter.append(someone)
        else:
            print(f"{someone.name} died. The attackers were {someone.attackers}.")
            print(f"hp = {int(someone.shield)}")
            someonedied = True
    players[:] = playersafter

    if len(players) == 1:
        print(f"\n\n{players[0].name} won! Game over.")
        input("\n\nThank you for playing.")
        break
    elif len(players) == 0:
        print(f"Everyone Dead! Game over.")
        input("\n\nThank you for playing.")
        break
    elif not(someonedied):
        print("Nobody died.")
    someonedied = False

    input(f"\n\nPress enter to start round {rounds}.")
    clear()