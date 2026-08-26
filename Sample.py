import pyautogui
import datetime
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0
print("open chrome...")
pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('alt','Space', 'x')
pyautogui.hotkey('x')
time.sleep(1)
pyautogui.typewrite('https://www.google.com/', interval=0.01) 
pyautogui.press('enter')
pyautogui.typewrite('Infy share price', interval=0.01) 
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(235, 500)
pyautogui.doubleClick()
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('win','r')
#pyautogui.typewrite('C:\\Users\\rpk18\\OneDrive\Desktop\\Infy Share Price.xlsx', interval=0.01)
pyautogui.typewrite('C:\\Users\\UNAIS\\Desktop\\Tamimi_XPO\\report.xlsx', interval=0.01)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'home')
pyautogui.hotkey('ctrl', 'down')
pyautogui.press('enter')
today_date = datetime.now().strftime("%Y-%m-%d")
pyautogui.typewrite(today_date, interval=0.05)
pyautogui.hotkey('tab')
pyautogui.hotkey('ctrl', 'alt', 'v')
pyautogui.hotkey('t')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 's')
pyautogui.hotkey('alt', 'f4')
pyautogui.hotkey('alt', 'f4')

print("Infy Share price copied for today...")