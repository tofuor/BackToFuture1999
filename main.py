__author__ = "FU"

from airtest.core.api import *
import pytesseract
from PIL import Image
import os, sys
import logging
import math

# 添加當前腳本所在的資料夾到 Python 路徑
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

from lib import lobby, farm, stage, reward

# auto_setup(__file__)
logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)
logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)

go_lobby = lobby.GoInLobby()
go_farm = farm.CollectFarm()
go_reward = reward.GetReward()
go_stage = stage.ResourceStage()
go_main_stage = stage.MainStage()

# 每次開啟都能做的
# go_lobby.run()
# go_farm.run()
# go_stage.experience_stage()
# go_stage.money_stage()
go_main_stage.stage_4_20()

# 每天僅一次
# go_stage.will_analysis()
# go_reward.run_all()




