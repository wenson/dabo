""" dBaseMenuBar.py

This module contains the class definitions and logic to build
a basic menu for all platforms. There are special needs for
complying with Apple's Human Interface Guidelines, for instance.

Typical usage would be to subclass this class, and then use the 
append() methods of the menubar and menus to add the specific 
menu items that your app needs.
"""
import os
import wx
import dabo
from dMenu import dMenu
from dMenuBar import dMenuBar
import dIcons
from dabo.dLocalize import _, n_


class FileMenu(dMenu):
	
	def __init__(self, *args, **kwargs):
		kwargs["MRU"] = True
		self.super(*args, **kwargs)
		
		
	def _afterInit(self):
		super(FileMenu, self)._afterInit()
		app = self.Application
		self.Caption = _("&File")

		if self.Application.ShowCommandWindowMenu:
			self.append(_("Command Win&dow") + "\tCtrl+D", OnHit=app.onCmdWin, 
					help=_("Open up a command window for debugging") )
		
		prmpt = _("Close Windo&w") + "\tCtrl+W"
		self.append(prmpt, OnHit=app.onWinClose, bmp="close",
				help=_("Close the current window") )

		self.appendSeparator()

		prmpt = _("&Quit") + "\tCtrl+Q"
# 		if wx.Platform == '__WXWIN__':
# 			prmpt = _("E&xit") + "\tAlt+F4"
		self.append(prmpt, id=wx.ID_EXIT, OnHit=app.onFileExit, 
				bmp="exit", help=_("Exit the application") )



class EditMenu(dMenu):
	def _afterInit(self):
		super(EditMenu, self)._afterInit()
		app = self.Application
		self.Caption = _("&Edit")

		self.append(_("&Undo") + "\tCtrl+Z", OnHit=app.onEditUndo, bmp="undo",
				help=_("Undo last action") )

		self.append(_("&Redo") + "\tCtrl+R", OnHit=app.onEditRedo, bmp="redo",
				help=_("Undo last undo") )

		self.appendSeparator()

		self.append(_("Cu&t") + "\tCtrl+X", OnHit=app.onEditCut, bmp="cut",
				help=_("Cut selected text") )

		self.append(_("&Copy") + "\tCtrl+C", OnHit=app.onEditCopy, bmp="copy",
				help=_("Copy selected text") )

		self.append(_("&Paste") + "\tCtrl+V", OnHit=app.onEditPaste, bmp="paste",
				help=_("Paste text from clipboard") )

		self.append(_("Select &All") + "\tCtrl+A", OnHit=app.onEditSelectAll,
				help=_("Select all text") )

		self.appendSeparator()

		# By default, the Find and Replace functions use a single dialog. The
		# commented lines below this enable the plain Find dialog call.
		self.append(_("&Find / Replace") + "\tCtrl+F", OnHit=app.onEditFind, 
				bmp="find", help=_("Find text in the active window") )

# 		self.append(_("Find") + "\tShift+Ctrl+F", OnHit=app.onEditFindAlone, 
# 				bmp="find", help=_("Find text in the active window") )

		self.append(_("Find A&gain") + "\tCtrl+G", OnHit=app.onEditFindAgain, bmp="",
				help=_("Repeat the last search") )

		self.appendSeparator()

		itm = self.append(_("&Preferences"), OnHit=app.onEditPreferences, bmp="configure",
				help=_("Set user preferences") )
		# Put the prefs item in the App Menu on Mac
		wx.App_SetMacPreferencesMenuItemId(itm.GetId())



class ViewMenu(dMenu):
	def _afterInit(self):
		super(ViewMenu, self)._afterInit()
		app = self.Application
		self.Caption = _("&View")
	
		self.append(_("Increase Font Size") + "\tCtrl++", OnHit=app.fontZoomIn)
		self.append(_("Decrease Font Size") + "\tCtrl+-", OnHit=app.fontZoomOut)
		self.append(_("Normal Font Size") + "\tCtrl+/", OnHit=app.fontZoomNormal)
	
		if app.ShowSizerLinesMenu:
			self.appendSeparator()
			self.append(_("Show/Hide Sizer &Lines")+"\tCtrl+L",	
					OnHit=app.onShowSizerLines, menutype="check",
					help=_("Cool sizer visualizing feature; check it out!"))


class HelpMenu(dMenu):
	def _afterInit(self):
		super(HelpMenu, self)._afterInit()
		app = self.Application
		self.Caption = _("&Help")

		itm = self.append(_("&About"), id=wx.ID_ABOUT, 
				OnHit=app.onHelpAbout, bmp="apply",
				help=_("About this application") )
		# Put the about menu in the App Menu on Mac
		wx.App_SetMacAboutMenuItemId(itm.GetId())
		wx.App_SetMacHelpMenuTitleName(self.Caption)


class dBaseMenuBar(dMenuBar):
	"""Creates a basic menu bar with File, Edit, and Help menus.

	The Edit menu has standard Copy, Cut, and Paste menu items, and the Help menu
	has an About menu item. On Mac, the About menu item and Help menu are moved
	to the appropriate place in the application menu.

	Typical usage would be to instantiate dBaseMenuBar, set it to your form's 
	menubar (using form.MenuBar = dabo.ui.dBaseMenuBar) and then use the 
	append() methods of dMenuBar and dMenu to add the specific dMenu(s) and
	dMenuItem(s) that your application needs.
	"""
	def _afterInit(self):
		super(dBaseMenuBar, self)._afterInit()
		self.appendMenu(FileMenu(self))
		self.appendMenu(EditMenu(self))
		self.appendMenu(ViewMenu(self))
		self.appendMenu(HelpMenu(self))

if __name__ == "__main__":
	app = dabo.dApp()
	app.setup()
	app.MainForm.MenuBar = None
#	app.MainForm.MenuBar = dBaseMenuBar()
	app.start()
