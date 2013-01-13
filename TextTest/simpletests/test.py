# -*- coding: utf-8 -*-
import sys
import time
import math
import Tkinter
import storytext


def mul(a, b):
	print 'params: %s, %s' % (a, b)
	result = a * b
	print 'result = %s' % result
	if result > 0:
		print 'positive'
	elif result == 0:
		print 'zero'
	else:
		print 'negative'


def file_write(s):
	f = open('log.txt', 'wt')
	f.write('%s %s-%s\n' % (time.strftime("%H:%M:%S"), s, s[::-1]))


def formula(val):
	print math.floor(math.fabs(val))


class TestGUI:
	def __init__(self, root):
		self.root = root

		frame1 = Tkinter.Frame(self.root)
		frame1.pack(fill="both")
		frame2 = Tkinter.Frame(self.root)
		frame2.pack(fill="both")
		frame3 = Tkinter.Frame(self.root)
		frame3.pack(fill="both")
		frame4 = Tkinter.Frame(self.root)
		frame4.pack(fill="both")

		Tkinter.Label(frame1, text="Input:").pack(side="left")
		self.var_in = Tkinter.StringVar(value="")
		Tkinter.Entry(frame1, name="entry_in", textvariable=self.var_in).pack()

		Tkinter.Label(frame2, text="Output:").pack(side="left")
		self.label_out = Tkinter.Label(frame2, name="label_out")
		self.label_out.pack(side="left")

		Tkinter.Button(frame3, name="entry_calc_sync", text="OnCalcSync", width=15, command=self.on_press_sync).pack(side="left")
		Tkinter.Button(frame4, name="entry_calc_async", text="OnCalcAsync", width=15, command=self.on_press_async).pack(side="left")
		Tkinter.Button(frame4, name="entry_exit", text="OnExit", width=15, command=self.on_exit).pack(side="left")

		self.root.title("Hello World!")
		self.root.mainloop()

	def _calc(self):
		try:
			return str(int(self.var_in.get()) * 2)
		except:
			return "error input"

	def on_press_sync(self):
		self.label_out["text"] = self._calc()

	def _operation_finish(self):
		storytext.applicationEvent('data to be loaded')
		self.label_out["text"] = self._calc()

	def on_press_async(self):
		self.root.after(10 * 1000, self._operation_finish)

	def on_exit(self):
		self.root.destroy()


if __name__ == '__main__':

	if len(sys.argv) == 4 and sys.argv[1] == 'mul':
		mul(int(sys.argv[2]), int(sys.argv[3]))
	elif len(sys.argv) == 3 and sys.argv[1] == 'file':
		file_write(sys.argv[2])
	elif len(sys.argv) == 3 and sys.argv[1] == 'math':
		formula(float(sys.argv[2]))
	elif len(sys.argv) == 2 and sys.argv[1] == 'gui':
		import tkinter_ex
		TestGUI(Tkinter.Tk())
	else:
		print "error params"
