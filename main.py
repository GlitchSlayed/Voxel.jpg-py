from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numba import jit

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

    if held_keys['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    if held_keys['4']:
        block_pick = 4
    if held_keys['5']:
        block_pick = 5
    if held_keys['6']:
        block_pick = 6
    if held_keys['7']:
        block_pick = 7
    if held_keys['8']:
        block_pick = 8
    if held_keys['9']:
        block_pick = 9
    if held_keys['0']:
        block_pick = 0

    if held_keys['left control']:
        player.speed = 15
        camera.fov = 107

    elif held_keys['left shift']:
        player.speed = 5
        camera.fov = 92
    else:
        player.speed = 8
        camera.fov = 100


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
                if block_pick == 1:
                    Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3:
                    Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4:
                    Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 5:
                    Voxel(position=self.position + mouse.normal, texture=cobble_texture)
                if block_pick == 6:
                    Voxel(position=self.position + mouse.normal, texture=spruce_texture)
                if block_pick == 7:
                    Voxel(position=self.position + mouse.normal, texture=planks_texture)
                if block_pick == 8:
                    Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 9:
                    Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 0:
                    Voxel(position=self.position + mouse.normal, texture=image)

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
app.run()
