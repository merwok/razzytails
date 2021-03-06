"""Defines transitions and callbacks for the game's fsm"""

from yape.fsm import FSM

# FSM transitions
transitions = [
    {
        'name': 'answer',
        'source': 'question',
        'destination': 'main',
    },
    {
        'name': 'item_collected',
        'source': 'item',
        'destination': 'main',
    },
    {
        'name': 'popup_question',
        'source': 'main',
        'destination': 'question'
    },
    {
        'name': 'popup_item',
        'source': 'main',
        'destination': 'item'
    },
    {
        'name': 'exit',
        'source': 'main',
        'destination': 'exit'
    },
    {
        'name': 'exit',
        'source': 'question',
        'destination': 'exit'
    },
    {
        'name': 'exit',
        'source': 'item',
        'destination': 'exit'
    },
    {
        'name': 'exit',
        'source': 'splash',
        'destination': 'exit'
    },
    {
        'name': 'exit',
        'source': 'endscreen',
        'destination': 'exit'
    },
    {
        'name': 'start',
        'source': 'splash',
        'destination': 'main'
    },
    {
        'name': 'end',
        'source': 'main',
        'destination': 'endscreen'
    },
    {
        'name': 'popup_info',
        'source': 'main',
        'destination': 'info'
    },
    {
        'name': 'info_closed',
        'source': 'info',
        'destination': 'main'
    },
]


# FSM callbacks
def add_item_to_inventory(player, item):
    player.items.append(item)
    player.current_item = item
    return True


def handle_answer(is_correct, level, player):
    if is_correct:
        # Remove all monsters on the player's current location
        for monster in level.monsters:
            if (monster.x, monster.y) == (player.x, player.y):
                level.monsters.remove(monster)
                level.monster_coordinates.pop(monster.id)
    else:
        level.reset_items(player)
        level.reset_monsters()
        game_state.popup_info()


def handle_item_collected(level, player):
    if len(level.items) == len(player.items):
        # no more items. you win!
        game_state.end()


callbacks = {
    'on_before_popup_item': add_item_to_inventory,
    'on_answer': handle_answer,
    'on_item_collected': handle_item_collected,
}

game_state = FSM('splash', transitions, callbacks)
