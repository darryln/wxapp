#!/usr/bin/python3

#import sys
import os
#import time
#import traceback
#import re
#import shutil
#from threading import Thread

#from distutils.version import LooseVersion

import wx
#import wx.adv
#import wx.lib.agw.aui as aui
import wx.html
#from wx.lib.msgpanel import MessagePanel
#from wx.adv import TaskBarIcon as TaskBarIcon
#from wx.adv import SplashScreen as SplashScreen
#import wx.lib.mixins.inspection

from sys import version

# persistent settings
import wx.lib.agw.persist as PM

from dialmeter import DialMeter
from aboutbox import AboutBox

APPNAME = "wxApp"

class frameMainAppWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(frameMainAppWindow, self).__init__(*args, **kw)

        self.spd = DialMeter(self)

        # set app name and default window size
        self.SetName(APPNAME);
        self.SetTitle(APPNAME);
        disp = wx.GetDisplaySize()
        self.appWindowSize = (40*disp[0]/100,50*disp[1]/100)
        self.SetSize(self.appWindowSize[0], self.appWindowSize[1])
        self.Centre()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self._persistMgr = PM.PersistenceManager.Get()
        _configFile = os.path.join(os.getcwd(), self.GetName())
        self._persistMgr.SetPersistenceFile(_configFile)

        if not self._persistMgr.RegisterAndRestore(self):
            print("App settings NOT restored!")
        else:
            print("App settings restored")

        self.SetFocus()
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&File")
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")
        self.SetMenuBar(menuBar)
        
        self.statusbar = self.CreateStatusBar()

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        
        #m_text = wx.StaticText(panel, -1, "Hello World!")
        #m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        #m_text.SetSize(m_text.GetBestSize())
        #box.Add(m_text, 0, wx.ALL, 10)
        
        panel.SetSizer(box)
        panel.Layout()

    def OnClose(self, event):
        print("OnClose: saving persistent settings")
        self._persistMgr.SaveAndUnregister(self)
        event.Skip()

    def OnAbout(self, event):
        print("OnAbout:")
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        print("OnExit:")
        self.Close(True)

class wxApp(wx.App):
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        super(wxApp, self).__init__(redirect, filename, useBestVisual, clearSigInt)

    def OnPreInit(self):
        super(wxApp, self).OnPreInit()

    def OnInit(self):
        wmain = frameMainAppWindow(None, -1)

        # Initialization code goes here.

        # show main window
        wmain.Show()
        return True


    #def RedirectStdio(self, filename=None)
    #    Redirect sys.stdout and sys.stderr to a file or a popup window.
    #def RestoreStdio(self)
    #def SetOutputWindowAttributes(self, title=None, pos=None, size=None)
    #    Set the title, position and/or size of the output window if the 
    #    stdio has been redirected. This should be called before any 
    #    output would cause the output window to be created.



if __name__ == '__main__':
    app = wxApp()
    app.MainLoop()
