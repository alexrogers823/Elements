from attack_names import Attacks
from gameplay_mods import Gameplay
import create_players, game_items
import time, math, random, os, sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def set_gameplay():
    '''Sets all meta variables before game starts'''
    play = Gameplay()
    main_menu(play)
    # tutorial(play)


def main_play_order(play, hero):
    if play.level == 0:
        game_intro(hero)
    while play.level < 10:
        order_of_levels(play, hero)
        shop(hero)

# playing with this idea. May or may not have it
def game_intro(hero):
    print()
    print('''\tLong ago, the world was balanced by the elemental forces
    that were bestowed, in equal strength and harmony.
    \tBut an evil entity took advantage of such strengths and created chaos,
    unleashing havoc by corrupting the guardians of the elements and the ones
    who serve them.
    Now, it is up to {} to restore order, and bring an end to great evil once and
    for all...'''.format(hero.name))
    input('\nPress ENTER to continue')


def battle(hero, enemy, exp_damage):
    # hero_battle = game_items.Battle(hero.life_points, hero.magic_points)
    # enemy_battle = game_items.Battle(enemy.life_points)
    hero_inventory = hero.display_inventory

    introductions = [
        "A {} stands in your way! Prepare for battle!",
        "Your path is being blocked by a {}! Can you take him?",
        "Look here, a {} is sizing you up! Kill them",
        "You've stumbled across a {}, and he looks dangerous!",
        "All of a sudden a {} approaches! Stand your ground!",
        "You're face to face with a {}! And he's out for blood"
        ]

    if not enemy.boss:
        print(random.choice(introductions).format(enemy.name))
    time.sleep(2)
    #Write a while loop that displays and executes attacks until there is a winner
    while hero.life_points > 0 and enemy.life_points > 0:
        attack, damage, magic_used = user_options(hero, enemy, hero_inventory)
        print("You attack with {}, causing {} damage!".format(attack, damage))
        time.sleep(1)
        # if hero elemental stone == enemy type, lower the damage
        enemy.attacked = damage
        hero.mp_replenish = magic_used
        if enemy.life_points <= 0:
            hero.mp_replenish
            break

        enemy.change_base_damage
        enemy_attack, enemy_damage = random.choice([(enemy.low_attack, enemy.base_low_damage), (enemy.high_attack, enemy.base_high_damage), (enemy.weapon_attack, enemy.base_weapon_damage)])
        enemy_damage = math.ceil(enemy_damage*exp_damage)
        print("The {} attacks with {}, causing {} damage!".format(enemy.name, enemy_attack, enemy_damage))
        hero.attacked = enemy_damage
        if hero.life_points <= 0:
            break

        hero.mp_replenish

    if enemy.life_points <= 0:
        return "win"
    else:
        return "loss"





def main_menu(play):
    '''Where the game starts. Sets default difficulty and mode'''
    difficulty, game_multiplier, enemy_multiplier = play.set_difficulty
    mode = play.set_mode

    print("Current gameplay: {} difficulty, {} LP boost".format(difficulty.title(), mode))

    choices = {
        "[C]hange modes": "change difficulty and modes",
        "[S]tart game": "start playing",
        "[P]assword": "enter save password"
    }
    print('Welcome! Choose from the following options')
    for choice in choices.keys():
        print('{} to {}'.format(choice, choices[choice]))

    # try/except here
    while True:
        try:
            path = input()
            if not path.lower().startswith('p') and not path.lower().startswith('c') and not path.lower().startswith('s'):
                raise ValueError
        except ValueError:
            print('Invalid Selection')
        else:
            break

    if path.lower().startswith('p'):
        tries = 0
        while True:
            try:
                if tries > 3:
                    sys.exit()
                password = input('Password: ')
                if len(password) > 16 or password[10] != 'X':
                    raise ValueError
            except ValueError:
                print('Invalid Password')
                tries += 1
                if tries == 2:
                    print('Restart the game if password selection was done by mistake')
            else:
                break
        hero = save_hack(password)
        main_play_order(play, hero)
    elif path.lower().startswith('c'):
        change_modes(play)
    elif path.lower().startswith('s'):
        hero = tutorial(play)
        main_play_order(play, hero)


    #if password isn't blank, unpack it as a tuple. if blank, ask for tutorial
    # and/or go to create_hero
    # also provide try/except if user enters an invalid password


def change_modes(play):
    '''function that allows user to set difficulty and mode for game'''
    # have information dict/list to show different modes
    # change private (or global) variable on based on user input
    play.set_difficulty = input("Choose easy, normal, or hard\n")
    play.set_mode = input("Now choose generous, scarce, or survival\n")
    main_menu(play)


def save_hack(password):
    '''Function that re-creates a previous hero based on password user inputted'''
    # create a tuple or dictionary using password via packing/unpacking
    # use inherited class to re-create hero using tuple and name
    element = {
        "AQ": "Water",
        "TE": "Earth",
        "PY": "Fire",
        "AE": "Air"
    }

    stone = {
        "W": "Water",
        "E": "Earth",
        "F": "Fire",
        "A": "Air",
        "O": ""
    }

    # ask the player for the hero's name again
    hero_name = input('I forgot your hero\'s name again. What was it?\n')
    basic_attack, weapon_attack = Attacks("hero", element[password[:2]]).names()
    if password[6] == 'T':
        temp_stone = True
    else:
        temp_stone = False

    hero = create_players.Hero(hero_name, element[password[:2]], life_points=int(password[2:5]), basic_attack=basic_attack, elemental_stone=stone[password[5]], xp=int(password[11:15]), weapon_attack=weapon_attack, temp_stone=temp_stone)
    print('Got it. Let\'s continue...')
    time.sleep(2)
    return hero


def tutorial(play):
    '''Sets tutorial variable to true, and gives tutorial on basics of game'''
    print('Is this your first time playing?')
    if input().lower().startswith('y'):
        play.show_tutorials
        tutorial_explanations()
    # shop and fusion tutorial will happen during gameplay
    hero = create_hero()
    # game_intro(hero)
    # shop(hero)
    # generate_password(hero)
    return hero

def tutorial_explanations():
    # talk about player types and weaknesses
    # give an example of battle gameplay
    # talk about XP and coin gains
    next = '[Press ENTER]'
    print('''Welcome!
    In ELEMENTS, heroes and enemies are based on one of four types: Water, Earth, Fire, and Air
    Each type has a weakness (Water <--> Fire, Earth <--> Air) that can be used to your or your opponents advantage
    {}'''.format(next))
    input()
    print('''Your hero will start out with 100 life points and 50 magic points. Enemies will vary
    Enemy damage will reduce your LP, and special/weapon attacks will reduce your MP
    MP will increase by 5 after every turn, while LP will not increase until level ends
    If your LP hits zero, it's game over
    {}'''.format(next))
    input()
    print('''Each time you beat an enemy, you gain XP and Coins
    Higher XP leads to greater hero damage, and you can use coins in the shop (more on this later)
    {}'''.format(next))
    input()
    print('''Shop and fusions will be explained during the game
    You're ready to pick your hero
    {}'''.format(next))
    input()

def tutorial_shop(hero):
    print('''Welcome to the shop!
    This is where you can buy things for {} that will help in battles.
    For example, {} has {} coins, and {} costs 100 coins. You can buy it now.
    Also, you see {}'s XP. Higher XP leads to more impactful attacks.
    I'll let you take a look around.
    [ENTER to continue]''')



def create_hero():
    '''Sets hero name and type to use throughout gameplay'''
    print("Create your hero. Choose wisely!")
    # user chooses one of the types: water, earth, fire, or air
    element_choices = ["Water", "Earth", "Fire", "Air"]
    print("Which element type? Water, Earth, Fire, or Air?")
    while True:
        try:
            element_type = input().title()
            if element_type not in element_choices:
                raise ValueError
        except ValueError:
            print("Invalid choice. (Make sure your choice has correct spelling)")
        else:
            break

    basic_attack, weapon_attack = Attacks("hero", element_type).names()
    # user names the hero
    hero_name = input("Your hero needs a name...\n")
    # after deciding, a hero is made using the inherited class that was imported
    print("Creating hero {}".format(hero_name))
    time.sleep(3)
    return create_players.Hero(hero_name, element_type, basic_attack, weapon_attack=weapon_attack)



def order_of_levels(play, hero):
    '''Creates level order based on hero type'''
    # based on hero weakness, cycle levels to where weakness is levels 4 and 9
    # for now, we will have each level as separate function
    # later, we will refactor to call one 'level' function with parameters deciding which level
    order = {
        "Water": ["Air", "Earth", "Water", "Fire"],
        "Earth": ["Water", "Fire", "Earth", "Air"],
        "Fire": ["Earth", "Air", "Fire", "Water"],
        "Air": ["Fire", "Water", "Air", "Earth"]
    }

    stages = {
        "Water": ["Symbolic Ocean", "Aquatic Sanctuary"],
        "Earth": ["High Ground", "Cave of Wonder"],
        "Fire": ["Pyrocity", "Flaming Desert"],
        "Air": ["Windy Bridge", "Floating Sky"]
    }

    # Order is minion, sub-boss, boss 1, boss 2
    enemy_names = {
        "Water": ["Whitewater Sage", "Sr. Whitewater Sage", "Oceanic Prince", "Oceanic King"],
        "Earth": ["Geo Wrangler", "Geo Champion", "Earth Emperor", "Earth God"],
        "Fire": ["Blazed Knight", "Blazed Bishop", "Scorched Lieutenant", "Scorched General"],
        "Air": ["Wind Sorcerer", "Advanced Wind Sorcerer", "Wind Keeper", "Wind Master"]
    }

    play.level_up
    hero.lp_replenish = play.lp_replenish

    if play.level < 5:
        level_select = order[hero.element_type][play.level-1]
        stage_select = stages[level_select][0]
    elif play.level == 9:
        level_select = order[hero.element_type][play.level-6]
        stage_select = stages[level_select][1]
    else:
        level_select = order[hero.element_type][play.level-5]
        stage_select = stages[level_select][1]

    minion_name = enemy_names[level_select][0]
    boss_name = enemy_names[level_select][2]

    number_of_enemies = play.call_enemies
    exp_increase = play.multiplier**(play.level-1)
    # print(play.level)


    if play.level == 8:
        level_eight()
    elif play.level < 9:
        set_level(play, level_select, stage_select, hero, minion_name, boss_name, play.level, exp_increase, number_of_enemies)
    else:
        level_ten()
        elematrix()
    # level_one(level_select[0], stages[level_select[0]][0], hero, enemy_names[level_select[0]][0], enemy_names[level_select[0]][2])
    # level_two(level_select[1], stages[level_select[1]][0], hero, enemy_names[level_select[1]][0], enemy_names[level_select[1]][2])
    # level_three(level_select[2], stages[level_select[2]][0])
    # level_four(level_select[3], stages[level_select[3]][0])
    # level_five(level_select[0], stages[level_select[0]][1])
    # level_six(level_select[1], stages[level_select[1]][1])
    # level_seven(level_select[2], stages[level_select[2]][1])
    # level_eight("Fusion", "Lightning Tower")
    # level_nine(level_select[3], stages[level_select[3]][1])
    # level_ten("Fusion", "Element Vortex")



def shop(hero):
    '''Where user can purchase upgrades for their hero'''
    # show weapons and stones, and how much each cost
    # make sure hero can only equip one elemental stone
    while True:
        print("{0} SHOP {0}".format("-"*5))
        print("Type in the first three letters of item to purchase.")
        print("When you're finished, type EXIT to start next level")
        print(hero.shop_stats)
        print()
        # for loop that displays all options (from a class)
        for item in hero.display_shop_options:
            print("{}: {} Coins \n\t-{}".format(item[0], item[1], item[2]))
        buy = input()
        if buy.upper() != 'EXIT':
            if buy.lower().startswith('wea'):
                hero.acquire_items = 'weapon'
            print('Item bought!')
            time.sleep(2)
            clear_screen()
        else:
            break

    print("On to the next level...")
    time.sleep(1)


def display_stats(hero, level, coins, xp):
    '''Recurring function where full hero statistics are shown at end
    of level, or after shop purchases'''
    # may play with idea of using coins to display during battle
    print('{0} Stage {1} Clear {0}'.format('*'*3, level))
    print(hero.name)
    time.sleep(1)
    print('Coins gained during level: {}'.format(coins))
    time.sleep(1)
    print('XP gained during level: {}'.format(xp))
    time.sleep(1)
    # if flawless:
    #     print('Flawless victory!')


def user_options(hero, enemy, hero_inventory):
    '''Recurring function that displays what hero can do to attack during gameplay'''
    # 'Hero's move
    print()
    print(hero.stats)
    print("{0} VS {0}".format("-"*3))
    print(enemy.stats)
    print("Your move")
    print("*"*8)
    # display normal attacks
    # display special attacks only if acquired
    # display stones
    number = 0 #Hack-ish
    option_mp = [0, 10, 15] #Also hack-ish
    for option in hero_inventory:
        print('[{}]  {} ({} MP)'.format(chr(number+65), option, option_mp[number]))
        number += 1

    letter = ord(input().upper()) - 65
    basic, weapon = hero.choose_attack_damage
    choice = hero_inventory[letter]
    choice_attack = {
        "A": basic,
        "B": weapon
    }
    # hero.choose_attack_damage = letter
    attack_points, magic_points = choice_attack[chr(letter+65)]


    return choice, attack_points, magic_points

def set_level(play, chosen_type, stage, hero, minion_name, boss_name, level, exp_damage, number_of_enemies):
    level_coins = 0
    level_xp = 0
    '''Creates level based on various factors'''
    # unused function. Meant to create all levels using several arguments instead
    # will come back to this. Could be useful for refactoring into cleaner code
    # if level == 1:
    #     number_of_enemies = 5

    minion_low_attack, minion_high_attack, minion_weapon_attack = Attacks("enemy", chosen_type).names()
    minion_life_points = math.floor(20*exp_damage)
    boss_low_attack, boss_high_attack, boss_weapon_attack = Attacks("enemy", chosen_type, boss=True).names()
    boss_life_points = 50
    stage_boss = create_players.Enemy(boss_name, chosen_type, boss_life_points, boss_low_attack, boss_high_attack, weapon_attack=boss_weapon_attack, boss=True)
    print("Welcome to the {}".format(stage))
    time.sleep(1)
    print("Stage {} Begin".format(level))
    time.sleep(1)
    print("Enemies: {}".format(number_of_enemies))
    time.sleep(1)

    #5 enemies plus boss
    kills = 0
    while kills < number_of_enemies:
        minion = create_players.Enemy(minion_name, chosen_type, minion_life_points, minion_low_attack, minion_high_attack, weapon_attack=minion_weapon_attack)
        # outcome = battle(hero, minion)
        if battle(hero, minion, exp_damage) == "win":
            print("{} is defeated! You gain 5 coins".format(minion.name))
            hero.gain_coins_and_xp = 'minion'
            level_coins += 5
            level_xp += 5
            # hero.gain_xp = 'minion'
            time.sleep(1)
            kills += 1
        else:
            game_over(hero, "bad", play)

    print("You did good, but now...here comes the boss, {}!".format(stage_boss.name))
    # outcome = battle(hero, boss)
    if battle(hero, stage_boss, exp_damage) == "win":
        print("{} is defeated! You beat the level!".format(stage_boss.name))
        hero.gain_coins_and_xp = 'boss'
        level_coins += 75
        level_xp += 50
        # hero.gain_xp = 'boss'
        time.sleep(3)
        display_stats(hero, level, level_coins, level_xp)
        clear_screen()
        # shop(hero)
    else:
        game_over(hero, "bad", play)


def level_one(chosen_type, stage, hero, minion_name, boss_name, number_of_enemies=5):
    '''Sets level'''
    minion_low_attack, minion_high_attack, minion_weapon_attack = Attacks("enemy", chosen_type).names()
    minion_life_points = 20
    boss_low_attack, boss_high_attack, boss_weapon_attack = Attacks("enemy", chosen_type, boss=True).names()
    boss_life_points = 50
    stage_boss = create_players.Enemy(boss_name, chosen_type, boss_life_points, boss_low_attack, boss_high_attack, weapon_attack=boss_weapon_attack, boss=True)
    print("Welcome to the {}".format(stage))
    time.sleep(1)
    print("Stage 1 Begin")
    time.sleep(1)

    #5 enemies plus boss
    kills = 0
    while kills < number_of_enemies:
        minion = create_players.Enemy(minion_name, chosen_type, minion_life_points, minion_low_attack, minion_high_attack, weapon_attack=minion_weapon_attack)
        # outcome = battle(hero, minion)
        if battle(hero, minion) == "win":
            print("{} is defeated! You gain 5 coins".format(minion.name))
            hero.gain_coins_and_xp = 'minion'
            # hero.gain_xp = 'minion'
            time.sleep(1)
            kills += 1
        else:
            game_over(hero, "bad")
            print("You did good, but now...here comes the boss, {}!".format(stage_boss.name))
            # outcome = battle(hero, boss)
            if battle(hero, stage_boss) == "win":
                print("{} is defeated! You beat the level!".format(stage_boss.name))
                hero.gain_coins_and_xp = 'boss'
                # hero.gain_xp = 'boss'
                time.sleep(3)
                clear_screen()
                shop(hero)
            else:
                game_over(hero, "bad")

def level_two(chosen_type, stage, hero, minion_name, boss_name, number_of_enemies=8):
    '''Sets level'''
    minion_low_attack, minion_high_attack, minion_weapon_attack = Attacks("enemy", chosen_type).names()
    minion_life_points = 20
    boss_low_attack, boss_high_attack, boss_weapon_attack = Attacks("enemy", chosen_type, boss=True).names()
    boss_life_points = 70
    stage_boss = create_players.Enemy(boss_name, chosen_type, boss_life_points, boss_low_attack, boss_high_attack, weapon_attack=boss_weapon_attack, boss=True)
    print("Welcome to the {}".format(stage))
    time.sleep(1)
    print("Stage 2 Begin")
    time.sleep(1)

    #8 enemies plus boss
    kills = 0
    while kills < number_of_enemies:
        minion = create_players.Enemy(minion_name, chosen_type, minion_life_points, minion_low_attack, minion_high_attack, weapon_attack=minion_weapon_attack)
        # outcome = battle(hero, minion)
        if battle(hero, minion) == "win":
            print("{} is defeated! You gain 5 coins".format(minion.name))
            hero.gain_coins_and_xp = 'minion'
            # hero.gain_xp = 'minion'
            time.sleep(1)
            kills += 1
        else:
            game_over(hero, "bad")
    print("You did good, but now...here comes the boss, {}!".format(stage_boss.name))
    # outcome = battle(hero, boss)
    if battle(hero, stage_boss) == "win":
        print("{} is defeated! You beat the level!".format(stage_boss.name))
        hero.gain_coins_and_xp = 'boss'
        # hero.gain_xp = 'boss'
        time.sleep(3)
        # clear_screen()
        # shop(hero)
    else:
        game_over(hero, "bad")


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


def game_over(hero, result, play):
    '''signals end of game to user'''
    # if hero is killed, gives bad message
    if result == 'bad':
        print("Looks like {} has fallen. Game over".format(hero.name))
        print("Keep playing though. You're one step closer to success!")
    # if user beat game, gives good message (good ending)
    if result == 'good':
        print("After ten levels of brutal hell, you did it! {} is the king of elements".format(hero.name))
        print("Challenge yourself by switching difficulties if you haven't already")
    print()
    time.sleep(2)
    # goes to generate_password function based on stats of hero
    print("Use this password to start game with current stats:")
    generate_password(hero, play.level)
    sys.exit()


def generate_password(hero, level):
    '''After game ends, this will generate a password based on hero stats,
    so that user can choose to start game with these stats next time'''
    # will use hero object to pack/unpack statistics into password
    # parameter will either be *args (tuple) or **kwargs (dictionary)
    # will then make an array based on argument passed, then join into single string
    one = {
        "Water": "AQ",
        "Earth": "TE",
        "Fire": "PY",
        "Air": "AE"
    }

    if hero.life_points == 100 or hero.life_points < 1:
        two = '100'
    else:
        two = '0{}'.format(hero.life_points)

    if hero.elemental_stone and hero.temp_stone:
        three = '{}T'.format(hero.elemental_stone[0])
    elif hero.temp_stone:
        three = 'OT'
    else:
        three = 'OO'

    four = hero.magic_points

    five = 1 #weapon level. Will do later

    if hero.xp > 1000:
        six = hero.xp
    else:
        six = '0{}'.format(hero.xp)

    if level > 2 or level < 10:
        seven = '0{}'.format(level)
    else:
        seven = ''

    print('{}{}{}{}{}X{}{}'.format(one[hero.element_type], two, three, four, five, six, seven))



# -- START OF PROGRAM --

print('{0} ELEMENTS {0}'.format('-'*10))
time.sleep(2)
print('An RPG game on the four powers of life')
time.sleep(2)
print()

# main_menu()

# include try/except using keyboard interruption where if the user wants to leave
# at any time, they can do so and end the game abruptly

# play_again = input('Interesting game right? Wanna give it another try? [y/n]')
# if play_again.lower().startswith('y'):
#     main_menu()

# private variables. move these later
# game_difficulty = 'normal'
# game_mode = 'scarce'
game_multiplier = 1.3
set_gameplay()
