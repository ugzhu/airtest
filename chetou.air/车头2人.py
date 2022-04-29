# -*- encoding=utf8 -*-
__author__ = "zhaohongliang"

from airtest.core.api import *

auto_setup(__file__)

while True:
    while True:
        if not exists(Template(r"tpl1643439635940.png", threshold=0.8, rgb=True, record_pos=(-0.157, -0.487), resolution=(702, 1248))):
            sleep(2.0)
        else:
            touch(Template(r"tpl1638464761109.png", record_pos=(0.006, 0.381), resolution=(1080, 1920)))
            break
    while True:
        if not exists(Template(r"tpl1643439467523.png", record_pos=(-0.466, -0.788), resolution=(702, 1248))):
            sleep(2.0)
        else:
            sleep(8.0)
            touch(Template(r"tpl1643439467523.png", record_pos=(-0.466, -0.788), resolution=(702, 1248)))
            break
    touch(Template(r"tpl1638464581956.png", record_pos=(-0.449, 0.826), resolution=(1080, 1920)))
    touch(Template(r"tpl1638464874010.png", record_pos=(0.233, 0.264), resolution=(1080, 1920)))
    sleep(2.0)
    touch(Template(r"tpl1638465228396.png", record_pos=(-0.003, 0.381), resolution=(1080, 1920)))
    sleep(4.0)
    if exists(Template(r"tpl1638464874010.png", record_pos=(0.233, 0.264), resolution=(1080, 1920))):
        touch(Template(r"tpl1638464874010.png", record_pos=(0.233, 0.264), resolution=(1080, 1920)))
    sleep(4.0)
    touch(Template(r"tpl1638464890326.png", record_pos=(-0.057, 0.256), resolution=(1080, 1920)))
    sleep(1.0)
    touch(Template(r"tpl1638465336347.png", record_pos=(0.227, 0.394), resolution=(1080, 1920)))