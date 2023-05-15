import pyautogui
from time import sleep
mousepos=[]
sleep(3)
x1=pyautogui.position()[0]
y1=pyautogui.position()[1]
print(x1, y1) 
sleep(3)
x2=pyautogui.position()[0]
y2=pyautogui.position()[1]
print(x2, y2)
new1 = x2-x1
new2 = y2-y1
for x in [x1, y1, new1, new2]:
  mousepos.append(x)
print(mousepos) 
pyautogui.screenshot('test.png', region=mousepos)
