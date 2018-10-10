from random import choice

class Dialogue:
    def __init__(self):
        pass


    def battle_introductions(self, enemy):
        introductions = [
            "A {} stands in your way! Prepare for battle!",
            "Your path is being blocked by a {}! Can you take him?",
            "Look here, a {} is sizing you up! Kill them",
            "You've stumbled across a {}, and he looks dangerous!",
            "All of a sudden a {} approaches! Stand your ground!",
            "You're face to face with a {}! And he's out for blood"
            ]

        return choice(introductions).format(enemy.name)

    def cutscenes(self, hero, level, mid=""):
        story = {
            "1": [], # Move the 'long ago...' part here
            "2": ['''"My friends have been corrupted" {} realized. There was something wrong witht them.''',
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
                '''{} now knew that he would be going up against his weakness. And it wouldn't be easy...'''],
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
            "10": [],
            "10A": ['''All of a sudden, the elements go wild...''',
                '''A strange anomoly appears, and it looks...so...menicing!''',
                ("It's time", "to fight", "ELEMATRIX!")]
        }

        key = str(level) if mid == "" else str(level)+mid

        return story[key]
