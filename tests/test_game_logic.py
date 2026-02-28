from game_logic import movement_settings, selected_block_pick, texture_name_for_pick


def test_selected_block_pick_defaults_to_current_when_no_numeric_key_pressed():
    held_keys = {'left control': True}
    assert selected_block_pick(held_keys, current_pick=4) == 4


def test_selected_block_pick_updates_on_numeric_key_press():
    held_keys = {'3': True}
    assert selected_block_pick(held_keys, current_pick=1) == 3


def test_movement_settings_prioritizes_sprint_over_crouch():
    held_keys = {'left control': True, 'left shift': True}
    assert movement_settings(held_keys) == (15, 107)


def test_movement_settings_crouch_values():
    held_keys = {'left shift': True}
    assert movement_settings(held_keys) == (5, 92)


def test_texture_name_for_pick_mappings():
    assert texture_name_for_pick(1) == 'grass'
    assert texture_name_for_pick(8) == 'dirt'
    assert texture_name_for_pick(0) == 'image'
