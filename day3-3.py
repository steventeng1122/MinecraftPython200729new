# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:58:21 2020

@author: user
"""

fe
import time,random

pos=mc.player.getPos()
while True:
    x=pos.x+random.uniform(-20,20)
    z=pos.z+random.uniform(-20,20)
    y=pos.y+30
    mc.spawnEntity(x,y,z,20,93)
    time.sleep(0.1)