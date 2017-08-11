# -*- coding: utf-8 -*-
import cv2
from managers import Capturemanager,WindowManager

class Cameo(object):
	"""docstring for Cameo"""
	def __init__(self):
		super(Cameo, self).__init__()
		self._windowManeger = WindowManager('Cameo',self.onkeypress)
		self._capturemanager = Capturemanager(cv2.VideoCapture(0),self._windowManeger,True)

	def run(self):
		self._windowManeger.createWindow()
		while self._windowManeger.isWindowCreated:
			self._capturemanager.enterFrame()
			frame = self._capturemanager.frame

			self._capturemanager.exitFrame()
			self._windowManeger.processEvents()

	def onkeypress(self,keycode):
		''''''
		if keycode == 32:	#space
			self._capturemanager.writeImage('source/screenshot.png')
		elif keycode == 9:	#tab
			if not self._capturemanager.isWritingVideo:
				self._capturemanager.startWritingVideo('source/screencast.avi')
			else:
				self._capturemanager.stopWritingVideo()
		elif keycode == 27:	#escape
			self._windowManeger.destroyWindow()

if __name__ == '__main__':
	Cameo().run()

