from airtest.core.api import *
import logging

# create a logger by passing the name to getLogger
reward_logger = logging.getLogger('reward')
# reception_room_logger = reward_logger.getChild('reception_room')

class GetReward():
    '''
        獎勵類型
    '''
    def __init__(self):
        pass

    def daily_task(self):
        '''
            每日任務獎勵
        '''
        touch(Template(r"picture\reward\reward_daily_task_logo.png", record_pos=(-0.439, -0.069), resolution=(1920, 1080)))
        sleep(3)
        touch(Template(r"picture\reward\reward_get_all.png", record_pos=(0.415, -0.16), resolution=(1920, 1080)))
        sleep(2)
        #點一下中間下面
        touch((930,930))
        sleep(2)
        touch(Template(r"picture\reward\reward_exit.png", record_pos=(-0.466, -0.247), resolution=(1920, 1080)))
        sleep(2)

    def monthly(self):
        '''
            通行證獎勵
        '''
        touch(Template(r"picture\reward\monthly_logo.png", record_pos=(-0.329, -0.229), resolution=(1920, 1080)))
        sleep(2)
        if exists(Template(r"picture\reward\reward_monthly_getall.png", record_pos=(0.374, 0.24), resolution=(1920, 1080))):
            touch(Template(r"picture\reward\reward_monthly_getall.png", record_pos=(0.374, 0.24), resolution=(1920, 1080)))
            sleep(2)
            touch((930,930))
            sleep(2)
        touch(Template(r"picture\reward\reward_exit.png", record_pos=(-0.466, -0.247), resolution=(1920, 1080)))
        sleep(2)

    def spec_reward(self):
        '''
            特別獎勵如7日活動等等
        '''
        touch(Template(r"picture\reward\reward_spec_reward_logo.png", record_pos=(-0.264, -0.229), resolution=(1920, 1080)))
        sleep(2)
        pos = wait(Template(r"picture\reward\reward_tomorrow_can_get.png", record_pos=(-0.168, 0.011), resolution=(1920, 1080)))
        pos = (pos[0] - 200, pos[1])
        touch(pos)
        sleep(2)
        touch((930,930))
        touch(Template(r"picture\reward\reward_exit.png", record_pos=(-0.466, -0.247), resolution=(1920, 1080)))
        sleep(2)

    def run_all(self):
        '''
            一次跑全部獎勵
        '''
        self.daily_task()
        self.monthly()
        self.spec_reward()
        


