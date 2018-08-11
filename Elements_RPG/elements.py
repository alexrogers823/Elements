import create_players
import time, random, os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def battle(hero, enemy):
    introductions = [
        "A {} stands in your way! Prepare for battle!",
        "Your path is being blocked by a {}! Can you take him?",
        "Look here, a {} is sizing you up! Kill them"]

    print(random.choice(introductions.format(enemy.name)))
    time.sleep(2)
    #Write a while loop that displays and executes attacks until there is a winner


def main_menu():
    '''Where the game starts. Sets default difficulty and mode'''

    choices = {
        "[C]hange modes": "change difficulty and modes",
        "[S]tart game": "start playing"
        "[P]assword": "enter save password"
    }
    print('Welcome! Choose from the following options')
    for choice in choices.keys():
        print('{} to {}'.format(choice, choices[choice]))

    # try/except here
    path = input()

    if path.lower().startswith('pass'):
        password = input('Password: ')
        save_hack(password)
    elif path.lower().startswith('ch'):
        change_modes()
    else:
        tutorial()
    #if password isn't blank, unpack it as a tuple. if blank, ask for tutorial
    # and/or go to create_hero
    # also provide try/except if user enters an invalid password


def change_modes(difficulty, mode):
    # have information dict/list to show different modes
    # change private (or global) variable on based on user input


def save_hack(password):
    '''Function that re-creates a previous hero based on password user inputted'''
    # ask the player for the hero's name again
    # create a tuple or dictionary using password via packing/unpacking
    # use inherited class to re-create hero using tuple and name


def tutorial():
    '''Sets tutorial variable to true, and gives tutorial on basics of game'''
    # talk about player types and weaknesses
    # give an example of battle gameplay
    # talk about XP and coin gains
    # shop and fusion tutorial will happen during gameplay


def create_hero():
    '''Sets hero name and type to use throughout gameplay'''
    print("Create your hero. Choose wisely!")
    # user chooses one of the types: water, earth, fire, or air
    element_type = input("Which element type? Water, Earth, Fire, or Air?\n").title()
    weapon_attack = element_type + " Attack"
    # user names the hero
    hero_name = input("Your hero needs a name...\n")
    # after deciding, a hero is made using the inherited class that was imported
    print("Creating hero {}".format(hero_name))
    time.sleep(3)



def order_of_levels():
    '''Creates level order based on hero type'''
    level_types = ["Water", "Earth", "Fire", "Air"]
    # based on hero weakness, cycle levels to where weakness is levels 4 and 9
    # for now, we will have each level as separate function
    # later, we will refactor to call one 'level' function with parameters deciding which level


def shop():
    '''Where user can purchase upgrades for their hero'''
    # show weapons and stones, and how much each cost
    # make sure hero can only equip one elemental stones


def display_stats():
    '''Recurring function where full hero statistics are shown at end
    of level, or after shop purchases'''
    # may play with idea of using coins to display during battle


def user_options():
    '''Recurring function that displays what hero can do to attack during gameplay'''
    # 'Hero's move
    print("Your move")
    # display normal attacks
    # display special attacks only if acquired
    # display stones

def set_level():
    '''Creates level based on various factors'''
    # unused function. Meant to create all levels using several arguments instead
    # will come back to this. Could be useful for refactoring into cleaner code


def level_one():
    '''Sets level'''


def level_two():
    '''Sets level'''


def level_three():
    '''Sets level'''


def level_four():
    '''Sets level'''


def level_five():
    '''Sets level'''


def level_six():
    '''Sets level'''


def level_seven():
    '''Sets level'''


def level_eight():
    '''Sets level'''


def level_nine():
    '''Sets level'''


def level_ten():
    '''Sets level'''


def elematrix():
    '''Introduces boss and continues level 10'''
    # comes in boss part of level level_ten
    print("All of the sudden, the elements go wild...")
    time.sleep(2)
    print("A strange anomoly appears, and it looks...so...menicing")
    time.sleep(3)
    slow_message = ["It's time", "to fight", "ELEMATRIX!"]
    for word in slow_message:
        print(word, end="")
        time.sleep(1)


def game_over():
    '''signals end of game to user'''
    # if hero is killed, gives bad message
    if result == 'bad':
        print("Looks like {} has fallen. Game over".format(hero.name))
        print("Keep playing though. You're one step closer to success!")
    # if user beat game, gives good message (good ending)
    if result == 'good':
        print("After ten levels of brutal hell, you did it! {} is the king of elements".format(hero.name))
        print("Challenge yourself by switching difficulties if you haven't already")
    # goes to generate_password function based on stats of hero
    generate_password()


def generate_password():
    '''After game ends, this will generate a password based on hero stats,
    so that user can choose to start game with these stats next time'''
    # will use hero object to pack/unpack statistics into password
    # parameter will either be *args (tuple) or **kwargs (dictionary)
    # will then make an array based on argument passed, then join into single string



# -- START OF PROGRAM --

print('{0} ELEMENTS {0}'.format('-'*10))
time.sleep(2)
print('An RPG game on the four powers of life')
time.sleep(2)

# main_menu()

# include try/except using keyboard interruption where if the user wants to leave
# at any time, they can do so and end the game abruptly

# play_again = input('Interesting game right? Wanna give it another try? [y/n]')
# if play_again.lower().startswith('y'):
#     main_menu()

# private variables. move these later
game_difficulty = 'normal'
game_mode = 'scarce'
game_multiplier = 1.3
