import pyautogui
import subprocess
import datetime
import time

def join(id, password):
    subprocess.call("C:\\Users\\Manu\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    while True:
        join1 = pyautogui.locateOnScreen('join1.png')
        if join1 != None:
            pyautogui.click(join1)
            print("Clicked Join 1")
            break
        else:
            print("Could not find join 1")
            time.sleep(2)

    while True:
        feild = pyautogui.locateOnScreen('feild.png')
        if feild != None:
            pyautogui.click(feild)
            print("Made the Input Feild active")
            pyautogui.typewrite(id)
            pyautogui.click(pyautogui.locateOnScreen('join2.png'))
            break
        else:
            print("Could not find the input feild")
            time.sleep(2)

    while True:
        feild2 = pyautogui.locateOnScreen('feild2.png')
        if feild2 != None:
            pyautogui.click(feild2)
            print("Made the Input Feild 2 active")
            pyautogui.typewrite(password)
            pyautogui.click(pyautogui.locateOnScreen('join3.png'))
            break
        else:
            print("Could not find the input feild 2")
            time.sleep(2)



while True:
    now = datetime.datetime.now()
    current_time = (now.strftime("%m-%d-%y %H:%M"))
    # 02-06-21 22:16

    if current_time == "02-09-21 21:15":
        join("727 1754 1387", "014604")
        break
    else:
        print("Not the time")
        time.sleep(10)