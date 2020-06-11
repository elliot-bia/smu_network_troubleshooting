#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# #    File: logic.py
# #    Project: 学校网络故障排查
# #    Author: zzy
# #    mail: elliot.bia.8989@outlook.com
# #    github: https://github.com/elliot-bia
# #    Date: 2019-10-30 10:24:52
# #    LastEditors: zzy
# #    LastEditTime: 2019-11-13 11:02:35
# #    ---------------------------------
# #    Description: 逻辑代码文件
###

# from __future__ import print_function
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from test1_2 import *
from ico_none import *
# from test3_frame_big import *
import webbrowser 
import ifaddr
import ctypes



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        self.setupUi(self)
        # 设置tab大小
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 135px; width: 115px; }")
        self.pushButton_3.clicked.connect(self.pushButton_3_Clicked) # 访问校园网
        self.pushButton_6.clicked.connect(self.pushButton_6_Clicked) # 退出校园网
        self.pushButton_7.clicked.connect(self.pushButton_7_Clicked) # 访问百度
        self.pushButton_10.clicked.connect(self.pushButton_10_Clicked) # 重启
        self.pushButton_8.clicked.connect(self.pushButton_8_Clicked) # 自动获取IP地址
        self.pushButton_9.clicked.connect(self.pushButton_9_Clicked) # 重置状态


    def pushButton_3_Clicked(self, event):
        webbrowser.open('http://1.1.1.1', new=0, autoraise=True)
        
    def pushButton_6_Clicked(self, event):
        webbrowser.open('http://1.1.1.1:8000', new=0, autoraise=True)

    def pushButton_7_Clicked(self, event):
        webbrowser.open('www.baidu.com', new=0, autoraise=True)

    def pushButton_10_Clicked(self, event):
        reply = QMessageBox.question(self, 'Message',
            "确认重启?\n请务必保存文件", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            os.system("shutdown -r -t 3")
        else:
            pass      

    def pushButton_8_Clicked(self, event):
        for adapter in ifaddr.get_adapters():
            for ip in adapter.ips:
                # print(ip.nice_name)
                adapter_name = ip.nice_name
                os.system('netsh interface ip set address name="%s" source=dhcp' %(adapter_name))
                # print("ip")
                os.system('netsh interface ip set dns name="%s" source=dhcp' %(adapter_name))
        QMessageBox.about(self, 'Message',
            "设置成功, 请尝试登录校园网账号")   

    def pushButton_9_Clicked(self, event):
        os.system('netsh winsock reset')

        reply = QMessageBox.question(self, 'Message',
            "确认重启?\n请务必保存文件", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            os.system("shutdown -r -t 3")
        else:
            QMessageBox.about(self, 'Message',
            "重启后生效, 请自行重启")      
        



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == '__main__':

    # try:
    #     # 检测管理员权限
    #     if is_admin():
    #         app = QApplication(sys.argv)
    
    #         myWin = MyWindow()

    #         myWin.show()
    #         sys.exit(app.exec_())
    #     else:
    #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # except:
    #     pass


    app = QApplication(sys.argv)
    
    myWin = MyWindow()

    myWin.show()
    sys.exit(app.exec_())
   
