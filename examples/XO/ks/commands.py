# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Place(object):

	@staticmethod
	def name():
		return 'Place'


	def __init__(self, x=None, y=None):
		self.initialize(x, y)
	

	def initialize(self, x=None, y=None):
		self.x = x
		self.y = y
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('I', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('I', self.y)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.x = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.y = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		return offset
