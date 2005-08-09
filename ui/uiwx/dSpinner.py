import wx, dabo, dabo.ui

if __name__ == "__main__":
	dabo.ui.loadUI("wx")

import dDataControlMixin as dcm
import dabo.dEvents as dEvents
from dabo.dLocalize import _

class dSpinner(wx.SpinCtrl, dcm.dDataControlMixin):
	""" Allows editing integer values.
	"""
	def __init__(self, parent, properties=None, *args, **kwargs):
		self._baseClass = dSpinner
		preClass = wx.PreSpinCtrl
		dcm.dDataControlMixin.__init__(self, preClass, parent, properties, *args, **kwargs)

	
	def _initEvents(self):
		super(dSpinner, self)._initEvents()
		self.Bind(wx.EVT_SPINCTRL, self._onWxHit)
		

	def _preInitUI(self, kwargs):
		# Force the use of arrow keys
		kwargs["style"] = kwargs["style"] | wx.SP_ARROW_KEYS
		return kwargs

	
	def _getInitPropertiesList(self):
		additional = ["SpinnerWrap",]
		original = list(super(dSpinner, self)._getInitPropertiesList())
		return tuple(original + additional)
		
		
	# Property get/set/del methods follow. Scroll to bottom to see the property
	# definitions themselves.
	def _getMax(self):
		return self.GetMax()

	def _setMax(self, value):
		if self._constructed():
			rangeLow = self.GetMin()
			rangeHigh = int(value)
			self.SetRange(rangeLow, rangeHigh)
		else:
			self._properties["Max"] = value


	def _getMin(self):
		return self.GetMin()

	def _setMin(self, value):
		if self._constructed():
			rangeLow = int(value)
			rangeHigh = self.Max
			self.SetRange(rangeLow, rangeHigh)
		else:
			self._properties["Min"] = value

	def _getSpinnerWrap(self):
		return self.hasWindowStyleFlag(wx.SP_WRAP)

	def _setSpinnerWrap(self, value):
		self.delWindowStyleFlag(wx.SP_WRAP)
		if value:
			self.addWindowStyleFlag(wx.SP_WRAP)


	# Property definitions:
	Min = property(_getMin, _setMin, None, 
		"Specifies the lowest possible value for the spinner. (int)")

	Max = property(_getMax, _setMax, None, 
		"Specifies the highest possible value for the spinner. (int)")

	SpinnerWrap = property(_getSpinnerWrap, _setSpinnerWrap, None,
		"Specifies whether the spinner value wraps at the high/low value. (bool)")

class _dSpinner_test(dSpinner):
	def initProperties(self):
		self.Max = 12
		self.Min = 5
		self.SpinnerWrap = True

if __name__ == "__main__":
	import test
	test.Test().runTest(_dSpinner_test)
