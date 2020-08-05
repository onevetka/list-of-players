import json
import os


# List of players -->

def init_list(file):
    """
    Load list from file. Reads json objects
    """
    global players
    global total_amount
    global amount_of_good
    global amount_of_bad

    try:
        with open(file, 'r') as jfr:
            try:
                players = json.load(jfr)
            except Exception:
                print("Повреждена структура json объектов в файле '" + str(file) + "'")
                raise SystemExit(1)
            finally:
                jfr.close()
    except FileNotFoundError:
        print("Error: file '" + str(file) + "' not found")
        raise SystemExit(1)
    jfr.close()

    total_amount = 0
    amount_of_good = 0
    amount_of_bad = 0

    for i in players:
        if i['opportunity'] == 'Yes':
            amount_of_good += 1
        else:
            amount_of_bad += 1
        total_amount += 1


def get_statistics():
    """
    Adds General information about the list to a single line
    """
    return 'Total: ' + str(total_amount) + '         ' +\
           'Good: ' + str(amount_of_good) + '         ' +\
           'Bad: ' + str(amount_of_bad)


def increase_stat(tf):
    global total_amount
    global amount_of_good
    global amount_of_bad

    total_amount += 1
    if tf:
        amount_of_good += 1
    else:
        amount_of_bad += 1


def save_changes(file):
    """
    Write list to file
    """
    with open(file, 'w') as jf:
        json.dump(players, jf, indent=4)


def add_player(name, opportunity, description):
    """
    Add or change profile onto initialized list
    :return True - If player have added into list.
            False - If the player is not in the list
    """
    global players
    profile = {
        'name': name,
        'opportunity': opportunity,
        'description': description
    }
    for i in range(len(players)):
        if players[i]['name'] == profile['name']:
            players[i] = profile
            return True
    players.append(profile)
    players = sort_players()
    return False


def sort_players():
    return sorted(players, key=lambda x: x['name'])


def find_player(name):
    """
    Return the players profile with name
    Return name = '\0' if player not found
    """
    for i in players:
        if name == i['name']:
            return i['opportunity'] + ' ' +\
                   i['description']
    return 'Player not found'

# TODO: Сделать возможность удаления игрока из списка. Лучше через вторую вкладку


# Specificity of tkinter -->

def get_list():
    """
    Return a list as a string
    """
    plist = ""
    for i in players:
        plist = \
            plist +\
            i['name'] + ' - ' +\
            i['opportunity'] + '\n' +\
            i['description'] +\
            '\n\n'
    return plist


# Settings of game -->

def add_to_clipboard(text):
    """
    Add text to buffer
    """
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)
