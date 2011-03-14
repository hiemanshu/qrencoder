#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Hiemanshu Sharma <mail@theindiangeek.in>
# Date: Mon Mar 14 2011, 17:30:20
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation; either version 2, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
#
# You should have received a copy of the GNU Library General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

# Import essential modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyKDE4.kdecore import KUrl
from subprocess import call


class qrencoder(plasmascript.Applet):

    #   Constructor, forward initialization to its superclass
    #   Note: try to NOT modify this constructor; all the setup code
    #   should be placed in the init method.
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    #   init method
    #   Put here all the code needed to initialize our plasmoid
    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.Square)
        self.resize(300,400)     
        
        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        
        self.label = Plasma.Label(self.applet)
        self.label.setText("Enter the text to be converted")
        self.label.nativeWidget().setAlignment(Qt.AlignHCenter)
        self.layout.addItem(self.label)
        
        self.text = Plasma.LineEdit(self.applet)
        self.text.setClearButtonShown(True)
        self.text.nativeWidget().setMaxLength(1000)
        self.layout.addItem(self.text)
        
        self.button = Plasma.PushButton(self.applet)
        self.button.setText("Generate")
        self.button.clicked.connect(self.generate)
        self.layout.addItem(self.button)
        
        self.webView = Plasma.WebView(self.applet)
        self.webView.setUrl(KUrl("about:blank"))
	self.webView.setMinimumSize(250, 250)
        self.layout.addItem(self.webView)
        self.setLayout(self.layout)

    def generate(self):
	call(['qrencode', '-s', str(10), '-m', str(3), '-o', '/home/hiemanshu/qrencoder.png', self.text.text()])
	self.webView.setUrl(KUrl("file:///home/hiemanshu/qrencoder.png"))
	
    #   Simple painting function
    def paintInterface(self, painter, option, rect):
       painter.save()
    #    # Simple paint code example
    #    textColor = Plasma.Theme.defaultTheme().color(Plasma.Theme.TextColor)
    #    painter.setPen(textColor)
    #    painter.drawText(rect, Qt.AlignHCenter, "Enter text to convert to QRcode")   
       painter.restore()

    #   CreateApplet method
    #   Note: do NOT modify it, needed by Plasma
def CreateApplet(parent):
    return qrencoder(parent)
