import pyautogui
import os
import time
import driver

def __Aexec__(i): #请照规范来，先确定CONFIG是否设置 然后执行自动化脚本
    if(not __Aconfig__):
        print("{}配置未设置，此EXEC跳过".format(__Aname__))
        return
    os.system("start /max cmd.exe")
    time.sleep(0.5)
    pyautogui.typewrite("{} -u {} --cmd ls -l".format(__Aconfig__(),i[0]))
    pyautogui.press("enter")
    time.sleep(3)
    #保存截图
    route=__Aname__()+i+".png"
    area=driver.get_workarea()
    pyautogui.screenshot(region=(area[0],area[1],area[2],area[3])).save(route)
    #记得退出
    pyautogui.typewrite("exit")
    pyautogui.press("enter") 
    return route #方便写docx
    
def __Aname__():
    return "poc-yaml-hikvision-unauthenticated-rce-cve-2021-36260"

def __Aconfig__():
    #请填写^ ^ 脚本路径 并参照你使用脚本的具体命令进行修改
    return ""
