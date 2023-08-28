import pyautogui
import os
import time

def __Aexec__(i): #请照规范来，先确定CONFIG是否设置 然后执行自动化脚本
    if(not __Aconfig__):
        print("{}配置未设置，此EXEC跳过".format(__Aname__))
        return
    os.system("start cmd.exe /max")
    time.sleep(0.5)
    user,password=i[2].split(" ")
    pyautogui.typewrite("ssh {}@{} -p {}".format(user,i[0],i[1]))
    pyautogui.press("enter")
    pyautogui.typewrite("yes")
    pyautogui.press("enter")
    pyautogui.typewrite(password)
    pyautogui.press("enter")
    time.sleep("0.5")
    pyautogui.typewrite("whoami")
    time.sleep(1)
    #保存截图
    route=__Aname__()+i+".png"
    pyautogui.screenshot().save(route)
    #记得退出
    pyautogui.typewrite("exit")
    pyautogui.press("enter")
    pyautogui.typewrite("exit")
    pyautogui.press("enter") 
    return route
    
def __Aname__():
    return "SSH"

def __Aconfig__(): #需要安装Windows SSH客户端
    pass