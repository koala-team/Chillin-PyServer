# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECellType(Enum):
	Empty = 0
	DestroyableBlock = 1
	UndestroyableBlock = 2


class Cell(object):

	@staticmethod
	def name():
		return 'Cell'


	def __init__(self, type=None):
		self.initialize(type)
	

	def initialize(self, type=None):
		self.type = type
	

	def serialize(self):
		s = b''
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('B', self.type.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.type
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			self.type = ECellType(tmp1)
		else:
			self.type = None
		
		return offset


class Bomberman(object):

	@staticmethod
	def name():
		return 'Bomberman'


	def __init__(self, x=None, y=None, bomb_level=None, is_dead=None):
		self.initialize(x, y, bomb_level, is_dead)
	

	def initialize(self, x=None, y=None, bomb_level=None, is_dead=None):
		self.x = x
		self.y = y
		self.bomb_level = bomb_level
		self.is_dead = is_dead
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('B', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('B', self.y)
		
		# serialize self.bomb_level
		s += b'\x00' if self.bomb_level is None else b'\x01'
		if self.bomb_level is not None:
			s += struct.pack('B', self.bomb_level)
		
		# serialize self.is_dead
		s += b'\x00' if self.is_dead is None else b'\x01'
		if self.is_dead is not None:
			s += struct.pack('?', self.is_dead)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.x = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.x = None
		
		# deserialize self.y
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.y = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.y = None
		
		# deserialize self.bomb_level
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.bomb_level = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.bomb_level = None
		
		# deserialize self.is_dead
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.is_dead = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_dead = None
		
		return offset


class Bomb(object):

	@staticmethod
	def name():
		return 'Bomb'


	def __init__(self, x=None, y=None, timer=None, level=None):
		self.initialize(x, y, timer, level)
	

	def initialize(self, x=None, y=None, timer=None, level=None):
		self.x = x
		self.y = y
		self.timer = timer
		self.level = level
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('B', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('B', self.y)
		
		# serialize self.timer
		s += b'\x00' if self.timer is None else b'\x01'
		if self.timer is not None:
			s += struct.pack('B', self.timer)
		
		# serialize self.level
		s += b'\x00' if self.level is None else b'\x01'
		if self.level is not None:
			s += struct.pack('B', self.level)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.x = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.x = None
		
		# deserialize self.y
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.y = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.y = None
		
		# deserialize self.timer
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.timer = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.timer = None
		
		# deserialize self.level
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			self.level = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.level = None
		
		return offset


class Explosion(object):

	@staticmethod
	def name():
		return 'Explosion'


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
			s += struct.pack('B', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('B', self.y)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.x = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.x = None
		
		# deserialize self.y
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.y = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.y = None
		
		return offset


class World(object):

	@staticmethod
	def name():
		return 'World'


	def __init__(self, board=None, bombermans=None, bombs=None, explosions=None):
		self.initialize(board, bombermans, bombs, explosions)
	

	def initialize(self, board=None, bombermans=None, bombs=None, explosions=None):
		self.board = board
		self.bombermans = bombermans
		self.bombs = bombs
		self.explosions = explosions
	

	def serialize(self):
		s = b''
		
		# serialize self.board
		s += b'\x00' if self.board is None else b'\x01'
		if self.board is not None:
			tmp12 = b''
			tmp12 += struct.pack('I', len(self.board))
			while len(tmp12) and tmp12[-1] == b'\x00'[0]:
				tmp12 = tmp12[:-1]
			s += struct.pack('B', len(tmp12))
			s += tmp12
			
			for tmp13 in self.board:
				s += b'\x00' if tmp13 is None else b'\x01'
				if tmp13 is not None:
					tmp14 = b''
					tmp14 += struct.pack('I', len(tmp13))
					while len(tmp14) and tmp14[-1] == b'\x00'[0]:
						tmp14 = tmp14[:-1]
					s += struct.pack('B', len(tmp14))
					s += tmp14
					
					for tmp15 in tmp13:
						s += b'\x00' if tmp15 is None else b'\x01'
						if tmp15 is not None:
							s += tmp15.serialize()
		
		# serialize self.bombermans
		s += b'\x00' if self.bombermans is None else b'\x01'
		if self.bombermans is not None:
			tmp16 = b''
			tmp16 += struct.pack('I', len(self.bombermans))
			while len(tmp16) and tmp16[-1] == b'\x00'[0]:
				tmp16 = tmp16[:-1]
			s += struct.pack('B', len(tmp16))
			s += tmp16
			
			for tmp17 in self.bombermans:
				s += b'\x00' if tmp17 is None else b'\x01'
				if tmp17 is not None:
					tmp18 = b''
					tmp18 += struct.pack('I', len(tmp17))
					while len(tmp18) and tmp18[-1] == b'\x00'[0]:
						tmp18 = tmp18[:-1]
					s += struct.pack('B', len(tmp18))
					s += tmp18
					
					s += tmp17.encode('ISO-8859-1') if PY3 else tmp17
				s += b'\x00' if self.bombermans[tmp17] is None else b'\x01'
				if self.bombermans[tmp17] is not None:
					s += self.bombermans[tmp17].serialize()
		
		# serialize self.bombs
		s += b'\x00' if self.bombs is None else b'\x01'
		if self.bombs is not None:
			tmp19 = b''
			tmp19 += struct.pack('I', len(self.bombs))
			while len(tmp19) and tmp19[-1] == b'\x00'[0]:
				tmp19 = tmp19[:-1]
			s += struct.pack('B', len(tmp19))
			s += tmp19
			
			for tmp20 in self.bombs:
				s += b'\x00' if tmp20 is None else b'\x01'
				if tmp20 is not None:
					tmp21 = b''
					tmp21 += struct.pack('I', len(tmp20))
					while len(tmp21) and tmp21[-1] == b'\x00'[0]:
						tmp21 = tmp21[:-1]
					s += struct.pack('B', len(tmp21))
					s += tmp21
					
					s += tmp20.encode('ISO-8859-1') if PY3 else tmp20
				s += b'\x00' if self.bombs[tmp20] is None else b'\x01'
				if self.bombs[tmp20] is not None:
					tmp22 = b''
					tmp22 += struct.pack('I', len(self.bombs[tmp20]))
					while len(tmp22) and tmp22[-1] == b'\x00'[0]:
						tmp22 = tmp22[:-1]
					s += struct.pack('B', len(tmp22))
					s += tmp22
					
					for tmp23 in self.bombs[tmp20]:
						s += b'\x00' if tmp23 is None else b'\x01'
						if tmp23 is not None:
							s += tmp23.serialize()
		
		# serialize self.explosions
		s += b'\x00' if self.explosions is None else b'\x01'
		if self.explosions is not None:
			tmp24 = b''
			tmp24 += struct.pack('I', len(self.explosions))
			while len(tmp24) and tmp24[-1] == b'\x00'[0]:
				tmp24 = tmp24[:-1]
			s += struct.pack('B', len(tmp24))
			s += tmp24
			
			for tmp25 in self.explosions:
				s += b'\x00' if tmp25 is None else b'\x01'
				if tmp25 is not None:
					s += tmp25.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.board
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
			tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp28 = s[offset:offset + tmp27]
			offset += tmp27
			tmp28 += b'\x00' * (4 - tmp27)
			tmp29 = struct.unpack('I', tmp28)[0]
			
			self.board = []
			for tmp30 in range(tmp29):
				tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp32:
					tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp34 = s[offset:offset + tmp33]
					offset += tmp33
					tmp34 += b'\x00' * (4 - tmp33)
					tmp35 = struct.unpack('I', tmp34)[0]
					
					tmp31 = []
					for tmp36 in range(tmp35):
						tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp38:
							tmp37 = Cell()
							offset = tmp37.deserialize(s, offset)
						else:
							tmp37 = None
						tmp31.append(tmp37)
				else:
					tmp31 = None
				self.board.append(tmp31)
		else:
			self.board = None
		
		# deserialize self.bombermans
		tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp39:
			tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp41 = s[offset:offset + tmp40]
			offset += tmp40
			tmp41 += b'\x00' * (4 - tmp40)
			tmp42 = struct.unpack('I', tmp41)[0]
			
			self.bombermans = {}
			for tmp43 in range(tmp42):
				tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp46:
					tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp48 = s[offset:offset + tmp47]
					offset += tmp47
					tmp48 += b'\x00' * (4 - tmp47)
					tmp49 = struct.unpack('I', tmp48)[0]
					
					tmp44 = s[offset:offset + tmp49].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp49]
					offset += tmp49
				else:
					tmp44 = None
				tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp50:
					tmp45 = Bomberman()
					offset = tmp45.deserialize(s, offset)
				else:
					tmp45 = None
				self.bombermans[tmp44] = tmp45
		else:
			self.bombermans = None
		
		# deserialize self.bombs
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp53 = s[offset:offset + tmp52]
			offset += tmp52
			tmp53 += b'\x00' * (4 - tmp52)
			tmp54 = struct.unpack('I', tmp53)[0]
			
			self.bombs = {}
			for tmp55 in range(tmp54):
				tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp58:
					tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp60 = s[offset:offset + tmp59]
					offset += tmp59
					tmp60 += b'\x00' * (4 - tmp59)
					tmp61 = struct.unpack('I', tmp60)[0]
					
					tmp56 = s[offset:offset + tmp61].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp61]
					offset += tmp61
				else:
					tmp56 = None
				tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp62:
					tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp64 = s[offset:offset + tmp63]
					offset += tmp63
					tmp64 += b'\x00' * (4 - tmp63)
					tmp65 = struct.unpack('I', tmp64)[0]
					
					tmp57 = []
					for tmp66 in range(tmp65):
						tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp68:
							tmp67 = Bomb()
							offset = tmp67.deserialize(s, offset)
						else:
							tmp67 = None
						tmp57.append(tmp67)
				else:
					tmp57 = None
				self.bombs[tmp56] = tmp57
		else:
			self.bombs = None
		
		# deserialize self.explosions
		tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp69:
			tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp71 = s[offset:offset + tmp70]
			offset += tmp70
			tmp71 += b'\x00' * (4 - tmp70)
			tmp72 = struct.unpack('I', tmp71)[0]
			
			self.explosions = []
			for tmp73 in range(tmp72):
				tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp75:
					tmp74 = Explosion()
					offset = tmp74.deserialize(s, offset)
				else:
					tmp74 = None
				self.explosions.append(tmp74)
		else:
			self.explosions = None
		
		return offset
