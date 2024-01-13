@echo off
setlocal

set "deviceFound=false"

for /f "tokens=*" %%i in ('adb devices ^| findstr /R /C:"device$"') do (
    set "deviceFound=true"
)

echo "%deviceFound%"

if "%deviceFound%"=="false" (
    adb kill-server
    adb start-server
    timeout 5
)

@echo off
call "C:\Desktop\script\back_to_future_1999\back_to_furture_1999_env\Scripts\python.exe" -u "D:\AirtestIDE\sample\custom_launcher.py" "C:\Desktop\script\back_to_future_1999\main.py" --device "android://127.0.0.1:5037/emulator-5554?cap_method=JAVACAP&ori_method=ADBORI&touch_method=ADBTOUCH" --log "C:\Desktop\script\back_to_future_1999\log"

endlocal