# -*- coding: utf-8 -*-
import Tkinter
import logging

origLabel = Tkinter.Label


class Label(origLabel):
	def __init__(self, *args, **kw):
		origLabel.__init__(self, *args, **kw)
		self.logger = logging.getLogger("gui log")

	def _update_text(self, value):
		self.logger.info("Updated Text for label '%s' (set to %s)" % (self.winfo_name(), value))

	def configure(self, *args, **kw):
		origLabel.configure(self, *args, **kw)
		if "text" in kw:
			self._update_text(kw["text"])

	def __setitem__(self, key, value):
		origLabel.__setitem__(self, key, value)
		if key == "text":
			self._update_text(value)

	config = configure
	internal_configure = origLabel.configure

Tkinter.Label = Label
