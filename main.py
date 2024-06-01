import pyautogui
import keyboard
from time import sleep

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
    self.mousepos = [self.x1, self.y1, self.x2, self.y2]
    pyautogui.screenshot('test.png', region=self.mousepos)#type: ignore


rf = regionfinder()

while True: 
  if keyboard.is_pressed('shift'):
    rf.pos()
    sleep(1) #? Here so that it doesn't accidentally take both regions at the same time
  if not rf.x2 == None:
    try:
      rf.screenshot()
      print(rf.mousepos)
      print('Take a look at your image at "test.png"')
      exit()
    except ValueError as e:
      print("Coordinate 'right' is Les than 'left', try again but this time press the top left of your image first!")
      exit()
