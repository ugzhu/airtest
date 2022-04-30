# -*- encoding=utf8 -*-
__author__ = "Yujie Zhu"

from airtest.core.api import *

auto_setup(__file__)

def reset():
    touch([690,300])
    sleep(3.0)
    touch([590,920])
    sleep(3.0)
    touch([400,910])

def mail():
    touch([190, 1375])
    sleep(10.0)
    touch([730, 933])
    sleep(10.0)
    touch([636,1222])
    sleep(10.0)
    touch([592, 927])      
    sleep(10.0)
    touch([424, 924]) 
    sleep(10.0)
    touch([181, 1359]) 
    sleep(10.0)
    touch([120, 1233]) 
    sleep(10.0)
    touch([367, 523]) 
    sleep(10.0)
    touch([744, 660]) 
    sleep(10.0)
    
    
    
while True:
    sleep(3.0)
    if exists(Template(r"tpl1651273382652.png", record_pos=(-0.125, 0.022), resolution=(810, 1440))):
        sleep(5.0)
        reset()
        
    touch([630,700])
    if exists(Template(r"tpl1651275516642.png", record_pos=(-0.015, -0.005), resolution=(810, 1440))):
        sleep(5.0)
        mail()


