# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class EDir(Enum):
	Top = 0
	Right = 1
	Bottom = 2
	Left = 3


class Move(object):

	@staticmethod
	def name():
		return 'Move'


	def __init__(self, direction=None):
		self.initialize(direction)
	

	def initialize(self, direction=None):
		self.direction = direction
	

	def serialize(self):
		s = b''
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('B', self.direction.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.direction
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			self.direction = EDir(tmp1)
		else:
			self.direction = None
		
		return offset


class Bomb(object):

	@staticmethod
	def name():
		return 'Bomb'


	def __init__(self):
		self.initialize()
	

	def initialize(self):
		return
	

	def serialize(self):
		s = b''
		
		return s
	

	def deserialize(self, s, offset=0):
		return offset
