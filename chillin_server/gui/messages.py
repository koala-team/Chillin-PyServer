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


	def __init__(self, game_name=None, sides=None, gui_cycle_duration=None):
		self.initialize(game_name, sides, gui_cycle_duration)
	

	def initialize(self, game_name=None, sides=None, gui_cycle_duration=None):
		self.game_name = game_name
		self.sides = sides
		self.gui_cycle_duration = gui_cycle_duration
	

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
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.game_name
		tmp18 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp18:
			tmp19 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp20 = s[offset:offset + tmp19]
			offset += tmp19
			tmp20 += b'\x00' * (4 - tmp19)
			tmp21 = struct.unpack('I', tmp20)[0]
			
			self.game_name = s[offset:offset + tmp21].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp21]
			offset += tmp21
		else:
			self.game_name = None
		
		# deserialize self.sides
		tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp22:
			tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp24 = s[offset:offset + tmp23]
			offset += tmp23
			tmp24 += b'\x00' * (4 - tmp23)
			tmp25 = struct.unpack('I', tmp24)[0]
			
			self.sides = {}
			for tmp26 in range(tmp25):
				tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp29:
					tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp31 = s[offset:offset + tmp30]
					offset += tmp30
					tmp31 += b'\x00' * (4 - tmp30)
					tmp32 = struct.unpack('I', tmp31)[0]
					
					tmp27 = s[offset:offset + tmp32].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp32]
					offset += tmp32
				else:
					tmp27 = None
				tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp33:
					tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp35 = s[offset:offset + tmp34]
					offset += tmp34
					tmp35 += b'\x00' * (4 - tmp34)
					tmp36 = struct.unpack('I', tmp35)[0]
					
					tmp28 = []
					for tmp37 in range(tmp36):
						tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp39:
							tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp41 = s[offset:offset + tmp40]
							offset += tmp40
							tmp41 += b'\x00' * (4 - tmp40)
							tmp42 = struct.unpack('I', tmp41)[0]
							
							tmp38 = s[offset:offset + tmp42].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp42]
							offset += tmp42
						else:
							tmp38 = None
						tmp28.append(tmp38)
				else:
					tmp28 = None
				self.sides[tmp27] = tmp28
		else:
			self.sides = None
		
		# deserialize self.gui_cycle_duration
		tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp43:
			self.gui_cycle_duration = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.gui_cycle_duration = None
		
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
			tmp44 = b''
			tmp44 += struct.pack('I', len(self.side_name))
			while len(tmp44) and tmp44[-1] == b'\x00'[0]:
				tmp44 = tmp44[:-1]
			s += struct.pack('B', len(tmp44))
			s += tmp44
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.agent_name
		s += b'\x00' if self.agent_name is None else b'\x01'
		if self.agent_name is not None:
			tmp45 = b''
			tmp45 += struct.pack('I', len(self.agent_name))
			while len(tmp45) and tmp45[-1] == b'\x00'[0]:
				tmp45 = tmp45[:-1]
			s += struct.pack('B', len(tmp45))
			s += tmp45
			
			s += self.agent_name.encode('ISO-8859-1') if PY3 else self.agent_name
		
		# serialize self.team_nickname
		s += b'\x00' if self.team_nickname is None else b'\x01'
		if self.team_nickname is not None:
			tmp46 = b''
			tmp46 += struct.pack('I', len(self.team_nickname))
			while len(tmp46) and tmp46[-1] == b'\x00'[0]:
				tmp46 = tmp46[:-1]
			s += struct.pack('B', len(tmp46))
			s += tmp46
			
			s += self.team_nickname.encode('ISO-8859-1') if PY3 else self.team_nickname
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.side_name
		tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp47:
			tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp49 = s[offset:offset + tmp48]
			offset += tmp48
			tmp49 += b'\x00' * (4 - tmp48)
			tmp50 = struct.unpack('I', tmp49)[0]
			
			self.side_name = s[offset:offset + tmp50].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp50]
			offset += tmp50
		else:
			self.side_name = None
		
		# deserialize self.agent_name
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp53 = s[offset:offset + tmp52]
			offset += tmp52
			tmp53 += b'\x00' * (4 - tmp52)
			tmp54 = struct.unpack('I', tmp53)[0]
			
			self.agent_name = s[offset:offset + tmp54].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp54]
			offset += tmp54
		else:
			self.agent_name = None
		
		# deserialize self.team_nickname
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp57 = s[offset:offset + tmp56]
			offset += tmp56
			tmp57 += b'\x00' * (4 - tmp56)
			tmp58 = struct.unpack('I', tmp57)[0]
			
			self.team_nickname = s[offset:offset + tmp58].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp58]
			offset += tmp58
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
			tmp59 = b''
			tmp59 += struct.pack('I', len(self.side_name))
			while len(tmp59) and tmp59[-1] == b'\x00'[0]:
				tmp59 = tmp59[:-1]
			s += struct.pack('B', len(tmp59))
			s += tmp59
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.agent_name
		s += b'\x00' if self.agent_name is None else b'\x01'
		if self.agent_name is not None:
			tmp60 = b''
			tmp60 += struct.pack('I', len(self.agent_name))
			while len(tmp60) and tmp60[-1] == b'\x00'[0]:
				tmp60 = tmp60[:-1]
			s += struct.pack('B', len(tmp60))
			s += tmp60
			
			s += self.agent_name.encode('ISO-8859-1') if PY3 else self.agent_name
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.side_name
		tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp61:
			tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp63 = s[offset:offset + tmp62]
			offset += tmp62
			tmp63 += b'\x00' * (4 - tmp62)
			tmp64 = struct.unpack('I', tmp63)[0]
			
			self.side_name = s[offset:offset + tmp64].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp64]
			offset += tmp64
		else:
			self.side_name = None
		
		# deserialize self.agent_name
		tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp65:
			tmp66 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp67 = s[offset:offset + tmp66]
			offset += tmp66
			tmp67 += b'\x00' * (4 - tmp66)
			tmp68 = struct.unpack('I', tmp67)[0]
			
			self.agent_name = s[offset:offset + tmp68].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp68]
			offset += tmp68
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
		tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp69:
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
			tmp70 = b''
			tmp70 += struct.pack('I', len(self.winner_sidename))
			while len(tmp70) and tmp70[-1] == b'\x00'[0]:
				tmp70 = tmp70[:-1]
			s += struct.pack('B', len(tmp70))
			s += tmp70
			
			s += self.winner_sidename.encode('ISO-8859-1') if PY3 else self.winner_sidename
		
		# serialize self.details
		s += b'\x00' if self.details is None else b'\x01'
		if self.details is not None:
			tmp71 = b''
			tmp71 += struct.pack('I', len(self.details))
			while len(tmp71) and tmp71[-1] == b'\x00'[0]:
				tmp71 = tmp71[:-1]
			s += struct.pack('B', len(tmp71))
			s += tmp71
			
			for tmp72 in self.details:
				s += b'\x00' if tmp72 is None else b'\x01'
				if tmp72 is not None:
					tmp73 = b''
					tmp73 += struct.pack('I', len(tmp72))
					while len(tmp73) and tmp73[-1] == b'\x00'[0]:
						tmp73 = tmp73[:-1]
					s += struct.pack('B', len(tmp73))
					s += tmp73
					
					s += tmp72.encode('ISO-8859-1') if PY3 else tmp72
				s += b'\x00' if self.details[tmp72] is None else b'\x01'
				if self.details[tmp72] is not None:
					tmp74 = b''
					tmp74 += struct.pack('I', len(self.details[tmp72]))
					while len(tmp74) and tmp74[-1] == b'\x00'[0]:
						tmp74 = tmp74[:-1]
					s += struct.pack('B', len(tmp74))
					s += tmp74
					
					for tmp75 in self.details[tmp72]:
						s += b'\x00' if tmp75 is None else b'\x01'
						if tmp75 is not None:
							tmp76 = b''
							tmp76 += struct.pack('I', len(tmp75))
							while len(tmp76) and tmp76[-1] == b'\x00'[0]:
								tmp76 = tmp76[:-1]
							s += struct.pack('B', len(tmp76))
							s += tmp76
							
							s += tmp75.encode('ISO-8859-1') if PY3 else tmp75
						s += b'\x00' if self.details[tmp72][tmp75] is None else b'\x01'
						if self.details[tmp72][tmp75] is not None:
							tmp77 = b''
							tmp77 += struct.pack('I', len(self.details[tmp72][tmp75]))
							while len(tmp77) and tmp77[-1] == b'\x00'[0]:
								tmp77 = tmp77[:-1]
							s += struct.pack('B', len(tmp77))
							s += tmp77
							
							s += self.details[tmp72][tmp75].encode('ISO-8859-1') if PY3 else self.details[tmp72][tmp75]
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.winner_sidename
		tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp78:
			tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp80 = s[offset:offset + tmp79]
			offset += tmp79
			tmp80 += b'\x00' * (4 - tmp79)
			tmp81 = struct.unpack('I', tmp80)[0]
			
			self.winner_sidename = s[offset:offset + tmp81].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp81]
			offset += tmp81
		else:
			self.winner_sidename = None
		
		# deserialize self.details
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp84 = s[offset:offset + tmp83]
			offset += tmp83
			tmp84 += b'\x00' * (4 - tmp83)
			tmp85 = struct.unpack('I', tmp84)[0]
			
			self.details = {}
			for tmp86 in range(tmp85):
				tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp89:
					tmp90 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp91 = s[offset:offset + tmp90]
					offset += tmp90
					tmp91 += b'\x00' * (4 - tmp90)
					tmp92 = struct.unpack('I', tmp91)[0]
					
					tmp87 = s[offset:offset + tmp92].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp92]
					offset += tmp92
				else:
					tmp87 = None
				tmp93 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp93:
					tmp94 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp95 = s[offset:offset + tmp94]
					offset += tmp94
					tmp95 += b'\x00' * (4 - tmp94)
					tmp96 = struct.unpack('I', tmp95)[0]
					
					tmp88 = {}
					for tmp97 in range(tmp96):
						tmp100 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp100:
							tmp101 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp102 = s[offset:offset + tmp101]
							offset += tmp101
							tmp102 += b'\x00' * (4 - tmp101)
							tmp103 = struct.unpack('I', tmp102)[0]
							
							tmp98 = s[offset:offset + tmp103].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp103]
							offset += tmp103
						else:
							tmp98 = None
						tmp104 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp104:
							tmp105 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp106 = s[offset:offset + tmp105]
							offset += tmp105
							tmp106 += b'\x00' * (4 - tmp105)
							tmp107 = struct.unpack('I', tmp106)[0]
							
							tmp99 = s[offset:offset + tmp107].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp107]
							offset += tmp107
						else:
							tmp99 = None
						tmp88[tmp98] = tmp99
				else:
					tmp88 = None
				self.details[tmp87] = tmp88
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
			tmp108 = b''
			tmp108 += struct.pack('I', len(self.action_types))
			while len(tmp108) and tmp108[-1] == b'\x00'[0]:
				tmp108 = tmp108[:-1]
			s += struct.pack('B', len(tmp108))
			s += tmp108
			
			for tmp109 in self.action_types:
				s += b'\x00' if tmp109 is None else b'\x01'
				if tmp109 is not None:
					tmp110 = b''
					tmp110 += struct.pack('I', len(tmp109))
					while len(tmp110) and tmp110[-1] == b'\x00'[0]:
						tmp110 = tmp110[:-1]
					s += struct.pack('B', len(tmp110))
					s += tmp110
					
					s += tmp109.encode('ISO-8859-1') if PY3 else tmp109
		
		# serialize self.action_payloads
		s += b'\x00' if self.action_payloads is None else b'\x01'
		if self.action_payloads is not None:
			tmp111 = b''
			tmp111 += struct.pack('I', len(self.action_payloads))
			while len(tmp111) and tmp111[-1] == b'\x00'[0]:
				tmp111 = tmp111[:-1]
			s += struct.pack('B', len(tmp111))
			s += tmp111
			
			for tmp112 in self.action_payloads:
				s += b'\x00' if tmp112 is None else b'\x01'
				if tmp112 is not None:
					tmp113 = b''
					tmp113 += struct.pack('I', len(tmp112))
					while len(tmp113) and tmp113[-1] == b'\x00'[0]:
						tmp113 = tmp113[:-1]
					s += struct.pack('B', len(tmp113))
					s += tmp113
					
					s += tmp112.encode('ISO-8859-1') if PY3 else tmp112
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.action_types
		tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp114:
			tmp115 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp116 = s[offset:offset + tmp115]
			offset += tmp115
			tmp116 += b'\x00' * (4 - tmp115)
			tmp117 = struct.unpack('I', tmp116)[0]
			
			self.action_types = []
			for tmp118 in range(tmp117):
				tmp120 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp120:
					tmp121 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp122 = s[offset:offset + tmp121]
					offset += tmp121
					tmp122 += b'\x00' * (4 - tmp121)
					tmp123 = struct.unpack('I', tmp122)[0]
					
					tmp119 = s[offset:offset + tmp123].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp123]
					offset += tmp123
				else:
					tmp119 = None
				self.action_types.append(tmp119)
		else:
			self.action_types = None
		
		# deserialize self.action_payloads
		tmp124 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp124:
			tmp125 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp126 = s[offset:offset + tmp125]
			offset += tmp125
			tmp126 += b'\x00' * (4 - tmp125)
			tmp127 = struct.unpack('I', tmp126)[0]
			
			self.action_payloads = []
			for tmp128 in range(tmp127):
				tmp130 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp130:
					tmp131 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp132 = s[offset:offset + tmp131]
					offset += tmp131
					tmp132 += b'\x00' * (4 - tmp131)
					tmp133 = struct.unpack('I', tmp132)[0]
					
					tmp129 = s[offset:offset + tmp133].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp133]
					offset += tmp133
				else:
					tmp129 = None
				self.action_payloads.append(tmp129)
		else:
			self.action_payloads = None
		
		return offset
