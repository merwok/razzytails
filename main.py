#!/usr/bin/env python
import pygame

from loaders import initialize, load_map
from input_handlers import handle_events
from graphics import render
from const import GAME_STATES


def main():
    # Initialize display screen and load assets
    screen, config, player = initialize()
    level = load_map(config.start, player)
    game_state = GAME_STATES['main']
    # Run game loop
    game_loop(game_state, screen, config, level, player)


def game_loop(game_state, screen, config, level, player):
    while game_state != GAME_STATES['exit']:
        game_state = handle_events(game_state, config, level, player)
        # FIXME: Remove when raspberries are removed
        player_coordinate = player.x, player.y
        if player_coordinate in level.map.raspberry_coordinates:
            player.raspberries += 1
            level.map.raspberry_coordinates.remove(player_coordinate)
            game_state = GAME_STATES['dialog']
        #
        render(game_state, screen, config, level, player)

if __name__ == "__main__":
    main()
