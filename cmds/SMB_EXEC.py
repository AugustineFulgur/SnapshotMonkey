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
    user,password=i[2].split(" ") #这个没有匿名模式
    pyautogui.typewrite("{} {}:{}{} -codec gb2312".format(__Aconfig__,user,password,i[0]))
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("whoami\n")
    pyautogui.press("enter")
    time.sleep(2)
    #保存截图
    route=__Aname__()+i+".png"
    area=driver.get_workarea()
    pyautogui.screenshot(region=(area[0],area[1],area[2],area[3])).save(route)
    #记得退出
    pyautogui.typewrite("exit")
    pyautogui.press("enter") 
    return route
    
def __Aname__():
    return "SMB"

def __Aconfig__():
    #请填写^ ^ SMBEXEC脚本路径
    return ""