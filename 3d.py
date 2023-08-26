from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController
app = Ursina()
player = FirstPersonController()

for i in range(-5,6):
    grass_block = Entity(mode = 'cube',color=color.gray,collider='box,position = (i,0,i)')
    i += 1
app.run()