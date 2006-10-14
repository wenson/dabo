import time
import wx
import dabo
import dabo.dEvents as dEvents
import dFormMixin as fm
import dPanel, dIcons, dSizer


class dFormMainBase(fm.dFormMixin):
	""" This is the main top-level form for the application.
	"""
	def __init__(self, preClass, parent=None, properties=None, *args, **kwargs):
		fm.dFormMixin.__init__(self, preClass, parent, properties, *args, **kwargs)
	
		self.Size = (640, 480)
		self.Position = (-1, -1)

		if wx.Platform != '__WXMAC__':
			self.CreateStatusBar()

		
	def _afterInit(self):
		super(dFormMainBase, self)._afterInit()
		
		# This is to accomodate the Dabo icon, which has a white background.
		# We should set the white as transparent and set a mask, though.
		self.BackColor = "White"
		
		# Set up the Dabo icon
		self.bitmap = self.drawBitmap("dabo_lettering_250x100", x=10, y=0)
		plat = self.Application.Platform.lower()
		off = 150
		if plat == "win":
			off = 180
		elif plat == "gtk":
			off = 160
		self.bitmap.DynamicYpos = lambda: self.Height - off
		self.autoClearDrawings = True
		self.bindEvent(dEvents.Resize, self.__onResize)
	
	
	def __onResize(self, evt):
		self.update()		

	
	def _beforeClose(self, evt=None):
		forms2close = [frm for frm in self.Application.uiForms
				if frm is not self]
		while forms2close:
			frm = forms2close[0]
			# This will allow forms to veto closing (i.e., user doesn't
			# want to save pending changes). 
			if frm.close() == False:
				# The form stopped the closing process. The user
				# must deal with this form (save changes, etc.) 
				# before the app can exit.
				frm.bringToFront()
				return False
			else:
				forms2close.remove(frm)

	


class dFormMain(wx.Frame, dFormMainBase):
	def __init__(self, parent=None, properties=None, *args, **kwargs):
		self._baseClass = dFormMain

		if dabo.settings.MDI:
			# Hack this into an MDI Parent:
			dFormMain.__bases__ = (wx.MDIParentFrame, dFormMainBase)
			preClass = wx.PreMDIParentFrame
			self._mdi = True
		else:
			# This is a normal SDI form:
			dFormMain.__bases__ = (wx.Frame, dFormMainBase)
			preClass = wx.PreFrame
			self._mdi = False
		## (Note that it is necessary to run the above block each time, because
		##  we are modifying the dFormMain class definition globally.)

		dFormMainBase.__init__(self, preClass, parent, properties, *args, **kwargs)





if __name__ == "__main__":
	import test
	test.Test().runTest(dFormMain)
