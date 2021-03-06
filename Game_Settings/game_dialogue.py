from random import choice

class Dialogue:
    def __init__(self):
        pass

    def tutorial_text(self, keyword):
        advice = {
            "main": ['''Welcome!
                    In ELEMENTS, heroes and enemies are based on one of four types: Water, Earth, Fire, and Air
                    Each type has a weakness (Water <--> Fire, Earth <--> Air) that can be used to your or your opponents advantage
                    {}''',
                    '''Your hero will start out with 100 life points and 50 magic points. Enemies will vary
                    Enemy damage will reduce your LP, and special/weapon attacks will reduce your MP
                    MP will increase by 5 after every turn, while LP will not increase until level ends
                    If your LP hits zero, it's game over
                    {}''',
                    '''Each time you beat an enemy, you gain XP and Coins
                    Higher XP leads to greater hero damage, and you can use coins in the shop (more on this later)
                    {}''',
                    '''Shop and fusions will be explained during the game
                    You're ready to pick your hero
                    {}'''],
            "shop": '''Welcome to the shop!
                    This is where you can buy things for {0} that will help in battles.
                    For example, {0} has {1} coins, and {2} costs 100 coins. You can buy it now.
                    Also, you see {0}'s XP. Higher XP leads to more impactful attacks.
                    I'll let you take a look around.''',
            "fusion": [],
        }

        return advice[keyword]


    def battle_introductions(self):
        introductions = [
            "A {} stands in your way! Prepare for battle!",
            "Your path is being blocked by a {}! Can you take him?",
            "Look here, a {} is sizing you up! Kill them",
            "You've stumbled across a {}, and he looks dangerous!",
            "All of a sudden a {} approaches! Stand your ground!",
            "You're face to face with a {}! And he's out for blood"
            ]

        return choice(introductions)

    def cutscenes(self, level, mid=""):
        story = {
            "1": ['''Long ago, the world was balanced by the elemental forces that were
                bestowed, in equal strength and harmony.''',
                '''But an evil entity took advantage of such strengths and created chaos,
                unleashing havoc by corrupting the guardians of the elements and the ones
                who serve them.''',
                '''Now, it is up to {} to restore order, and bring an end to great evil once and
                for all...'''], # Move the 'long ago...' part here
            "2": ['''"My friends have been corrupted" {} realized. There was something wrong with them.''',
                '''Never had other tribes been so hostile to each other. Not for centuries.''',
                '''"There must be something in the air," the warrior thought, "or the way the stars have aligned"''',
                '''Confused, and determined to seek the issue, they carried on...'''],
            "3": ['''"This seems odd", {} said. The approaching area felt so familiar...''',
                '''The symbols on the walls were identical to their own''',
                '''Suddenly {} realized. "Oh no!" the warrior said. "My own people have been corrupted!"'''],
            "4": ['''{}'s heart became filled with sadness after fighting their own people''',
                '''"I will end this evil presence!" the hero declared. "Then all will return to normal"''',
                '''But as {} was pondering, a shadow appeared...''',
                '''A force that had the exact opposite sign.''',
                '''{} now knew that they would be going up against their weakness. And it wouldn't be easy...'''],
            "5": ['''Now {} realized that they were getting closer to the great force that corrupted the world.''',
                '''Having defeated each of the elements, their confidence seemed to get higher.''',
                '''As {} kept walking, they noticed symbols that they had already came across.''',
                '''"Is this a place I already visited?", they wondered. "Or...a stronger tribe of an element before?"''',
                '''Ready for anything, {} carried on...'''],
            "6": ['''{} hadn't truly realized how many people were corrupted by this dark spirit.''',
                '''It was clear that the people of this world needed help to overcome this''',
                '''But what {} still wondered, was why this was still happening?''',
                '''Then, just over the hill, a raged man charged at the hero...'''],
            "7": ['''Now, more determined than ever, {} traversed faster, hoping the answer lie ahead.''',
                '''They were emotionally weakened by witnessing what the darkness had done to their friends.''',
                '''Suddenly, {} felt a strong force. A presence, distant but there.''',
                '''Then it went away. "What was that?" said the hero.''',
                '''"Could I be getting closer to the source? Will I be victorious soon?"''',
                '''The presence returned, this time saying...''',
                '''"...ultimate power..."'''],
            "8": ['''"Man, this feels weird" {} stated. They were getting closer to a force they had never encounted.''',
                '''It was clear that they were getting closer to the source of it all.''',
                '''As the horizon became more clear, {} saw a large tower. It looked as if sparks randomly surrounded it.''',
                '''"I don't know what element habits this place" the warrior said, "but it can't be good..."'''],
            "8A": ['''The two bosses began to merge into one!''',
                '''With both elements changed, this new monster emitted jolts of lightning!'''],
            "9": ['''A voice called out to {}...''',
                '''"MERE MORTAL" it said, "YOU WILL SUBMIT TO THE ULTIMATE POWER!"''',
                '''{} was ready to fight back. "Who are you?" they replied. "And why are you here?"'''
                '''"I AM ELEMATRIX" shouted the voice, "AND YOU WILL LEARN TO OBEY ME!"''',
                '''"I will never let you rule!" {} shouted. "I will save my friends and restore humanity!"''',
                '''"IF YOU WILL NOT COME WILLINGLY..."''',
                '''"THEN I SHALL SEND AN ARMY OF YOUR WEAKNESS AT YOU. HAHAHA..."'''],
            "10": ['''"Show yourself!" {} cried out to Elematrix. "I will defeat you and save the world!"''',
                '''"IS THAT SO?" Elematrix replied. "YOU WISH TO BE DEFEATED SO SOON?"''',
                '''The hero was not in the mood for games. "You will face me! Right here, right now!"''',
                '''It was at that point that the world around {} began to change...''',
                '''The sky darkened, the water disappeared, and the ground shifted to something unknown.''',
                '''Alone and confused, {} yelled, "What is going on?!? Where am I? Answer me!"''',
                '''"IF YOU WANT TO FACE ME, YOU WILL DO SO ON MY FIELD" Elematrix answered. "BUT FIRST..."''',
                '''"I WILL THROW EVERY TYPE OF ELEMENT YOUR WAY. AND IF YOU SURVIVE, I'LL BE GLAD TO ANNIHILATE YOU MYSELF!""'''],
            "10A": ['''All of a sudden, the elements go wild...''',
                '''A strange anomoly appears, and it looks...so...menicing!''',
                ("It's time", "to fight", "ELEMATRIX!")]
        }

        key = str(level) if mid == "" else str(level)+mid

        return story[key]
