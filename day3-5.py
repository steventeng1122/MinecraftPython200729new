# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:41:22 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
def plantree (x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,46)
    mc.setBlocks(x,y,z,x,y+4,z,17)
ex,y,z=mc.player.getTilePos()
for i in range(10):
    plantree(x+7*i,y,z+0)
    plantree(x+7*i,y,z+7)
    plantree(x+7*i,y,z+14e)