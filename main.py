from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numba import jit
from game_logic import movement_settings, selected_block_pick, texture_name_for_pick

app = Ursina()

# importing textures

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
cobble_texture = load_texture('assets/cobble_block.png')
spruce_texture = load_texture('assets/spruce_block.png')
planks_texture = load_texture('assets/planks_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
image = load_texture('assets/image.png')

# window setup

window.title = 'Voxel.jpg-py pre-release 0.0.3'
window.icon = load_texture('/resources/blocks/textures/grass.png')
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = False

# declaration

block_pick = 1


# character controller
class Player(FirstPersonController):
    def __init__(self):
        super(Player, self).__init__()
        self.camera = camera
        self.speed = 8
        camera.fov = 100
        self.mouse = mouse
        self.in_menu = False
        self.crouching = False
        self.sprinting = False


# player actions
def update():
    global block_pick
    global hand

    block_pick = selected_block_pick(held_keys, block_pick)
    player.speed, camera.fov = movement_settings(held_keys)


# setting up the hand
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            scale=0.20,
            texture='assets/arm.png',
            rotation=Vec3(160, -5, 0),
            position=Vec2(0.5, -0.6)
        )


hand = Hand()


# setting up the cube
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5)

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                texture_name = texture_name_for_pick(block_pick)
                textures = {
                    'grass': grass_texture,
                    'stone': stone_texture,
                    'brick': brick_texture,
                    'dirt': dirt_texture,
                    'cobble': cobble_texture,
                    'spruce': spruce_texture,
                    'planks': planks_texture,
                    'image': image,
                }
                Voxel(position=self.position + mouse.normal, texture=textures[texture_name])

            if key == 'left mouse down':
                destroy(self)


# mouse locking
class Mouse:

    def __init__(self):
        self.enabled = False
        self.visible = False
        self.locked = True


# sky box
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture='sky_sunset',
            scale=150,
            double_sided=True)


# voxel positioning
for z in range(40):
    for x in range(40):
        for y in range(1):
            voxel = Voxel(position=(x, y, z))


# quit key
def input(key):
    if key == 'q':
        quit()


player = FirstPersonController()
sky = Sky()


if __name__ == '__main__':
    app.run()
