import pyautogui
import os
import time
import driver

def __Aexec__(i): #请照规范来，先确定CONFIG是否设置 然后执行自动化脚本
    os.system("start /max cmd.exe")
    time.sleep(0.5)
    pyautogui.typewrite("ftp  {} {}".format(i[0],i[1]))
    pyautogui.press("enter")
    upp=1[2].split(" ")
    if upp.__len__()==1: #这个模式只有anonymous
        pyautogui.typewrite("anonymous")
        pyautogui.press("enter")
    else:
        pyautogui.typewrite(upp[0])
        pyautogui.press("enter")
        pyautogui.typewrite(upp[1])
        pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.press("enter")
    #保存截图
    route=__Aname__()+i+".png"
    area=driver.get_workarea()
    pyautogui.screenshot(region=(area[0],area[1],area[2],area[3])).save(route)
    #记得退出
    pyautogui.typewrite("exit")
    pyautogui.press("enter")
    return route 
    
def __Aname__():
    return "FTP"

def __Aconfig__():
    pass