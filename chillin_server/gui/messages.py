# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Message(object):

	@staticmethod
	def name():
		return 'Message'


	def __init__(self, type=None, payload=None):
		self.initialize(type, payload)
	

	def initialize(self, type=None, payload=None):
		self.type = type
		self.payload = payload
	

	def serialize(self):
		s = b''
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			tmp0 = b''
			tmp0 += struct.pack('I', len(self.type))
			while len(tmp0) and tmp0[-1] == b'\x00'[0]:
				tmp0 = tmp0[:-1]
			s += struct.pack('B', len(tmp0))
			s += tmp0
			
			s += self.type.encode('ISO-8859-1') if PY3 else self.type
		
		# serialize self.payload
		s += b'\x00' if self.payload is None else b'\x01'
		if self.payload is not None:
			tmp1 = b''
			tmp1 += struct.pack('I', len(self.payload))
			while len(tmp1) and tmp1[-1] == b'\x00'[0]:
				tmp1 = tmp1[:-1]
			s += struct.pack('B', len(tmp1))
			s += tmp1
			
			s += self.payload.encode('ISO-8859-1') if PY3 else self.payload
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.type
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp4 = s[offset:offset + tmp3]
			offset += tmp3
			tmp4 += b'\x00' * (4 - tmp3)
			tmp5 = struct.unpack('I', tmp4)[0]
			
			self.type = s[offset:offset + tmp5].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp5]
			offset += tmp5
		else:
			self.type = None
		
		# deserialize self.payload
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp8 = s[offset:offset + tmp7]
			offset += tmp7
			tmp8 += b'\x00' * (4 - tmp7)
			tmp9 = struct.unpack('I', tmp8)[0]
			
			self.payload = s[offset:offset + tmp9].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp9]
			offset += tmp9
		else:
			self.payload = None
		
		return offset


class Auth(object):

	@staticmethod
	def name():
		return 'Auth'


	def __init__(self, authenticated=None):
		self.initialize(authenticated)
	

	def initialize(self, authenticated=None):
		self.authenticated = authenticated
	

	def serialize(self):
		s = b''
		
		# serialize self.authenticated
		s += b'\x00' if self.authenticated is None else b'\x01'
		if self.authenticated is not None:
			s += struct.pack('?', self.authenticated)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.authenticated
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.authenticated = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.authenticated = None
		
		return offset


class GameInfo(object):

	@staticmethod
	def name():
		return 'GameInfo'


	def __init__(self, game_name=None, sides=None, gui_cycle_duration=None, gui_side_colors=None):
		self.initialize(game_name, sides, gui_cycle_duration, gui_side_colors)
	

	def initialize(self, game_name=None, sides=None, gui_cycle_duration=None, gui_side_colors=None):
		self.game_name = game_name
		self.sides = sides
		self.gui_cycle_duration = gui_cycle_duration
		self.gui_side_colors = gui_side_colors
	

	def serialize(self):
		s = b''
		
		# serialize self.game_name
		s += b'\x00' if self.game_name is None else b'\x01'
		if self.game_name is not None:
			tmp11 = b''
			tmp11 += struct.pack('I', len(self.game_name))
			while len(tmp11) and tmp11[-1] == b'\x00'[0]:
				tmp11 = tmp11[:-1]
			s += struct.pack('B', len(tmp11))
			s += tmp11
			
			s += self.game_name.encode('ISO-8859-1') if PY3 else self.game_name
		
		# serialize self.sides
		s += b'\x00' if self.sides is None else b'\x01'
		if self.sides is not None:
			tmp12 = b''
			tmp12 += struct.pack('I', len(self.sides))
			while len(tmp12) and tmp12[-1] == b'\x00'[0]:
				tmp12 = tmp12[:-1]
			s += struct.pack('B', len(tmp12))
			s += tmp12
			
			for tmp13 in self.sides:
				s += b'\x00' if tmp13 is None else b'\x01'
				if tmp13 is not None:
					tmp14 = b''
					tmp14 += struct.pack('I', len(tmp13))
					while len(tmp14) and tmp14[-1] == b'\x00'[0]:
						tmp14 = tmp14[:-1]
					s += struct.pack('B', len(tmp14))
					s += tmp14
					
					s += tmp13.encode('ISO-8859-1') if PY3 else tmp13
				s += b'\x00' if self.sides[tmp13] is None else b'\x01'
				if self.sides[tmp13] is not None:
					tmp15 = b''
					tmp15 += struct.pack('I', len(self.sides[tmp13]))
					while len(tmp15) and tmp15[-1] == b'\x00'[0]:
						tmp15 = tmp15[:-1]
					s += struct.pack('B', len(tmp15))
					s += tmp15
					
					for tmp16 in self.sides[tmp13]:
						s += b'\x00' if tmp16 is None else b'\x01'
						if tmp16 is not None:
							tmp17 = b''
							tmp17 += struct.pack('I', len(tmp16))
							while len(tmp17) and tmp17[-1] == b'\x00'[0]:
								tmp17 = tmp17[:-1]
							s += struct.pack('B', len(tmp17))
							s += tmp17
							
							s += tmp16.encode('ISO-8859-1') if PY3 else tmp16
		
		# serialize self.gui_cycle_duration
		s += b'\x00' if self.gui_cycle_duration is None else b'\x01'
		if self.gui_cycle_duration is not None:
			s += struct.pack('f', self.gui_cycle_duration)
		
		# serialize self.gui_side_colors
		s += b'\x00' if self.gui_side_colors is None else b'\x01'
		if self.gui_side_colors is not None:
			tmp18 = b''
			tmp18 += struct.pack('I', len(self.gui_side_colors))
			while len(tmp18) and tmp18[-1] == b'\x00'[0]:
				tmp18 = tmp18[:-1]
			s += struct.pack('B', len(tmp18))
			s += tmp18
			
			for tmp19 in self.gui_side_colors:
				s += b'\x00' if tmp19 is None else b'\x01'
				if tmp19 is not None:
					tmp20 = b''
					tmp20 += struct.pack('I', len(tmp19))
					while len(tmp20) and tmp20[-1] == b'\x00'[0]:
						tmp20 = tmp20[:-1]
					s += struct.pack('B', len(tmp20))
					s += tmp20
					
					s += tmp19.encode('ISO-8859-1') if PY3 else tmp19
				s += b'\x00' if self.gui_side_colors[tmp19] is None else b'\x01'
				if self.gui_side_colors[tmp19] is not None:
					tmp21 = b''
					tmp21 += struct.pack('I', len(self.gui_side_colors[tmp19]))
					while len(tmp21) and tmp21[-1] == b'\x00'[0]:
						tmp21 = tmp21[:-1]
					s += struct.pack('B', len(tmp21))
					s += tmp21
					
					s += self.gui_side_colors[tmp19].encode('ISO-8859-1') if PY3 else self.gui_side_colors[tmp19]
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.game_name
		tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp22:
			tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp24 = s[offset:offset + tmp23]
			offset += tmp23
			tmp24 += b'\x00' * (4 - tmp23)
			tmp25 = struct.unpack('I', tmp24)[0]
			
			self.game_name = s[offset:offset + tmp25].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp25]
			offset += tmp25
		else:
			self.game_name = None
		
		# deserialize self.sides
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
			tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp28 = s[offset:offset + tmp27]
			offset += tmp27
			tmp28 += b'\x00' * (4 - tmp27)
			tmp29 = struct.unpack('I', tmp28)[0]
			
			self.sides = {}
			for tmp30 in range(tmp29):
				tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp33:
					tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp35 = s[offset:offset + tmp34]
					offset += tmp34
					tmp35 += b'\x00' * (4 - tmp34)
					tmp36 = struct.unpack('I', tmp35)[0]
					
					tmp31 = s[offset:offset + tmp36].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp36]
					offset += tmp36
				else:
					tmp31 = None
				tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp37:
					tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp39 = s[offset:offset + tmp38]
					offset += tmp38
					tmp39 += b'\x00' * (4 - tmp38)
					tmp40 = struct.unpack('I', tmp39)[0]
					
					tmp32 = []
					for tmp41 in range(tmp40):
						tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp43:
							tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp45 = s[offset:offset + tmp44]
							offset += tmp44
							tmp45 += b'\x00' * (4 - tmp44)
							tmp46 = struct.unpack('I', tmp45)[0]
							
							tmp42 = s[offset:offset + tmp46].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp46]
							offset += tmp46
						else:
							tmp42 = None
						tmp32.append(tmp42)
				else:
					tmp32 = None
				self.sides[tmp31] = tmp32
		else:
			self.sides = None
		
		# deserialize self.gui_cycle_duration
		tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp47:
			self.gui_cycle_duration = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.gui_cycle_duration = None
		
		# deserialize self.gui_side_colors
		tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp48:
			tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp50 = s[offset:offset + tmp49]
			offset += tmp49
			tmp50 += b'\x00' * (4 - tmp49)
			tmp51 = struct.unpack('I', tmp50)[0]
			
			self.gui_side_colors = {}
			for tmp52 in range(tmp51):
				tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp55:
					tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp57 = s[offset:offset + tmp56]
					offset += tmp56
					tmp57 += b'\x00' * (4 - tmp56)
					tmp58 = struct.unpack('I', tmp57)[0]
					
					tmp53 = s[offset:offset + tmp58].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp58]
					offset += tmp58
				else:
					tmp53 = None
				tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp59:
					tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp61 = s[offset:offset + tmp60]
					offset += tmp60
					tmp61 += b'\x00' * (4 - tmp60)
					tmp62 = struct.unpack('I', tmp61)[0]
					
					tmp54 = s[offset:offset + tmp62].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp62]
					offset += tmp62
				else:
					tmp54 = None
				self.gui_side_colors[tmp53] = tmp54
		else:
			self.gui_side_colors = None
		
		return offset


class AgentJoined(object):

	@staticmethod
	def name():
		return 'AgentJoined'


	def __init__(self, side_name=None, agent_name=None, team_nickname=None):
		self.initialize(side_name, agent_name, team_nickname)
	

	def initialize(self, side_name=None, agent_name=None, team_nickname=None):
		self.side_name = side_name
		self.agent_name = agent_name
		self.team_nickname = team_nickname
	

	def serialize(self):
		s = b''
		
		# serialize self.side_name
		s += b'\x00' if self.side_name is None else b'\x01'
		if self.side_name is not None:
			tmp63 = b''
			tmp63 += struct.pack('I', len(self.side_name))
			while len(tmp63) and tmp63[-1] == b'\x00'[0]:
				tmp63 = tmp63[:-1]
			s += struct.pack('B', len(tmp63))
			s += tmp63
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.agent_name
		s += b'\x00' if self.agent_name is None else b'\x01'
		if self.agent_name is not None:
			tmp64 = b''
			tmp64 += struct.pack('I', len(self.agent_name))
			while len(tmp64) and tmp64[-1] == b'\x00'[0]:
				tmp64 = tmp64[:-1]
			s += struct.pack('B', len(tmp64))
			s += tmp64
			
			s += self.agent_name.encode('ISO-8859-1') if PY3 else self.agent_name
		
		# serialize self.team_nickname
		s += b'\x00' if self.team_nickname is None else b'\x01'
		if self.team_nickname is not None:
			tmp65 = b''
			tmp65 += struct.pack('I', len(self.team_nickname))
			while len(tmp65) and tmp65[-1] == b'\x00'[0]:
				tmp65 = tmp65[:-1]
			s += struct.pack('B', len(tmp65))
			s += tmp65
			
			s += self.team_nickname.encode('ISO-8859-1') if PY3 else self.team_nickname
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.side_name
		tmp66 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp66:
			tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp68 = s[offset:offset + tmp67]
			offset += tmp67
			tmp68 += b'\x00' * (4 - tmp67)
			tmp69 = struct.unpack('I', tmp68)[0]
			
			self.side_name = s[offset:offset + tmp69].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp69]
			offset += tmp69
		else:
			self.side_name = None
		
		# deserialize self.agent_name
		tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp70:
			tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp72 = s[offset:offset + tmp71]
			offset += tmp71
			tmp72 += b'\x00' * (4 - tmp71)
			tmp73 = struct.unpack('I', tmp72)[0]
			
			self.agent_name = s[offset:offset + tmp73].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp73]
			offset += tmp73
		else:
			self.agent_name = None
		
		# deserialize self.team_nickname
		tmp74 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp74:
			tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp76 = s[offset:offset + tmp75]
			offset += tmp75
			tmp76 += b'\x00' * (4 - tmp75)
			tmp77 = struct.unpack('I', tmp76)[0]
			
			self.team_nickname = s[offset:offset + tmp77].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp77]
			offset += tmp77
		else:
			self.team_nickname = None
		
		return offset


class AgentLeft(object):

	@staticmethod
	def name():
		return 'AgentLeft'


	def __init__(self, side_name=None, agent_name=None):
		self.initialize(side_name, agent_name)
	

	def initialize(self, side_name=None, agent_name=None):
		self.side_name = side_name
		self.agent_name = agent_name
	

	def serialize(self):
		s = b''
		
		# serialize self.side_name
		s += b'\x00' if self.side_name is None else b'\x01'
		if self.side_name is not None:
			tmp78 = b''
			tmp78 += struct.pack('I', len(self.side_name))
			while len(tmp78) and tmp78[-1] == b'\x00'[0]:
				tmp78 = tmp78[:-1]
			s += struct.pack('B', len(tmp78))
			s += tmp78
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.agent_name
		s += b'\x00' if self.agent_name is None else b'\x01'
		if self.agent_name is not None:
			tmp79 = b''
			tmp79 += struct.pack('I', len(self.agent_name))
			while len(tmp79) and tmp79[-1] == b'\x00'[0]:
				tmp79 = tmp79[:-1]
			s += struct.pack('B', len(tmp79))
			s += tmp79
			
			s += self.agent_name.encode('ISO-8859-1') if PY3 else self.agent_name
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.side_name
		tmp80 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp80:
			tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp82 = s[offset:offset + tmp81]
			offset += tmp81
			tmp82 += b'\x00' * (4 - tmp81)
			tmp83 = struct.unpack('I', tmp82)[0]
			
			self.side_name = s[offset:offset + tmp83].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp83]
			offset += tmp83
		else:
			self.side_name = None
		
		# deserialize self.agent_name
		tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp84:
			tmp85 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp86 = s[offset:offset + tmp85]
			offset += tmp85
			tmp86 += b'\x00' * (4 - tmp85)
			tmp87 = struct.unpack('I', tmp86)[0]
			
			self.agent_name = s[offset:offset + tmp87].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp87]
			offset += tmp87
		else:
			self.agent_name = None
		
		return offset


class StartGame(object):

	@staticmethod
	def name():
		return 'StartGame'


	def __init__(self, start_time=None):
		self.initialize(start_time)
	

	def initialize(self, start_time=None):
		self.start_time = start_time
	

	def serialize(self):
		s = b''
		
		# serialize self.start_time
		s += b'\x00' if self.start_time is None else b'\x01'
		if self.start_time is not None:
			s += struct.pack('I', self.start_time)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.start_time
		tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp88:
			self.start_time = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.start_time = None
		
		return offset


class EndGame(object):

	@staticmethod
	def name():
		return 'EndGame'


	def __init__(self, winner_sidename=None, details=None):
		self.initialize(winner_sidename, details)
	

	def initialize(self, winner_sidename=None, details=None):
		self.winner_sidename = winner_sidename
		self.details = details
	

	def serialize(self):
		s = b''
		
		# serialize self.winner_sidename
		s += b'\x00' if self.winner_sidename is None else b'\x01'
		if self.winner_sidename is not None:
			tmp89 = b''
			tmp89 += struct.pack('I', len(self.winner_sidename))
			while len(tmp89) and tmp89[-1] == b'\x00'[0]:
				tmp89 = tmp89[:-1]
			s += struct.pack('B', len(tmp89))
			s += tmp89
			
			s += self.winner_sidename.encode('ISO-8859-1') if PY3 else self.winner_sidename
		
		# serialize self.details
		s += b'\x00' if self.details is None else b'\x01'
		if self.details is not None:
			tmp90 = b''
			tmp90 += struct.pack('I', len(self.details))
			while len(tmp90) and tmp90[-1] == b'\x00'[0]:
				tmp90 = tmp90[:-1]
			s += struct.pack('B', len(tmp90))
			s += tmp90
			
			for tmp91 in self.details:
				s += b'\x00' if tmp91 is None else b'\x01'
				if tmp91 is not None:
					tmp92 = b''
					tmp92 += struct.pack('I', len(tmp91))
					while len(tmp92) and tmp92[-1] == b'\x00'[0]:
						tmp92 = tmp92[:-1]
					s += struct.pack('B', len(tmp92))
					s += tmp92
					
					s += tmp91.encode('ISO-8859-1') if PY3 else tmp91
				s += b'\x00' if self.details[tmp91] is None else b'\x01'
				if self.details[tmp91] is not None:
					tmp93 = b''
					tmp93 += struct.pack('I', len(self.details[tmp91]))
					while len(tmp93) and tmp93[-1] == b'\x00'[0]:
						tmp93 = tmp93[:-1]
					s += struct.pack('B', len(tmp93))
					s += tmp93
					
					for tmp94 in self.details[tmp91]:
						s += b'\x00' if tmp94 is None else b'\x01'
						if tmp94 is not None:
							tmp95 = b''
							tmp95 += struct.pack('I', len(tmp94))
							while len(tmp95) and tmp95[-1] == b'\x00'[0]:
								tmp95 = tmp95[:-1]
							s += struct.pack('B', len(tmp95))
							s += tmp95
							
							s += tmp94.encode('ISO-8859-1') if PY3 else tmp94
						s += b'\x00' if self.details[tmp91][tmp94] is None else b'\x01'
						if self.details[tmp91][tmp94] is not None:
							tmp96 = b''
							tmp96 += struct.pack('I', len(self.details[tmp91][tmp94]))
							while len(tmp96) and tmp96[-1] == b'\x00'[0]:
								tmp96 = tmp96[:-1]
							s += struct.pack('B', len(tmp96))
							s += tmp96
							
							s += self.details[tmp91][tmp94].encode('ISO-8859-1') if PY3 else self.details[tmp91][tmp94]
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.winner_sidename
		tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp97:
			tmp98 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp99 = s[offset:offset + tmp98]
			offset += tmp98
			tmp99 += b'\x00' * (4 - tmp98)
			tmp100 = struct.unpack('I', tmp99)[0]
			
			self.winner_sidename = s[offset:offset + tmp100].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp100]
			offset += tmp100
		else:
			self.winner_sidename = None
		
		# deserialize self.details
		tmp101 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp101:
			tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp103 = s[offset:offset + tmp102]
			offset += tmp102
			tmp103 += b'\x00' * (4 - tmp102)
			tmp104 = struct.unpack('I', tmp103)[0]
			
			self.details = {}
			for tmp105 in range(tmp104):
				tmp108 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp108:
					tmp109 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp110 = s[offset:offset + tmp109]
					offset += tmp109
					tmp110 += b'\x00' * (4 - tmp109)
					tmp111 = struct.unpack('I', tmp110)[0]
					
					tmp106 = s[offset:offset + tmp111].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp111]
					offset += tmp111
				else:
					tmp106 = None
				tmp112 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp112:
					tmp113 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp114 = s[offset:offset + tmp113]
					offset += tmp113
					tmp114 += b'\x00' * (4 - tmp113)
					tmp115 = struct.unpack('I', tmp114)[0]
					
					tmp107 = {}
					for tmp116 in range(tmp115):
						tmp119 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp119:
							tmp120 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp121 = s[offset:offset + tmp120]
							offset += tmp120
							tmp121 += b'\x00' * (4 - tmp120)
							tmp122 = struct.unpack('I', tmp121)[0]
							
							tmp117 = s[offset:offset + tmp122].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp122]
							offset += tmp122
						else:
							tmp117 = None
						tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp123:
							tmp124 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp125 = s[offset:offset + tmp124]
							offset += tmp124
							tmp125 += b'\x00' * (4 - tmp124)
							tmp126 = struct.unpack('I', tmp125)[0]
							
							tmp118 = s[offset:offset + tmp126].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp126]
							offset += tmp126
						else:
							tmp118 = None
						tmp107[tmp117] = tmp118
				else:
					tmp107 = None
				self.details[tmp106] = tmp107
		else:
			self.details = None
		
		return offset


class SceneActions(object):

	@staticmethod
	def name():
		return 'SceneActions'


	def __init__(self, action_types=None, action_payloads=None):
		self.initialize(action_types, action_payloads)
	

	def initialize(self, action_types=None, action_payloads=None):
		self.action_types = action_types
		self.action_payloads = action_payloads
	

	def serialize(self):
		s = b''
		
		# serialize self.action_types
		s += b'\x00' if self.action_types is None else b'\x01'
		if self.action_types is not None:
			tmp127 = b''
			tmp127 += struct.pack('I', len(self.action_types))
			while len(tmp127) and tmp127[-1] == b'\x00'[0]:
				tmp127 = tmp127[:-1]
			s += struct.pack('B', len(tmp127))
			s += tmp127
			
			for tmp128 in self.action_types:
				s += b'\x00' if tmp128 is None else b'\x01'
				if tmp128 is not None:
					tmp129 = b''
					tmp129 += struct.pack('I', len(tmp128))
					while len(tmp129) and tmp129[-1] == b'\x00'[0]:
						tmp129 = tmp129[:-1]
					s += struct.pack('B', len(tmp129))
					s += tmp129
					
					s += tmp128.encode('ISO-8859-1') if PY3 else tmp128
		
		# serialize self.action_payloads
		s += b'\x00' if self.action_payloads is None else b'\x01'
		if self.action_payloads is not None:
			tmp130 = b''
			tmp130 += struct.pack('I', len(self.action_payloads))
			while len(tmp130) and tmp130[-1] == b'\x00'[0]:
				tmp130 = tmp130[:-1]
			s += struct.pack('B', len(tmp130))
			s += tmp130
			
			for tmp131 in self.action_payloads:
				s += b'\x00' if tmp131 is None else b'\x01'
				if tmp131 is not None:
					tmp132 = b''
					tmp132 += struct.pack('I', len(tmp131))
					while len(tmp132) and tmp132[-1] == b'\x00'[0]:
						tmp132 = tmp132[:-1]
					s += struct.pack('B', len(tmp132))
					s += tmp132
					
					s += tmp131.encode('ISO-8859-1') if PY3 else tmp131
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.action_types
		tmp133 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp133:
			tmp134 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp135 = s[offset:offset + tmp134]
			offset += tmp134
			tmp135 += b'\x00' * (4 - tmp134)
			tmp136 = struct.unpack('I', tmp135)[0]
			
			self.action_types = []
			for tmp137 in range(tmp136):
				tmp139 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp139:
					tmp140 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp141 = s[offset:offset + tmp140]
					offset += tmp140
					tmp141 += b'\x00' * (4 - tmp140)
					tmp142 = struct.unpack('I', tmp141)[0]
					
					tmp138 = s[offset:offset + tmp142].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp142]
					offset += tmp142
				else:
					tmp138 = None
				self.action_types.append(tmp138)
		else:
			self.action_types = None
		
		# deserialize self.action_payloads
		tmp143 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp143:
			tmp144 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp145 = s[offset:offset + tmp144]
			offset += tmp144
			tmp145 += b'\x00' * (4 - tmp144)
			tmp146 = struct.unpack('I', tmp145)[0]
			
			self.action_payloads = []
			for tmp147 in range(tmp146):
				tmp149 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp149:
					tmp150 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp151 = s[offset:offset + tmp150]
					offset += tmp150
					tmp151 += b'\x00' * (4 - tmp150)
					tmp152 = struct.unpack('I', tmp151)[0]
					
					tmp148 = s[offset:offset + tmp152].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp152]
					offset += tmp152
				else:
					tmp148 = None
				self.action_payloads.append(tmp148)
		else:
			self.action_payloads = None
		
		return offset
