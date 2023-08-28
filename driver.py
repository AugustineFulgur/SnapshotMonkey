import pyautogui
import os
import time
import argparse
import cmds
from docx import Document
import pkgutil
import importlib
import re
import signal

DESCRIPTION='''
by AugustTheodor CatXicure\n
[猴子的命也是命！ Monkey lives matter!]\n
自动化猴子脚本 内网漏洞验证工具\n
目前支持 海康威视命令执行、FTP、SMBEXEC\n
如果要增加验证漏洞出POC 请参照cmds模块下的文件书写 文件会自动加载。\n
使用 python driver.py -t fscan扫描文件\n
'''

SNAPSHOT_MONKEY='''
 ::::::::  ::::    :::     :::     :::::::::   ::::::::  :::    :::  ::::::::  :::::::::::       ::::    ::::   ::::::::  ::::    ::: :::    ::: :::::::::: :::   ::: 
:+:    :+: :+:+:   :+:   :+: :+:   :+:    :+: :+:    :+: :+:    :+: :+:    :+:     :+:           +:+:+: :+:+:+ :+:    :+: :+:+:   :+: :+:   :+:  :+:        :+:   :+: 
+:+        :+:+:+  +:+  +:+   +:+  +:+    +:+ +:+        +:+    +:+ +:+    +:+     +:+           +:+ +:+:+ +:+ +:+    +:+ :+:+:+  +:+ +:+  +:+   +:+         +:+ +:+  
+#++:++#++ +#+ +:+ +#+ +#++:++#++: +#++:++#+  +#++:++#++ +#++:++#++ +#+    +:+     +#+           +#+  +:+  +#+ +#+    +:+ +#+ +:+ +#+ +#++:++    +#++:++#     +#++:   
       +#+ +#+  +#+#+# +#+     +#+ +#+               +#+ +#+    +#+ +#+    +#+     +#+           +#+       +#+ +#+    +#+ +#+  +#+#+# +#+  +#+   +#+           +#+    
#+#    #+# #+#   #+#+# #+#     #+# #+#        #+#    #+# #+#    #+# #+#    #+#     #+#           #+#       #+# #+#    #+# #+#   #+#+# #+#   #+#  #+#           #+#    
 ########  ###    #### ###     ### ###         ########  ###    ###  ########      ###           ###       ###  ########  ###    #### ###    ### ##########    ### '''

def get_modules():
    modules_name={}
    for filefiner, name, ispkg in pkgutil.iter_modules(cmds.__path__):
        print(filefiner,type(filefiner))
        print(name)
        print(ispkg)
        if not ispkg and "__Aexec__" in dir(name) and "__Aname__" in dir(name):
            modules_name[name.__Aname__()]=importlib.import_module(name) #如果标志方法在文件中，加入这个模块（话说python是不是有抽象类 不管了）
            #所以方法中必须带有__Aexec__和__Aname__ 前者执行自动化操作 后者对应FSCAN标志
    print("加载EXECS成功，共{}条。".format(modules_name.keys().__len__))
    return modules_name

def __main__():
    print(SNAPSHOT_MONKEY) #hzzmnl
    emodules=get_modules() #读取模块
    parser=argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-t",type=str,help="fscan文件",required=True)
    parser.add_argument("-name",type=str,help="输出doc文件名",required=True)
    argv=parser.parse_args()
    reg_blast=re.compile("([^\:\]]*)\:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:[0-9]{2,5}\:(.*)")#素一款正则表达式大师 虽然是多余的正则表达式大师
    #爆破与弱口令、未授权、匿名（合并一起写方便）
    reg_poc=re.compile("[\S]* ([\S]*) ([\S])*")#一款比较没什么用的正则表达式
    doc=Document() #打开新Docx
    p=doc.add_paragraph() #添加段落
    with open(argv.f) as fsc:
       deal_list=fsc.read().split()
       for i in deal_list:
           if i.startswith("[+]"): #如果带有[+]
                p.add_run(i) #带有[+]的都写进报告
                #如果符合规则 尝试提取信息
                try:
                    group=re.match(reg_blast,i).group()
                    #Aexec的参数和group匹配到的一样[+] [漏洞名] [IP][端口] [用户名 密码]|[匿名/未授权]
                    if group(1) in emodules.keys():
                        #匹配到对应的执行方式
                        print("匹配到{},IP{}".format(group(1),group(2)))
                        pic_route=emodules[group(1)].__Aexec__([group(2),group(3),group(4)]) #传入的是 IP 端口 用户名密码/未授权/匿名
                        doc.add_picture(pic_route)
                        os.remove(pic_route)
                except:
                    #那就不是上面这种 继续
                    try:
                        group=re.match(reg_poc,i).group()
                        #[URL] [POC名]
                        if group(1) in emodules.keys():
                            print("匹配到{},链接{}".format(group(1),group(2)))
                            emodules[group(1)].__Aexec__([group(2)])
                    except:
                        continue
    doc.save(argv.name) #保存docx
                    
if __name__=="__main__":
    __main__()