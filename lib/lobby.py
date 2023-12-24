from airtest.core.api import *
import logging
from win10toast import ToastNotifier

# create a logger by passing the name to getLogger
lobby_logger = logging.getLogger('lobby')

class GoInLobby():
    '''
        點擊圖示進入重返未來1999
    '''
    def __init__(self):
        pass

    def notfound(self):
        '''
            找不到圖片的錯誤通知
        '''
        lobby_logger.debug("No target found picture:lobby_start_game")
        toaster = ToastNotifier()
        toaster.show_toast("something error", icon_path="f.ico", duration=10)

    def run(self):
        '''
            執行lobby程式
        '''
        lobby_logger.debug("infra_logo")
        touch(Template(r"picture\lobby\lobby_1999_logo.png", record_pos=(0.082, -0.097), resolution=(1920, 1080)))
      
        # 公告
        if exists(Template(r"picture\lobby\lobby_announcement.png", record_pos=(0.419, -0.197), resolution=(1920, 1080))):
            touch(Template(r"picture\lobby\lobby_announcement.png", record_pos=(0.419, -0.197), resolution=(1920, 1080)))
        
        # 開始遊戲
        pos = wait(Template(r"picture\lobby\lobby_start_game.png", record_pos=(-0.004, 0.135), resolution=(1920, 1080)), timeout=40, interval=10, intervalfunc=self.notfound)
        touch(pos)

        # 剩下是新的一天的判斷式
        sleep(20)
        if exists(Template(r"picture\lobby\lobby_prelobby.png", record_pos=(-0.465, -0.243), resolution=(1920, 1080))):
            touch(Template(r"picture\lobby\lobby_prelobby.png", record_pos=(-0.465, -0.243), resolution=(1920, 1080)))
        #點一下中間下面
        touch((930,930))
        #點一下中間左邊
        touch((380,520))




