# -*- encoding=utf8 -*-
__author__ = "izanavi"

from airtest.core.api import *

auto_setup(__file__)

while True:
    touch(Template(r"tpl1648007594250.png", record_pos=(0.002, 0.411), resolution=(540, 960)))
    sleep(35.0)
    while True:
        if exists(Template(r"tpl1648008354634.png", record_pos=(-0.004, -0.77), resolution=(540, 960))):
            break
        else:
            sleep(7.0)
    for i in range(10):
        touch([213,904])
        sleep(0.2)
    sleep(3.0)
    while True:
        if not exists(Template(r"tpl1648008930348.png", record_pos=(-0.004, 0.815), resolution=(540, 960))):
            touch([213,904])
        else:
            break
    touch(Template(r"tpl1648009086566.png", record_pos=(-0.052, -0.13), resolution=(540, 960)))
    if exists(Template(r"tpl1648009098507.png", record_pos=(-0.235, 0.261), resolution=(540, 960))):
        touch(Template(r"tpl1648009098507.png", record_pos=(-0.235, 0.261), resolution=(540, 960)))
