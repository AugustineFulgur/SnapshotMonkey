# SnapshotMonkey 
## 根据fscan扫描报告自动化验证内网漏洞并将截图导入报告的小工具~

`by AugustTheodor_CatXicure`

### 使用方式： python driver.py -f fscan扫描文件位置 -name 输出docx文件位置 
目前支持 
1. SSH 
2. SMB 
3. FTP 
4. 一个用作示例的海康威视RCE（依葫芦画瓢可以改出其他python等文件POC）
5. 大华RCE

环境配置请看 Introduction.md **使用前务必查看此md文件并配置环境，除非你只验证FTP/SSH这两个** 欢迎提交EXEC
由于这是自动化脚本 使用时请不要动屏幕 否则会造成其他问题。等待运行完成后直接查看生成的docx文件即可。

关爱鼠标猴 从我做起


2023/8/27
完成基础骨架

2023/8/28
增加docx文件导出