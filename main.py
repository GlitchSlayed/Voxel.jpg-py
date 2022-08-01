from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

# importing textures

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')

# window setup

window.title = 'Voxel.jpg-py pre-release 0.0.1'
window.icon = load_texture('/resources/blocks/textures/grass.png')
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = False

# declaration

camera.fov = 100
camera.clip_plane_near = 0.1
camera.clip_plane_far = 1000

block_pick = 1


# setting up the hand
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture='assets/arm',
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6))

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


# player actions

def update():
    hand = Hand()
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

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

# setting up the cube
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5)
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 5: voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 6: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 7: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 8: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 9: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 0: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)

            if key == 'left mouse down':
                destroy(self)

# mouse locking

class Mouse():

    def __init__(self):
        self.enabled = False
        self.visible = False
        self.locked = True


# voxel positioning
for z in range(45):
    for x in range(45):
        for y in range (1):
            voxel = Voxel(position=(x, y, z))


# quit key
def input(key):
    if key == 'q':
        quit()


player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
