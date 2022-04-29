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

    
while True:
    sleep(5.0)
    if exists(Template(r"tpl1651273382652.png", record_pos=(-0.125, 0.022), resolution=(810, 1440))):
        reset()
    touch([630,700])
    


