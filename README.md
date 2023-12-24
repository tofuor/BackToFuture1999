#
## Enviroment
1. windows 10
2. python 3.10.7

### 創建環境
```
python -m venv back_to_furture_1999_env

.\back_to_furture_1999_env\Scripts\activate

pip install -r requirements.txt
```

### 執行腳本
1. 確認adb連接
```
adb kill-server 
adb start-server
adb device
```
2. 連接伺服器並執行腳本
```
& "C:\Desktop\script\back_to_future_1999\back_to_furture_1999_env\Scripts\python.exe" -u "D:\AirtestIDE\sample\custom_launcher.py" "C:\Desktop\script\back_to_future_1999\main.py" --device "android://127.0.0.1:5037/emulator-5554?cap_method=JAVACAP&ori_method=ADBORI&touch_method=ADBTOUCH" --log "C:\Desktop\script\back_to_future_1999\log"

```