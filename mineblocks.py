# Author: Creative Portal
# Title: MineBlocks
# Company: Creative Team
# Date of the Result: 25.12.21 
# IF YOU NEED HELP OR CONTACT: creativeportal92012@gmail.com
# Github: creative-portal

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

block_pick = 1

# update
def update():
       global block_pick

       # if-statement for the block pick
       if held_keys['1']: 
              block_pick = 1
       elif held_keys['2']: 
              block_pick = 2                                     
       elif held_keys['3']: 
              block_pick = 3
       elif held_keys['4']: 
              block_pick = 4

# voxel class
class Voxel(Button):

       # private init method
       def __init__(
              self, 
              position = (0, 0, 0), 
              texture = 'white_cube', 
              color = color.green
       ):
              super().__init__(
                     parent = scene,
                     position = position,
                     model = 'cube',
                     origin_y = 0.5,
                     texture = texture,
                     color = color
              )     

       # input
       def input(self, key):
              if self.hovered:
                     if key == 'left mouse down':
                            destroy(self)
                               
                     elif key == 'right mouse down':
                            if block_pick == 1:
                                   voxel = Voxel(
                                          position = self.position + mouse.normal,
                                          texture = 'brick', 
                                          color = color.pink
                                   )
                                   
                            elif block_pick == 2:
                                   voxel = Voxel(
                                          position = self.position + mouse.normal, 
                                          color = color.gray
                                   )
                                  
                            elif block_pick == 3:
                                   voxel = Voxel(
                                          position = self.position + mouse.normal, 
                                          color = color.brown
                                   )
                                   
                            elif block_pick == 4:
                                   voxel = Voxel(
                                          position = self.position + mouse.normal, 
                                          texture = 'white_cube', 
                                          color = color.green
                                   )
                                   

# sky class
class Sky(Entity):
       def __init__(self):
              super().__init__(
                     parent = scene,
                     model = 'sphere',
                     color = color.cyan,
                     scale = 150,
                     double_sided = True
              )

app = Ursina()

for vxls_z in range(45):
       for vxls_x in range(45):
              voxel = Voxel(
                     position = (
                            vxls_x, 
                            0, 
                            vxls_z
                     )
              )

player = FirstPersonController()
sky = Sky()

app.run()