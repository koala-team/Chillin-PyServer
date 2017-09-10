# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECell(Enum):
	Empty = 0
	X = 1
	O = 2


class World(object):

	@staticmethod
	def name():
		return 'World'


	def __init__(self, board=None):
		self.initialize(board)
	

	def initialize(self, board=None):
		self.board = board
	

	def serialize(self):
		s = b''
		
		# serialize self.board
		s += b'\x00' if self.board is None else b'\x01'
		if self.board is not None:
			for tmp0 in range(3):
				for tmp1 in range(3):
					s += b'\x00' if self.board[tmp0][tmp1] is None else b'\x01'
					if self.board[tmp0][tmp1] is not None:
						s += struct.pack('B', self.board[tmp0][tmp1].value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.board
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.board = [[None for _ in range(3)] for _ in range(3)]
			for tmp3 in range(3):
				for tmp4 in range(3):
					tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					if tmp5:
						tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						self.board[tmp3][tmp4] = ECell(tmp6)
					else:
						self.board[tmp3][tmp4] = None
		else:
			self.board = None
		
		return offset
