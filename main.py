#!/usr/bin/env python

import sys
import time

import pygame
from pygame.constants import KEYUP, KEYDOWN, K_ESCAPE, QUIT

from loaders import initialize, load_map
from input_handlers import handle_key
from graphics import render


def main(*args):
    # Initialize display screen and load assets
    assets = initialize()
    map_data = load_map('map1.json')
    player = map_data['map_data']['player_start']
    player['raspberries'] = 0
    while True:
        # Exit on escape key or X
        for event in pygame.event.get():
            pressed_escape = event.type == KEYUP and event.key == K_ESCAPE
            if pressed_escape or event.type == QUIT:
                return
            if event.type == KEYDOWN:
                handle_key(event.key, map_data, player)
        time.sleep(0.05)
        raspberry_coordinates = map_data['raspberry_coordinates']
        player_coordinate = player['x'], player['y']
        if player_coordinate in raspberry_coordinates:
            player['raspberries'] += 1
            raspberry_coordinates.remove(player_coordinate)
        render(assets, map_data, player)


if __name__ == "__main__":
    main(sys.argv)