"""Pure game logic helpers that can be tested without Ursina runtime."""

from typing import Any, Mapping


BLOCK_PICK_KEYS = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0,
}

BLOCK_PICK_TEXTURES = {
    1: 'grass',
    2: 'stone',
    3: 'brick',
    4: 'dirt',
    5: 'cobble',
    6: 'spruce',
    7: 'planks',
    8: 'dirt',
    9: 'brick',
    0: 'image',
}


def selected_block_pick(held_keys: Mapping[str, Any], current_pick: int) -> int:
    """Return the active block pick based on numeric key presses."""
    for key, value in BLOCK_PICK_KEYS.items():
        if held_keys.get(key):
            return value
    return current_pick


def movement_settings(held_keys: Mapping[str, Any]) -> tuple[int, int]:
    """Return (player_speed, camera_fov) based on movement modifiers."""
    if held_keys.get('left control'):
        return 15, 107
    if held_keys.get('left shift'):
        return 5, 92
    return 8, 100


def texture_name_for_pick(block_pick: int) -> str:
    """Return the symbolic texture name for a given block selection."""
    return BLOCK_PICK_TEXTURES[block_pick]
