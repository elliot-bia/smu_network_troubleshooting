#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# #    File: 
# #    Project: 
# #    Author: zzy
# #    mail: elliot.bia.8989@outlook.com
# #    github: https://github.com/elliot-bia
# #    Date: 2019-11-12 09:56:32
# #    LastEditors: zzy
# #    LastEditTime: 2019-11-13 10:18:18
# #    ---------------------------------
# #    Description: 
###

class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.West)


MainWindow.resize(490, 618)

self.tabWidget.setMinimumSize(QtCore.QSize(460, 461))


    # self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget = TabWidget(self.frame)


font = QtGui.QFont()
font.setFamily("幼圆")
font.setPointSize(20)
self.label_6.setFont(font)
self.label_6.setAlignment(QtCore.Qt.AlignCenter)
self.label_6.setObjectName("label_6")

font.setFamily("幼圆")
font.setPointSize(20)
self.label_5.setFont(font)
self.label_5.setAlignment(QtCore.Qt.AlignCenter)
self.label_5.setObjectName("label_5")

font = QtGui.QFont()
font.setFamily("幼圆")
font.setPointSize(20)
self.label_7.setFont(font)
self.label_7.setAlignment(QtCore.Qt.AlignCenter)
self.label_7.setObjectName("label_7")
