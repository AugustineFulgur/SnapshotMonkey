import pyautogui
import os
import time
import driver

def __Aexec__(i): #请照规范来，先确定CONFIG是否设置 然后执行自动化脚本
    os.system("start cmd.exe /max")
    time.sleep(1)
    pyautogui.typewrite("python {} --logon netkeyboard --rhost {} --proto http --rport 80".format(__Aconfig__(),i[0]))
    pyautogui.press("enter")
    time.sleep(3)
    #保存截图
    route=__Aname__()+i[0]+".png"
    area=driver.get_workarea()
    pyautogui.screenshot(region=(area[0],area[1],area[2],area[3])).save(route)
    #记得退出
    pyautogui.typewrite("exit")
    pyautogui.press("enter") 
    pyautogui.typewrite("exit")
    pyautogui.press("enter") 
    return route #方便写docx
    
def __Aname__(): #这里需要自定义
    return "poc-dahua"

def __Aconfig__():
    #请填写^ ^ SMBEXEC脚本路径
    return ""