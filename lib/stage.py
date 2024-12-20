from airtest.core.api import *
import logging
from PIL import Image
import pytesseract

# create a logger by passing the name to getLogger
stage_logger = logging.getLogger('stage')
resource_stage_logger = stage_logger.getChild('resource_stage')

class Others():
    '''
        其他關卡小function
    '''
    def __init__(self):
        self.enery_filename = r"C:\Desktop\script\back_to_future_1999\log\detect_energy.png"

    def back_to_lobby(self):
        '''
            回到大廳
        '''
        touch(Template(r"picture\stage\back_to_lobby.png", record_pos=(-0.39, -0.245), resolution=(1920, 1080)))
    

    def finish_stage(self, time_consume):
        '''
            檢測關卡打玩了沒
        '''
        pos = wait(Template(r"picture\stage\stage_victory.png", record_pos=(0.216, -0.179), resolution=(1920, 1080), threshold=0.9), timeout=time_consume, interval=10)
        touch(pos)
        sleep(5)

    def cut_image(self, filename):
        '''
            圖片剪裁
        '''
        img = Image.open(filename)

        # 設定裁剪區域 (左, 上, 右, 下)
        left = 1700
        top = 20
        right = 1800
        bottom = 70
        cropped_img = img.crop((left, top, right, bottom))

        # 保存裁剪後的圖片
        return cropped_img

    def judge_enery(self, stage_consume):
        '''
            檢測體力
        '''
        snapshot(filename=self.enery_filename, msg="detect enery")
        image = self.cut_image(self.enery_filename)
        # opencv取得體力值
        number = pytesseract.image_to_string(image, config='--psm 6 outputbase digits')
        # 計算可打的次數
        count_times = int(number)/stage_consume
        return int(count_times)

    def repeat_stage(self, repeat_time, costom_repeat_time):
        '''
            加入自定義打關卡的次數
        '''
        if repeat_time >= costom_repeat_time:
            self.switch(costom_repeat_time)
        else:
            self.switch(repeat_time)

    def switch(self, input_value):
        '''
            選擇一次打幾次關卡
        '''
        touch(Template(r"picture\stage\select_repeat.png", record_pos=(0.126, 0.231), resolution=(1920, 1080)))
        return {
            1: lambda: touch(Template(r"picture\stage\x1.png", record_pos=(0.146, 0.185), resolution=(1920, 1080))),
            2: lambda: touch(Template(r"picture\stage\x2.png", record_pos=(0.144, 0.14), resolution=(1920, 1080))),
            3: lambda: touch(Template(r"picture\stage\x3.png", record_pos=(0.144, 0.089), resolution=(1920, 1080))),
            4: lambda: touch(Template(r"picture\stage\x4.png", record_pos=(0.147, 0.042), resolution=(1920, 1080)))
        }.get(input_value, lambda: touch(Template(r"picture\stage\x4.png", record_pos=(0.147, 0.042), resolution=(1920, 1080))))()
    
    def really_start_action(self, stage_consume, costom_repeat_time):
        '''
            開始關卡前的重複次數(包含總共打幾次)
        '''
         # 判斷體力夠打幾關
        count_times = self.judge_enery(stage_consume)
        # 因為finish_stage裡面的wait關係，必須寫在外面，不然會有bug(wait不會照interval的時間等待)
        while(count_times >= 1):
            self.repeat_stage(count_times, costom_repeat_time)
            touch(Template(r"picture\stage\start_repeat.png", record_pos=(0.378, 0.231), resolution=(1920, 1080)))
            self.finish_stage(150)
            count_times = self.judge_enery(stage_consume)


class ResourceStage():
    '''
        資源關卡：
            1. 意志解析 will_analysis()
            2. 塵埃運動 experience_stage()
            3. 鑄幣美學 money_stage()
    '''
    def __init__(self):
        self.support_func = Others()

    def will_analysis(self):
        '''
            資源關卡 意志解析 will_analysis()
        '''
        touch(Template(r"picture\stage\go_in_stage.png", record_pos=(0.303, -0.046), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\go_in_resource_stage.png", record_pos=(-0.263, 0.232), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\select_will_stage.png", record_pos=(0.268, -0.02), resolution=(1920, 1080)))
        sleep(3)
        touch(Template(r"picture\stage\will_stage_7.png", record_pos=(-0.149, 0.181), resolution=(1920, 1080)))
        sleep(3)
        touch(Template(r"picture\stage\start_action.png", record_pos=(0.406, 0.197), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\repeat_2.png", record_pos=(0.366, 0.23), resolution=(1920, 1080)))
        self.support_func.finish_stage(150)
        self.support_func.back_to_lobby()

    def experience_stage(self):
        '''
            資源關卡 塵埃運動 experience_stage()
        '''
        stage_consume = 25
        custom_times = 4
        touch(Template(r"picture\stage\go_in_stage.png", record_pos=(0.303, -0.046), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\go_in_resource_stage.png", record_pos=(-0.263, 0.232), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\select_experience_stage.png", record_pos=(-0.243, -0.017), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\experience_stage_6.png", record_pos=(-0.151, 0.184), resolution=(1920, 1080)))
        sleep(3)
        touch(Template(r"picture\stage\start_action.png", record_pos=(0.406, 0.197), resolution=(1920, 1080)))
        sleep(3)
        self.support_func.really_start_action(stage_consume, custom_times)
        self.support_func.back_to_lobby()


    def money_stage(self):
        '''
            資源關卡 鑄幣美學 money_stage()
        '''
        stage_consume = 25
        custom_times = 4
        touch(Template(r"picture\stage\go_in_stage.png", record_pos=(0.303, -0.046), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\go_in_resource_stage.png", record_pos=(-0.263, 0.232), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\select_money_stage.png", record_pos=(0.178, -0.014), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\money_stage_6.png", record_pos=(-0.149, 0.185), resolution=(1920, 1080)))
        sleep(3)
        touch(Template(r"picture\stage\start_action.png", record_pos=(0.406, 0.197), resolution=(1920, 1080)))
        sleep(3)
        self.support_func.really_start_action(stage_consume, custom_times)
        self.support_func.back_to_lobby()


class MainStage():
    '''
        主要關卡：
            1. 第一關 
            2. 第二關 
            3. 第三關 
            4. 第四關 stage_4_20()

    '''
    def __init__(self):
        self.main_support_func = Others()

    def stage_4_20(self):
        '''
            主要關卡 第四關 stage_4_20()
        '''
        stage_consume = 18
        custom_times = 2
        touch(Template(r"picture\stage\go_in_stage.png", record_pos=(0.303, -0.046), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\go_in_four_stage.png", record_pos=(0.324, -0.002), resolution=(1920, 1080)))
        sleep(5)
        swipe(Template(r"picture\stage\swipe_to_4_20.png", record_pos=(-0.113, 0.186), resolution=(1920, 1080)), vector=[0.5802, -0.0029], duration=0.3, steps=2)
        sleep(5)
        if(exists(Template(r"picture\stage\stage_4_20.png", record_pos=(0.101, 0.178), resolution=(1920, 1080)))):
            touch(Template(r"picture\stage\stage_4_20.png", record_pos=(0.101, 0.178), resolution=(1920, 1080)))
            sleep(5)
        touch(Template(r"picture\stage\hard_stage.png", record_pos=(0.382, -0.075), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"picture\stage\start_action_hard.png", record_pos=(0.405, 0.195), resolution=(1920, 1080)))
        sleep(5)
        self.main_support_func.really_start_action(stage_consume, custom_times)
        self.main_support_func.back_to_lobby()


