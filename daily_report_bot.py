import pyautogui
import time
import os
#import datetime

from datetime import datetime

#now =datetime.now().strftime("%Y-%m-%D %H:%M:%S")

now = datetime.now()

date_time = now.strftime("%Y-%m-%d %H:%M:%S")
file_date = now.strftime("%Y-%m-%d")

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("Step 1:Open the chrome browser...")

#Open the start  menu
pyautogui.press('win')
time.sleep(1)

#Type Chrome
pyautogui.write('chrome',interval=0.1)
time.sleep(1)

#Press enter
pyautogui.press('enter')
time.sleep(2)

#go to any website
print("Step 2:Go to the website...")
pyautogui.hotkey('ctrl', 't', interval=0.1)
time.sleep(1)
pyautogui.write('https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671', interval=0.15)
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

#Data copy 
print("Step 3: Copy the full data of the website...")
pyautogui.hotkey('ctrl', 'a', interval=0.1)
time.sleep(1)
pyautogui.hotkey('ctrl', 'c', interval=0.1)
time.sleep(1) 

#Open the excel and paste the copied content
print("Step 4: Open the excel editor and paste the data...")
pyautogui.press('win')
time.sleep(1)
pyautogui.write('excel', interval=0.15)
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

#Create new work book 
pyautogui.press('enter')
time.sleep(5)

#select the particular cell and put the data
pyautogui.hotkey('ctrl','g')
pyautogui.write('A1')
pyautogui.press('enter')
pyautogui.typewrite(date_time)

pyautogui.press('down')
pyautogui.hotkey('ctrl', 'v', interval=0.1)
time.sleep(3)

filename=f"daily_report_{datetime.now().strftime('%Y-%m-%D')}.xlsx"
pyautogui.hotkey('ctrl','shift','s')
time.sleep(3)

'''
file_path=r"C:\Users\UNAIS\Desktop\Tamimi_XPO\report.xlsx"
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(file_path, interval=0.01)
pyautogui.press("enter")
'''
