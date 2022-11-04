import pywhatkit as w
import pyautogui
import keyboard as k
import time

def whatmsg(telef, notaw):
  #w.sendwhatmsg_instantly(telef, notaw)# este manda solo a un contacto
  w.sendwhatmsg_to_group_instantly(telef, notaw)
  time.sleep(2)
  pyautogui.click()
  time.sleep(1)
  k.press_and_release('enter')

msg = ["Hello, My dear family", "Good morning, Welcome to the city"]

whatmsg("DyONhoQJFAoD4JOuNwN8TN", "test python")