import pyautogui
import keyboard
from time import sleep
import os


os.environ['XAUTHORITY'] = '/home/kaleb/.Xauthority'

os.system('xauth generate :0 . trusted')

    
    
    
class regionfinder:
  x1 = None
  x2 = None
  def pos(self):
    position=pyautogui.position()
    if self.x1 == None:
      self.x1 = position[0]
      self.y1 = position[1]
      print(f'''pos1: x: {self.x1}  y: {self.y1}''')
    
    else:
      self.x2 = position[0]
      self.y2 = position[1]
      print(f'''pos2: x: {self.x2}  y: {self.y2}''')
      self.x2 = self.x2-self.x1
      self.y2 = self.y2-self.y1

  
  def screenshot(self):
    mousepos = [self.x1, self.y1, self.x2, self.y2]
    pyautogui.screenshot('test.png', region=mousepos)#type: ignore


rf = regionfinder()

while True: 
  if keyboard.is_pressed('i'):
    rf.pos()
    sleep(2)