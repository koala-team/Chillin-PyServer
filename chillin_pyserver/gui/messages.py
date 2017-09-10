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


	def __init__(self, game_name=None, sides=None):
		self.initialize(game_name, sides)
	

	def initialize(self, game_name=None, sides=None):
		self.game_name = game_name
		self.sides = sides
	

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
			tmp43 = b''
			tmp43 += struct.pack('I', len(self.side_name))
			while len(tmp43) and tmp43[-1] == b'\x00'[0]:
				tmp43 = tmp43[:-1]
			s += struct.pack('B', len(tmp43))
			s += tmp43
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.agent_name
		s += b'\x00' if self.agent_name is None else b'\x01'
		if self.agent_name is not None:
			tmp44 = b''
			tmp44 += struct.pack('I', len(self.agent_name))
			while len(tmp44) and tmp44[-1] == b'\x00'[0]:
				tmp44 = tmp44[:-1]
			s += struct.pack('B', len(tmp44))
			s += tmp44
			
			s += self.agent_name.encode('ISO-8859-1') if PY3 else self.agent_name
		
		# serialize self.team_nickname
		s += b'\x00' if self.team_nickname is None else b'\x01'
		if self.team_nickname is not None:
			tmp45 = b''
			tmp45 += struct.pack('I', len(self.team_nickname))
			while len(tmp45) and tmp45[-1] == b'\x00'[0]:
				tmp45 = tmp45[:-1]
			s += struct.pack('B', len(tmp45))
			s += tmp45
			
			s += self.team_nickname.encode('ISO-8859-1') if PY3 else self.team_nickname
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.side_name
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
			tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp48 = s[offset:offset + tmp47]
			offset += tmp47
			tmp48 += b'\x00' * (4 - tmp47)
			tmp49 = struct.unpack('I', tmp48)[0]
			
			self.side_name = s[offset:offset + tmp49].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp49]
			offset += tmp49
		else:
			self.side_name = None
		
		# deserialize self.agent_name
		tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp50:
			tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp52 = s[offset:offset + tmp51]
			offset += tmp51
			tmp52 += b'\x00' * (4 - tmp51)
			tmp53 = struct.unpack('I', tmp52)[0]
			
			self.agent_name = s[offset:offset + tmp53].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp53]
			offset += tmp53
		else:
			self.agent_name = None
		
		# deserialize self.team_nickname
		tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp54:
			tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp56 = s[offset:offset + tmp55]
			offset += tmp55
			tmp56 += b'\x00' * (4 - tmp55)
			tmp57 = struct.unpack('I', tmp56)[0]
			
			self.team_nickname = s[offset:offset + tmp57].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp57]
			offset += tmp57
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
			tmp58 = b''
			tmp58 += struct.pack('I', len(self.side_name))
			while len(tmp58) and tmp58[-1] == b'\x00'[0]:
				tmp58 = tmp58[:-1]
			s += struct.pack('B', len(tmp58))
			s += tmp58
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.agent_name
		s += b'\x00' if self.agent_name is None else b'\x01'
		if self.agent_name is not None:
			tmp59 = b''
			tmp59 += struct.pack('I', len(self.agent_name))
			while len(tmp59) and tmp59[-1] == b'\x00'[0]:
				tmp59 = tmp59[:-1]
			s += struct.pack('B', len(tmp59))
			s += tmp59
			
			s += self.agent_name.encode('ISO-8859-1') if PY3 else self.agent_name
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.side_name
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp62 = s[offset:offset + tmp61]
			offset += tmp61
			tmp62 += b'\x00' * (4 - tmp61)
			tmp63 = struct.unpack('I', tmp62)[0]
			
			self.side_name = s[offset:offset + tmp63].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp63]
			offset += tmp63
		else:
			self.side_name = None
		
		# deserialize self.agent_name
		tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp64:
			tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp66 = s[offset:offset + tmp65]
			offset += tmp65
			tmp66 += b'\x00' * (4 - tmp65)
			tmp67 = struct.unpack('I', tmp66)[0]
			
			self.agent_name = s[offset:offset + tmp67].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp67]
			offset += tmp67
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
		tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp68:
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
			tmp69 = b''
			tmp69 += struct.pack('I', len(self.winner_sidename))
			while len(tmp69) and tmp69[-1] == b'\x00'[0]:
				tmp69 = tmp69[:-1]
			s += struct.pack('B', len(tmp69))
			s += tmp69
			
			s += self.winner_sidename.encode('ISO-8859-1') if PY3 else self.winner_sidename
		
		# serialize self.details
		s += b'\x00' if self.details is None else b'\x01'
		if self.details is not None:
			tmp70 = b''
			tmp70 += struct.pack('I', len(self.details))
			while len(tmp70) and tmp70[-1] == b'\x00'[0]:
				tmp70 = tmp70[:-1]
			s += struct.pack('B', len(tmp70))
			s += tmp70
			
			for tmp71 in self.details:
				s += b'\x00' if tmp71 is None else b'\x01'
				if tmp71 is not None:
					tmp72 = b''
					tmp72 += struct.pack('I', len(tmp71))
					while len(tmp72) and tmp72[-1] == b'\x00'[0]:
						tmp72 = tmp72[:-1]
					s += struct.pack('B', len(tmp72))
					s += tmp72
					
					s += tmp71.encode('ISO-8859-1') if PY3 else tmp71
				s += b'\x00' if self.details[tmp71] is None else b'\x01'
				if self.details[tmp71] is not None:
					tmp73 = b''
					tmp73 += struct.pack('I', len(self.details[tmp71]))
					while len(tmp73) and tmp73[-1] == b'\x00'[0]:
						tmp73 = tmp73[:-1]
					s += struct.pack('B', len(tmp73))
					s += tmp73
					
					for tmp74 in self.details[tmp71]:
						s += b'\x00' if tmp74 is None else b'\x01'
						if tmp74 is not None:
							tmp75 = b''
							tmp75 += struct.pack('I', len(tmp74))
							while len(tmp75) and tmp75[-1] == b'\x00'[0]:
								tmp75 = tmp75[:-1]
							s += struct.pack('B', len(tmp75))
							s += tmp75
							
							s += tmp74.encode('ISO-8859-1') if PY3 else tmp74
						s += b'\x00' if self.details[tmp71][tmp74] is None else b'\x01'
						if self.details[tmp71][tmp74] is not None:
							tmp76 = b''
							tmp76 += struct.pack('I', len(self.details[tmp71][tmp74]))
							while len(tmp76) and tmp76[-1] == b'\x00'[0]:
								tmp76 = tmp76[:-1]
							s += struct.pack('B', len(tmp76))
							s += tmp76
							
							s += self.details[tmp71][tmp74].encode('ISO-8859-1') if PY3 else self.details[tmp71][tmp74]
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.winner_sidename
		tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp77:
			tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp79 = s[offset:offset + tmp78]
			offset += tmp78
			tmp79 += b'\x00' * (4 - tmp78)
			tmp80 = struct.unpack('I', tmp79)[0]
			
			self.winner_sidename = s[offset:offset + tmp80].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp80]
			offset += tmp80
		else:
			self.winner_sidename = None
		
		# deserialize self.details
		tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp81:
			tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp83 = s[offset:offset + tmp82]
			offset += tmp82
			tmp83 += b'\x00' * (4 - tmp82)
			tmp84 = struct.unpack('I', tmp83)[0]
			
			self.details = {}
			for tmp85 in range(tmp84):
				tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp88:
					tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp90 = s[offset:offset + tmp89]
					offset += tmp89
					tmp90 += b'\x00' * (4 - tmp89)
					tmp91 = struct.unpack('I', tmp90)[0]
					
					tmp86 = s[offset:offset + tmp91].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp91]
					offset += tmp91
				else:
					tmp86 = None
				tmp92 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp92:
					tmp93 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp94 = s[offset:offset + tmp93]
					offset += tmp93
					tmp94 += b'\x00' * (4 - tmp93)
					tmp95 = struct.unpack('I', tmp94)[0]
					
					tmp87 = {}
					for tmp96 in range(tmp95):
						tmp99 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp99:
							tmp100 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp101 = s[offset:offset + tmp100]
							offset += tmp100
							tmp101 += b'\x00' * (4 - tmp100)
							tmp102 = struct.unpack('I', tmp101)[0]
							
							tmp97 = s[offset:offset + tmp102].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp102]
							offset += tmp102
						else:
							tmp97 = None
						tmp103 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp103:
							tmp104 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp105 = s[offset:offset + tmp104]
							offset += tmp104
							tmp105 += b'\x00' * (4 - tmp104)
							tmp106 = struct.unpack('I', tmp105)[0]
							
							tmp98 = s[offset:offset + tmp106].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp106]
							offset += tmp106
						else:
							tmp98 = None
						tmp87[tmp97] = tmp98
				else:
					tmp87 = None
				self.details[tmp86] = tmp87
		else:
			self.details = None
		
		return offset


class CanvasAction(object):

	@staticmethod
	def name():
		return 'CanvasAction'


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
			tmp107 = b''
			tmp107 += struct.pack('I', len(self.action_types))
			while len(tmp107) and tmp107[-1] == b'\x00'[0]:
				tmp107 = tmp107[:-1]
			s += struct.pack('B', len(tmp107))
			s += tmp107
			
			for tmp108 in self.action_types:
				s += b'\x00' if tmp108 is None else b'\x01'
				if tmp108 is not None:
					tmp109 = b''
					tmp109 += struct.pack('I', len(tmp108))
					while len(tmp109) and tmp109[-1] == b'\x00'[0]:
						tmp109 = tmp109[:-1]
					s += struct.pack('B', len(tmp109))
					s += tmp109
					
					s += tmp108.encode('ISO-8859-1') if PY3 else tmp108
		
		# serialize self.action_payloads
		s += b'\x00' if self.action_payloads is None else b'\x01'
		if self.action_payloads is not None:
			tmp110 = b''
			tmp110 += struct.pack('I', len(self.action_payloads))
			while len(tmp110) and tmp110[-1] == b'\x00'[0]:
				tmp110 = tmp110[:-1]
			s += struct.pack('B', len(tmp110))
			s += tmp110
			
			for tmp111 in self.action_payloads:
				s += b'\x00' if tmp111 is None else b'\x01'
				if tmp111 is not None:
					tmp112 = b''
					tmp112 += struct.pack('I', len(tmp111))
					while len(tmp112) and tmp112[-1] == b'\x00'[0]:
						tmp112 = tmp112[:-1]
					s += struct.pack('B', len(tmp112))
					s += tmp112
					
					s += tmp111.encode('ISO-8859-1') if PY3 else tmp111
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.action_types
		tmp113 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp113:
			tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp115 = s[offset:offset + tmp114]
			offset += tmp114
			tmp115 += b'\x00' * (4 - tmp114)
			tmp116 = struct.unpack('I', tmp115)[0]
			
			self.action_types = []
			for tmp117 in range(tmp116):
				tmp119 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp119:
					tmp120 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp121 = s[offset:offset + tmp120]
					offset += tmp120
					tmp121 += b'\x00' * (4 - tmp120)
					tmp122 = struct.unpack('I', tmp121)[0]
					
					tmp118 = s[offset:offset + tmp122].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp122]
					offset += tmp122
				else:
					tmp118 = None
				self.action_types.append(tmp118)
		else:
			self.action_types = None
		
		# deserialize self.action_payloads
		tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp123:
			tmp124 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp125 = s[offset:offset + tmp124]
			offset += tmp124
			tmp125 += b'\x00' * (4 - tmp124)
			tmp126 = struct.unpack('I', tmp125)[0]
			
			self.action_payloads = []
			for tmp127 in range(tmp126):
				tmp129 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp129:
					tmp130 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp131 = s[offset:offset + tmp130]
					offset += tmp130
					tmp131 += b'\x00' * (4 - tmp130)
					tmp132 = struct.unpack('I', tmp131)[0]
					
					tmp128 = s[offset:offset + tmp132].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp132]
					offset += tmp132
				else:
					tmp128 = None
				self.action_payloads.append(tmp128)
		else:
			self.action_payloads = None
		
		return offset
