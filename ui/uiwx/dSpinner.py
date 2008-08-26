# -*- coding: utf-8 -*-
import locale
from decimal import Decimal as decimal
import wx
import dabo

if __name__ == "__main__":
	dabo.ui.loadUI("wx")
	
	
import dDataControlMixin as dcm
import dabo.dEvents as dEvents
from dabo.dLocalize import _
from dabo.ui import makeDynamicProperty
from dabo.ui import makeProxyProperty


class _dSpinButton(dcm.dDataControlMixin, wx.SpinButton):
	"""Simple wrapper around the base wx.SpinButton."""
	def __init__(self, parent, properties=None, attProperties=None, *args, **kwargs):
		self._baseClass = _dSpinButton
		preClass = wx.PreSpinButton
		kwargs["style"] = kwargs.get("style", 0) | wx.SP_ARROW_KEYS
		dcm.dDataControlMixin.__init__(self, preClass, parent, properties, attProperties, 
				*args, **kwargs)


	def __onWxSpinUp(self, evt):
		self.raiseEvent(dEvents.SpinUp, spinType="button")
		self.raiseEvent(dEvents.Spinner, spinType="button")


	def __onWxSpinDown(self, evt):
		self.raiseEvent(dEvents.SpinDown, spinType="button")
		self.raiseEvent(dEvents.Spinner, spinType="button")



class dSpinner(dabo.ui.dDataPanel):
	"""Control for allowing a user to increment a value by discreet steps across a range
	of valid values.
	"""
	def __init__(self, parent, properties=None, attProperties=None, *args, **kwargs):
		self.__constructed = False
		self._spinWrap = False
		self._min = 0
		self._max = 100
		self._increment = 1
		val = self._extractKey((properties, attProperties, kwargs), "Value", 0)
		val = self._numericStringVal(val)
		nm = self._extractKey((properties, attProperties, kwargs), "NameBase", "")
		if not nm:
			nm = self._extractKey((properties, attProperties, kwargs), "Name", "dSpinner")
		super(dSpinner, self).__init__(parent=parent, properties=properties, 
				attProperties=attProperties, *args, **kwargs)
		self._baseClass = dSpinner
		# Create the child controls
		self._proxy_textbox = dabo.ui.dTextBox(self, Value=val, Width=32, 
				StrictNumericEntry=False, _EventTarget=self)
		self._proxy_spinner = _dSpinButton(parent=self, _EventTarget=self)
		self.__constructed = True
		self.Sizer = dabo.ui.dSizer("h")
		self.Sizer.append(self._proxy_textbox, 1, valign="middle")
		self.Sizer.appendSpacer(2)
		self.Sizer.append(self._proxy_spinner, valign="middle")
		self.fitToSizer()
		# Because several properties could not be set until after the child
		# objects were created, we need to manually call _setProperties() here.
		self._properties["NameBase"] = nm
		self._setProperties(self._properties)
		self.autoBindEvents()
		ps = self._proxy_spinner
		pt = self._proxy_textbox
		# Set an essentially infinite range. We'll handle the range ourselves.
		ps.SetRange(-2**30, 2**30)
		# We'll also control wrapping ourselves
		self._proxy_spinner._addWindowStyleFlag(wx.SP_WRAP)
		ps.Bind(wx.EVT_SPIN_UP, self.__onWxSpinUp)
		ps.Bind(wx.EVT_SPIN_DOWN, self.__onWxSpinDown)
		ps.Bind(wx.EVT_SPIN, self._onWxHit)
		pt.Bind(wx.EVT_TEXT, self._onWxHit)
		self.bindEvent(dEvents.KeyChar, self._onChar)
		self.bindEvent(dEvents.LostFocus, self._onLostFocus)


	def _constructed(self):
		"""Returns True if the ui object has been fully created yet, False otherwise."""
		return self.__constructed
	

	def _coerceTypes(self, newVal, minn, maxx, margin):
		"""Handle the problems when min/max/increment values are
		of one type, and the edited value another.
		"""
		typN = type(newVal)
		# Only problem here is Decimal and float combinations
		if typN == decimal:
			def toDec(val):
				return decimal(str(val))
			margin = toDec(margin)
			if type(maxx) == float:
				maxx = toDec(maxx)
			if type(minn) == float:
				minn = toDec(minn)
		elif typN == float:
			if type(maxx) == decimal:
				maxx = float(maxx)
			if type(minn) == decimal:
				minn = float(minn)
		return minn, maxx, margin


	def _spinUp(self, evt=None):
		"""Handles a user request to increment the value."""
		ret = True
		curr = self._proxy_textbox.Value
		newVal = curr + self.Increment
		minn, maxx, margin = self._coerceTypes(newVal, self.Min, self.Max, 0.0001)
		diff = newVal - maxx
		if diff < margin:
			self._proxy_textbox.Value = newVal
		elif self._spinWrap:
			self._proxy_textbox.Value = minn + diff
		else:
			ret = False
		self._checkBounds()
		self.flushValue()
		self.raiseEvent(dEvents.Hit, hitType="button")
		return ret


	def _spinDown(self, evt=None):
		"""Handles a user request to decrement the value."""
		ret = True
		curr = self._proxy_textbox.Value
		newVal = curr - self.Increment
		minn, maxx, margin = self._coerceTypes(newVal, self.Min, self.Max, -0.0001)
		diff = newVal - minn
		if diff > margin:
			self._proxy_textbox.Value = newVal
		elif self._spinWrap:
			self._proxy_textbox.Value = maxx + diff
		else:
			ret = False
		self._checkBounds()
		self.flushValue()
		self.raiseEvent(dEvents.Hit, hitType="button")
		return ret


	def __onWxSpinUp(self, evt):
		"""Respond to the wx event by raising the Dabo event."""
		if self._spinUp():
			self.raiseEvent(dEvents.SpinUp, spinType="button")
			self.raiseEvent(dEvents.Spinner, spinType="button")


	def __onWxSpinDown(self, evt):
		"""Respond to the wx event by raising the Dabo event."""
		if self._spinDown():
			self.raiseEvent(dEvents.SpinDown, spinType="button")
			self.raiseEvent(dEvents.Spinner, spinType="button")
	
	
	def _checkBounds(self):
		"""Make sure that the value is within the current Min/Max"""
		if self._proxy_textbox.Value < self.Min:
			self._proxy_textbox.Value = self._proxy_spinner.Value = self.Min
		elif self._proxy_textbox.Value > self.Max:
			self._proxy_textbox.Value = self._proxy_spinner.Value = self.Max


	def _onWxHit(self, evt):
		# Determine what type of event caused Hit to be raised.
		if evt is None:
			typ = "key"
		elif evt.GetEventObject() is self._proxy_textbox:
			typ = "text"
		else:
			typ = "spin"
		# Flush the data on each hit, not just when focus is lost.
		self.flushValue()
		super(dSpinner, self)._onWxHit(evt, hitType=typ)


	def _onChar(self, evt):
		"""Handle the case where the user presses the up/down arrows to 
		activate the spinner.
		"""
		keys = dabo.ui.dKeys
		kc = evt.keyCode
		if kc in (keys.key_Up, keys.key_Numpad_up):
			if self._spinUp():
				self.raiseEvent(dEvents.SpinUp, spinType="key")
				self.raiseEvent(dEvents.Spinner, spinType="key")
			self._onWxHit(None)
		elif kc in (keys.key_Down, keys.key_Numpad_down):
			if self._spinDown():
				self.raiseEvent(dEvents.SpinDown, spinType="key")
				self.raiseEvent(dEvents.Spinner, spinType="key")
			self._onWxHit(None)


	def _onLostFocus(self, evt):
		"""We need to handle the case where the user types an invalid value
		into the textbox and then tabs/clicks away.
		"""
		val = self.Value
		pt = self._proxy_textbox
		if (val > self.Max) or (val < self.Min):
			self.Value = pt._oldVal
		pt._oldVal = self.Value


	def _numericStringVal(self, val):
		"""If passed a string, attempts to convert it to the appropriate numeric
		type. If such a conversion is not possible, returns None.
		"""
		ret = val
		if isinstance(val, basestring):
			if val.count(locale.localeconv()["decimal_point"]) > 0:
				func = decimal
			else:
				func = int
			try:
				ret = func(val)
			except ValueError:
				ret = None
		return ret


	def fontZoomIn(self, amt=1):
		"""Zoom in on the font, by setting a higher point size."""
		self._proxy_textbox._setRelativeFontZoom(amt)


	def fontZoomOut(self, amt=1):
		"""Zoom out on the font, by setting a lower point size."""
		self._proxy_textbox._setRelativeFontZoom(-amt)


	def fontZoomNormal(self):
		"""Reset the font zoom back to zero."""
		self._proxy_textbox._setAbsoluteFontZoom(0)


	def getBlankValue(self):
		return 0


	# Property get/set definitions begin here
	def _getChildren(self):
		# The native wx control will return the items that make up this composite
		# control, which our user doesn't want.
		return []
	
	
	def _getIncrement(self):
		return self._increment

	def _setIncrement(self, val):
		if self._constructed():
			self._increment = val
		else:
			self._properties["Increment"] = val


	def _getMax(self):
		return self._max

	def _setMax(self, val):
		if self._constructed():
			self._max = val
			self._checkBounds()
		else:
			self._properties["Max"] = val


	def _getMin(self):
		return self._min

	def _setMin(self, val):
		if self._constructed():
			self._min = val
			self._checkBounds()
		else:
			self._properties["Min"] = val


	def _getSpinnerWrap(self):
		return self._spinWrap

	def _setSpinnerWrap(self, val):
		if self._constructed():
			self._spinWrap = val
		else:
			self._properties["SpinnerWrap"] = val


	def _getValue(self):
		try:
			return self._proxy_textbox.Value
		except AttributeError:
			return None

	def _setValue(self, val):
		if self._constructed():
			if isinstance(val, (int, long, float, decimal)):
				self._proxy_textbox.Value = val
			else:
				numVal = self._numericStringVal(val)
				if numVal is None:
					dabo.errorLog.write(_("Spinner values must be numeric. Invalid:'%s'") % val)
				else:
					self._proxy_textbox.Value = val
		else:
			self._properties["Value"] = val



	Children = property(_getChildren, None, None, 
			_("""Returns a list of object references to the children of 
			this object. Only applies to containers. Children will be None for 
			non-containers.  (list or None)"""))
	
	Increment = property(_getIncrement, _setIncrement, None,
			_("Amount the control's value changes when the spinner buttons are clicked  (int/float)"))

	Max = property(_getMax, _setMax, None,
			_("Maximum value for the control  (int/float)"))
	
	Min = property(_getMin, _setMin, None,
			_("Minimum value for the control  (int/float)"))

	SpinnerWrap = property(_getSpinnerWrap, _setSpinnerWrap, None,
			_("Specifies whether the spinner value wraps at the high/low value. (bool)"))

	Value = property(_getValue, _setValue, None,
			_("Value of the control  (int/float)"))
	

	DynamicIncrement = makeDynamicProperty(Increment)
	DynamicMax = makeDynamicProperty(Max)
	DynamicMin = makeDynamicProperty(Min)
	DynamicSpinnerWrap = makeDynamicProperty(SpinnerWrap)


	# Pass-through props. These are simply ways of exposing the text control's props
	# through this control
	_proxyDict = {}
	Alignment = makeProxyProperty(_proxyDict, "Alignment", "_proxy_textbox", )
	BackColor = makeProxyProperty(_proxyDict, "BackColor", ("_proxy_textbox", "self"))
	Enabled = makeProxyProperty(_proxyDict, "Enabled", ("self", "_proxy_spinner", "_proxy_textbox"))
	Font = makeProxyProperty(_proxyDict, "Font", "_proxy_textbox")
	FontInfo = makeProxyProperty(_proxyDict, "FontInfo", "_proxy_textbox")
	FontSize = makeProxyProperty(_proxyDict, "FontSize", "_proxy_textbox")
	FontFace = makeProxyProperty(_proxyDict, "FontFace", "_proxy_textbox")
	FontBold = makeProxyProperty(_proxyDict, "FontBold", "_proxy_textbox")
	FontItalic = makeProxyProperty(_proxyDict, "FontItalic", "_proxy_textbox")
	FontUnderline = makeProxyProperty(_proxyDict, "FontUnderline", "_proxy_textbox")
	ForeColor = makeProxyProperty(_proxyDict, "ForeColor", "_proxy_textbox")
	Height = makeProxyProperty(_proxyDict, "Height", ("self", "_proxy_spinner", "_proxy_textbox"))
	ReadOnly = makeProxyProperty(_proxyDict, "ReadOnly", "_proxy_textbox")
	SelectOnEntry = makeProxyProperty(_proxyDict, "SelectOnEntry", "_proxy_textbox")
	ToolTipText = makeProxyProperty(_proxyDict, "ToolTipText", ("self", "_proxy_spinner", "_proxy_textbox"))
	Visible = makeProxyProperty(_proxyDict, "Visible", ("self", "_proxy_spinner", "_proxy_textbox"))
	


class _dSpinner_test(dSpinner):
	def initProperties(self):
		self.Max = 55
		self.Min = 0
		self.Value = 0
		self.Increment = 8.75
		self.SpinnerWrap = True
		self.FontSize = 10
		self.Width = 80
		
	def onHit(self, evt):
		print "HIT!", self.Value, "Hit Type", evt.hitType
	
	def onSpinUp(self, evt):
		print "Spin up event."
	
	def onSpinDown(self, evt):
		print "Spin down event."
	
	def onSpinner(self, evt):
		print "Spinner event."



if __name__ == '__main__':
	class TestForm(dabo.ui.dForm):
		def afterInit(self):
			pnl = dabo.ui.dPanel(self)
			self.Sizer.append1x(pnl)
			sz = pnl.Sizer = dabo.ui.dSizer("v")
			
			spn = self.spinner = _dSpinner_test(pnl)
			sz.append(spn, border=10, halign="center")
			
			lbl = dabo.ui.dLabel(pnl, Caption=_("Spinner Properties"), FontSize=18,
					FontBold=True)
			sz.appendSpacer(10)
			sz.append(lbl, halign="center")
			sz.appendSpacer(4)
			
			gsz = dabo.ui.dGridSizer(MaxCols=2, HGap=4, VGap=6)
			lbl = dabo.ui.dLabel(pnl, Caption="Min")
			txt = dabo.ui.dTextBox(pnl, DataSource=spn, DataField="Min", StrictNumericEntry=False)
			gsz.append(lbl, halign="right")
			gsz.append(txt)
			lbl = dabo.ui.dLabel(pnl, Caption="Max")
			txt = dabo.ui.dTextBox(pnl, DataSource=spn, DataField="Max", StrictNumericEntry=False)
			gsz.append(lbl, halign="right")
			gsz.append(txt)
			lbl = dabo.ui.dLabel(pnl, Caption="Increment")
			txt = dabo.ui.dTextBox(pnl, DataSource=spn, DataField="Increment", StrictNumericEntry=False)
			gsz.append(lbl, halign="right")
			gsz.append(txt)
			lbl = dabo.ui.dLabel(pnl, Caption="SpinnerWrap")
			chk = dabo.ui.dCheckBox(pnl, DataSource=spn, DataField="SpinnerWrap")
			gsz.append(lbl, halign="right")
			gsz.append(chk)
			lbl = dabo.ui.dLabel(pnl, Caption="FontSize")
			txt = dabo.ui.dTextBox(pnl, DataSource=spn, DataField="FontSize")
			gsz.append(lbl, halign="right")
			gsz.append(txt)
			lbl = dabo.ui.dLabel(pnl, Caption="Height")
			txt = dabo.ui.dTextBox(pnl, DataSource=spn, DataField="Height")
			gsz.append(lbl, halign="right")
			gsz.append(txt)
			lbl = dabo.ui.dLabel(pnl, Caption="ForeColor")
			txt = dabo.ui.dTextBox(pnl, ReadOnly=True, DataSource=spn, DataField="ForeColor")
			btn = dabo.ui.dButton(pnl, Caption="...", OnHit=self.onColor, Width=36)
			hsz = dabo.ui.dSizer("h")
			hsz.append(txt, 1)
			hsz.append(btn)
			gsz.append(lbl, halign="right")
			gsz.append(hsz)
			lbl = dabo.ui.dLabel(pnl, Caption="Enabled")
			chk = dabo.ui.dCheckBox(pnl, DataSource=spn, DataField="Enabled")
			gsz.append(lbl, halign="right")
			gsz.append(chk)
			
			sz.append(gsz, halign="center")
			self.update()
			self.layout()

		def onColor(self, evt):
			color = dabo.ui.getColor(self.spinner.ForeColor)
			if color is not None:
				self.spinner.ForeColor = color
				self.update()

	app = dabo.dApp(MainFormClass=TestForm)
	app.start()