# -*- coding: utf-8 -*-
import os
import wx
import dabo

if __name__ == "__main__":
	dabo.ui.loadUI("wx")

import dControlMixin as cm
from dabo.dLocalize import _
import dabo.dEvents as dEvents
from dabo.ui import makeDynamicProperty

# Need to define this exception class for x-platform
try:
	WindowsError
except:
	class WindowsError: pass

try:
	import wx.lib.pdfwin as pdfwin
	PDFWindow = pdfwin.PDFWindow
except (ImportError, AttributeError, WindowsError):
	class Dummy(object):
		_dummy = True
	PDFWindow = Dummy


class dPdfWindow(cm.dControlMixin, PDFWindow):
	"""Displays a PDF file on Windows using Adobe Acrobat Reader in a panel.

	See wx.lib.pdfwin.PDFWindow for the API.
	"""
	def __init__(self, parent, properties=None, attProperties=None, *args, **kwargs):
		if hasattr(PDFWindow, "_dummy"):
			raise ImportError, "wx.lib.pdfwin couldn't be imported, so dPdfWindow cannot instantiate."

		self._baseClass = dPdfWindow
		preClass = pdfwin.PDFWindow
		cm.dControlMixin.__init__(self, preClass, parent, properties, attProperties, 
				*args, **kwargs)
	


class _dPdfWindow_test(dPdfWindow):
	def afterInit(self):
		# Run the dReportWriter test, which will output a test 
		# pdf in this directory, and load that into the dPdfWindow:
		os.system("python ../../dReportWriter.py")
		self.LoadFile(os.path.abspath("dRW-test.pdf"))


if __name__ == "__main__":
	import test
	test.Test().runTest(_dPdfWindow_test)

