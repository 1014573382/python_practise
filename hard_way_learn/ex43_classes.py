from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):
    quips = [
        "You died, You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor():

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
             member and your last misson is to get the  neutron destruct
             bomb from the Weapons Armory, put is in the bridge, and
             blow the ship up after getting into an escape pod.
             
             You're running down the central corridor to the Weapons
             Armory when a Gothon jumps out, red scaly skin, dark grimy
             teeth, and evil clown costume flowing around his hate
             filled body. he's blocking the door to the Armory and
             about to pull a weapon to blast you.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon...
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser 
                past your head...
            """))
            return  'death'

        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy...
            """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'entral_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map():

    def __init__(self, start_scene):
        pass

    def next_scene(self, start_scene):
        pass

    def opening_scene(self):
        pass


a_map = Map('Central_corridor')
a_game = Engine(a_map)
a_game.play()

if __name__ == '__main__':
    death = CentralCorridor()
    death.enter()
