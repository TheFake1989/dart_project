#function import
from models.player import *

def around_the_world(players):
    for player in players:
        player.score = 1
        player.game = "around_the_world"
        player.throws = []


def shoot_down(players, shoot_down_target):
    for player in players:
        player.score = shoot_down_target
        player.game = "shoot_down"
        player.throws = []