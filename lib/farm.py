from airtest.core.api import *
import logging

# create a logger by passing the name to getLogger
farm_logger = logging.getLogger('farm')

class CollectFarm():
    '''
        收取資源
    '''
    def __init__(self):
        pass

    def notfound(self):
        '''
            點擊螢幕中間下方一次
        '''
        touch((930,930))

    def run(self):
        '''
            執行農場收菜
        '''
        touch(Template(r"picture\farm\farm_logo.png", record_pos=(0.288, 0.031), resolution=(1920, 1080)))
        sleep(10)
        touch(Template(r"picture\farm\farm_money.png", record_pos=(0.086, -0.177), resolution=(1920, 1080)))
        sleep(2)
        touch(Template(r"picture\farm\farm_experience_package.png", record_pos=(-0.089, -0.133), resolution=(1920, 1080)))
        sleep(2)
        touch(Template(r"picture\farm\farm_personal_trustworthy.png", record_pos=(-0.453, -0.127), resolution=(1920, 1080)))
        sleep(5)
        touch((1467,461))
        sleep(2)
        pos = wait(Template(r"picture\farm\farm_back.png", record_pos=(-0.466, -0.244), resolution=(1920, 1080)), timeout=40, interval=10, intervalfunc=self.notfound)
        touch(pos, duration=2, times=3)