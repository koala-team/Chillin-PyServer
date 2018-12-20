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


class JoinOfflineGame(object):

	@staticmethod
	def name():
		return 'JoinOfflineGame'


	def __init__(self, team_nickname=None, agent_name=None):
		self.initialize(team_nickname, agent_name)
	

	def initialize(self, team_nickname=None, agent_name=None):
		self.team_nickname = team_nickname
		self.agent_name = agent_name
	

	def serialize(self):
		s = b''
		
		# serialize self.team_nickname
		s += b'\x00' if self.team_nickname is None else b'\x01'
		if self.team_nickname is not None:
			tmp10 = b''
			tmp10 += struct.pack('I', len(self.team_nickname))
			while len(tmp10) and tmp10[-1] == b'\x00'[0]:
				tmp10 = tmp10[:-1]
			s += struct.pack('B', len(tmp10))
			s += tmp10
			
			s += self.team_nickname.encode('ISO-8859-1') if PY3 else self.team_nickname
		
		# serialize self.agent_name
		s += b'\x00' if self.agent_name is None else b'\x01'
		if self.agent_name is not None:
			tmp11 = b''
			tmp11 += struct.pack('I', len(self.agent_name))
			while len(tmp11) and tmp11[-1] == b'\x00'[0]:
				tmp11 = tmp11[:-1]
			s += struct.pack('B', len(tmp11))
			s += tmp11
			
			s += self.agent_name.encode('ISO-8859-1') if PY3 else self.agent_name
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.team_nickname
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp14 = s[offset:offset + tmp13]
			offset += tmp13
			tmp14 += b'\x00' * (4 - tmp13)
			tmp15 = struct.unpack('I', tmp14)[0]
			
			self.team_nickname = s[offset:offset + tmp15].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp15]
			offset += tmp15
		else:
			self.team_nickname = None
		
		# deserialize self.agent_name
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			tmp17 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp18 = s[offset:offset + tmp17]
			offset += tmp17
			tmp18 += b'\x00' * (4 - tmp17)
			tmp19 = struct.unpack('I', tmp18)[0]
			
			self.agent_name = s[offset:offset + tmp19].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp19]
			offset += tmp19
		else:
			self.agent_name = None
		
		return offset


class JoinOnlineGame(object):

	@staticmethod
	def name():
		return 'JoinOnlineGame'


	def __init__(self, token=None, agent_name=None):
		self.initialize(token, agent_name)
	

	def initialize(self, token=None, agent_name=None):
		self.token = token
		self.agent_name = agent_name
	

	def serialize(self):
		s = b''
		
		# serialize self.token
		s += b'\x00' if self.token is None else b'\x01'
		if self.token is not None:
			tmp20 = b''
			tmp20 += struct.pack('I', len(self.token))
			while len(tmp20) and tmp20[-1] == b'\x00'[0]:
				tmp20 = tmp20[:-1]
			s += struct.pack('B', len(tmp20))
			s += tmp20
			
			s += self.token.encode('ISO-8859-1') if PY3 else self.token
		
		# serialize self.agent_name
		s += b'\x00' if self.agent_name is None else b'\x01'
		if self.agent_name is not None:
			tmp21 = b''
			tmp21 += struct.pack('I', len(self.agent_name))
			while len(tmp21) and tmp21[-1] == b'\x00'[0]:
				tmp21 = tmp21[:-1]
			s += struct.pack('B', len(tmp21))
			s += tmp21
			
			s += self.agent_name.encode('ISO-8859-1') if PY3 else self.agent_name
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.token
		tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp22:
			tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp24 = s[offset:offset + tmp23]
			offset += tmp23
			tmp24 += b'\x00' * (4 - tmp23)
			tmp25 = struct.unpack('I', tmp24)[0]
			
			self.token = s[offset:offset + tmp25].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp25]
			offset += tmp25
		else:
			self.token = None
		
		# deserialize self.agent_name
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
			tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp28 = s[offset:offset + tmp27]
			offset += tmp27
			tmp28 += b'\x00' * (4 - tmp27)
			tmp29 = struct.unpack('I', tmp28)[0]
			
			self.agent_name = s[offset:offset + tmp29].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp29]
			offset += tmp29
		else:
			self.agent_name = None
		
		return offset


class ClientJoined(object):

	@staticmethod
	def name():
		return 'ClientJoined'


	def __init__(self, joined=None, side_name=None, sides=None):
		self.initialize(joined, side_name, sides)
	

	def initialize(self, joined=None, side_name=None, sides=None):
		self.joined = joined
		self.side_name = side_name
		self.sides = sides
	

	def serialize(self):
		s = b''
		
		# serialize self.joined
		s += b'\x00' if self.joined is None else b'\x01'
		if self.joined is not None:
			s += struct.pack('?', self.joined)
		
		# serialize self.side_name
		s += b'\x00' if self.side_name is None else b'\x01'
		if self.side_name is not None:
			tmp30 = b''
			tmp30 += struct.pack('I', len(self.side_name))
			while len(tmp30) and tmp30[-1] == b'\x00'[0]:
				tmp30 = tmp30[:-1]
			s += struct.pack('B', len(tmp30))
			s += tmp30
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.sides
		s += b'\x00' if self.sides is None else b'\x01'
		if self.sides is not None:
			tmp31 = b''
			tmp31 += struct.pack('I', len(self.sides))
			while len(tmp31) and tmp31[-1] == b'\x00'[0]:
				tmp31 = tmp31[:-1]
			s += struct.pack('B', len(tmp31))
			s += tmp31
			
			for tmp32 in self.sides:
				s += b'\x00' if tmp32 is None else b'\x01'
				if tmp32 is not None:
					tmp33 = b''
					tmp33 += struct.pack('I', len(tmp32))
					while len(tmp33) and tmp33[-1] == b'\x00'[0]:
						tmp33 = tmp33[:-1]
					s += struct.pack('B', len(tmp33))
					s += tmp33
					
					s += tmp32.encode('ISO-8859-1') if PY3 else tmp32
				s += b'\x00' if self.sides[tmp32] is None else b'\x01'
				if self.sides[tmp32] is not None:
					tmp34 = b''
					tmp34 += struct.pack('I', len(self.sides[tmp32]))
					while len(tmp34) and tmp34[-1] == b'\x00'[0]:
						tmp34 = tmp34[:-1]
					s += struct.pack('B', len(tmp34))
					s += tmp34
					
					for tmp35 in self.sides[tmp32]:
						s += b'\x00' if tmp35 is None else b'\x01'
						if tmp35 is not None:
							tmp36 = b''
							tmp36 += struct.pack('I', len(tmp35))
							while len(tmp36) and tmp36[-1] == b'\x00'[0]:
								tmp36 = tmp36[:-1]
							s += struct.pack('B', len(tmp36))
							s += tmp36
							
							s += tmp35.encode('ISO-8859-1') if PY3 else tmp35
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.joined
		tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp37:
			self.joined = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.joined = None
		
		# deserialize self.side_name
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp40 = s[offset:offset + tmp39]
			offset += tmp39
			tmp40 += b'\x00' * (4 - tmp39)
			tmp41 = struct.unpack('I', tmp40)[0]
			
			self.side_name = s[offset:offset + tmp41].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp41]
			offset += tmp41
		else:
			self.side_name = None
		
		# deserialize self.sides
		tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp42:
			tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp44 = s[offset:offset + tmp43]
			offset += tmp43
			tmp44 += b'\x00' * (4 - tmp43)
			tmp45 = struct.unpack('I', tmp44)[0]
			
			self.sides = {}
			for tmp46 in range(tmp45):
				tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp49:
					tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp51 = s[offset:offset + tmp50]
					offset += tmp50
					tmp51 += b'\x00' * (4 - tmp50)
					tmp52 = struct.unpack('I', tmp51)[0]
					
					tmp47 = s[offset:offset + tmp52].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp52]
					offset += tmp52
				else:
					tmp47 = None
				tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp53:
					tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp55 = s[offset:offset + tmp54]
					offset += tmp54
					tmp55 += b'\x00' * (4 - tmp54)
					tmp56 = struct.unpack('I', tmp55)[0]
					
					tmp48 = []
					for tmp57 in range(tmp56):
						tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp59:
							tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp61 = s[offset:offset + tmp60]
							offset += tmp60
							tmp61 += b'\x00' * (4 - tmp60)
							tmp62 = struct.unpack('I', tmp61)[0]
							
							tmp58 = s[offset:offset + tmp62].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp62]
							offset += tmp62
						else:
							tmp58 = None
						tmp48.append(tmp58)
				else:
					tmp48 = None
				self.sides[tmp47] = tmp48
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


class BaseSnapshot(object):

	@staticmethod
	def name():
		return 'BaseSnapshot'


	def __init__(self, world_payload=None):
		self.initialize(world_payload)
	

	def initialize(self, world_payload=None):
		self.world_payload = world_payload
	

	def serialize(self):
		s = b''
		
		# serialize self.world_payload
		s += b'\x00' if self.world_payload is None else b'\x01'
		if self.world_payload is not None:
			tmp127 = b''
			tmp127 += struct.pack('I', len(self.world_payload))
			while len(tmp127) and tmp127[-1] == b'\x00'[0]:
				tmp127 = tmp127[:-1]
			s += struct.pack('B', len(tmp127))
			s += tmp127
			
			s += self.world_payload.encode('ISO-8859-1') if PY3 else self.world_payload
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.world_payload
		tmp128 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp128:
			tmp129 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp130 = s[offset:offset + tmp129]
			offset += tmp129
			tmp130 += b'\x00' * (4 - tmp129)
			tmp131 = struct.unpack('I', tmp130)[0]
			
			self.world_payload = s[offset:offset + tmp131].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp131]
			offset += tmp131
		else:
			self.world_payload = None
		
		return offset


class RealtimeSnapshot(BaseSnapshot):

	@staticmethod
	def name():
		return 'RealtimeSnapshot'


	def __init__(self, world_payload=None, current_cycle=None, cycle_duration=None):
		self.initialize(world_payload, current_cycle, cycle_duration)
	

	def initialize(self, world_payload=None, current_cycle=None, cycle_duration=None):
		BaseSnapshot.initialize(self, world_payload)
		
		self.current_cycle = current_cycle
		self.cycle_duration = cycle_duration
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseSnapshot.serialize(self)
		
		# serialize self.current_cycle
		s += b'\x00' if self.current_cycle is None else b'\x01'
		if self.current_cycle is not None:
			s += struct.pack('I', self.current_cycle)
		
		# serialize self.cycle_duration
		s += b'\x00' if self.cycle_duration is None else b'\x01'
		if self.cycle_duration is not None:
			s += struct.pack('f', self.cycle_duration)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseSnapshot.deserialize(self, s, offset)
		
		# deserialize self.current_cycle
		tmp132 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp132:
			self.current_cycle = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.current_cycle = None
		
		# deserialize self.cycle_duration
		tmp133 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp133:
			self.cycle_duration = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.cycle_duration = None
		
		return offset


class TurnbasedSnapshot(RealtimeSnapshot):

	@staticmethod
	def name():
		return 'TurnbasedSnapshot'


	def __init__(self, world_payload=None, current_cycle=None, cycle_duration=None, turn_allowed_sides=None):
		self.initialize(world_payload, current_cycle, cycle_duration, turn_allowed_sides)
	

	def initialize(self, world_payload=None, current_cycle=None, cycle_duration=None, turn_allowed_sides=None):
		RealtimeSnapshot.initialize(self, world_payload, current_cycle, cycle_duration)
		
		self.turn_allowed_sides = turn_allowed_sides
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += RealtimeSnapshot.serialize(self)
		
		# serialize self.turn_allowed_sides
		s += b'\x00' if self.turn_allowed_sides is None else b'\x01'
		if self.turn_allowed_sides is not None:
			tmp134 = b''
			tmp134 += struct.pack('I', len(self.turn_allowed_sides))
			while len(tmp134) and tmp134[-1] == b'\x00'[0]:
				tmp134 = tmp134[:-1]
			s += struct.pack('B', len(tmp134))
			s += tmp134
			
			for tmp135 in self.turn_allowed_sides:
				s += b'\x00' if tmp135 is None else b'\x01'
				if tmp135 is not None:
					tmp136 = b''
					tmp136 += struct.pack('I', len(tmp135))
					while len(tmp136) and tmp136[-1] == b'\x00'[0]:
						tmp136 = tmp136[:-1]
					s += struct.pack('B', len(tmp136))
					s += tmp136
					
					s += tmp135.encode('ISO-8859-1') if PY3 else tmp135
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = RealtimeSnapshot.deserialize(self, s, offset)
		
		# deserialize self.turn_allowed_sides
		tmp137 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp137:
			tmp138 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp139 = s[offset:offset + tmp138]
			offset += tmp138
			tmp139 += b'\x00' * (4 - tmp138)
			tmp140 = struct.unpack('I', tmp139)[0]
			
			self.turn_allowed_sides = []
			for tmp141 in range(tmp140):
				tmp143 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp143:
					tmp144 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp145 = s[offset:offset + tmp144]
					offset += tmp144
					tmp145 += b'\x00' * (4 - tmp144)
					tmp146 = struct.unpack('I', tmp145)[0]
					
					tmp142 = s[offset:offset + tmp146].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp146]
					offset += tmp146
				else:
					tmp142 = None
				self.turn_allowed_sides.append(tmp142)
		else:
			self.turn_allowed_sides = None
		
		return offset


class BaseCommand(object):

	@staticmethod
	def name():
		return 'BaseCommand'


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
			tmp147 = b''
			tmp147 += struct.pack('I', len(self.type))
			while len(tmp147) and tmp147[-1] == b'\x00'[0]:
				tmp147 = tmp147[:-1]
			s += struct.pack('B', len(tmp147))
			s += tmp147
			
			s += self.type.encode('ISO-8859-1') if PY3 else self.type
		
		# serialize self.payload
		s += b'\x00' if self.payload is None else b'\x01'
		if self.payload is not None:
			tmp148 = b''
			tmp148 += struct.pack('I', len(self.payload))
			while len(tmp148) and tmp148[-1] == b'\x00'[0]:
				tmp148 = tmp148[:-1]
			s += struct.pack('B', len(tmp148))
			s += tmp148
			
			s += self.payload.encode('ISO-8859-1') if PY3 else self.payload
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.type
		tmp149 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp149:
			tmp150 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp151 = s[offset:offset + tmp150]
			offset += tmp150
			tmp151 += b'\x00' * (4 - tmp150)
			tmp152 = struct.unpack('I', tmp151)[0]
			
			self.type = s[offset:offset + tmp152].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp152]
			offset += tmp152
		else:
			self.type = None
		
		# deserialize self.payload
		tmp153 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp153:
			tmp154 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp155 = s[offset:offset + tmp154]
			offset += tmp154
			tmp155 += b'\x00' * (4 - tmp154)
			tmp156 = struct.unpack('I', tmp155)[0]
			
			self.payload = s[offset:offset + tmp156].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp156]
			offset += tmp156
		else:
			self.payload = None
		
		return offset


class RealtimeCommand(BaseCommand):

	@staticmethod
	def name():
		return 'RealtimeCommand'


	def __init__(self, type=None, payload=None, cycle=None):
		self.initialize(type, payload, cycle)
	

	def initialize(self, type=None, payload=None, cycle=None):
		BaseCommand.initialize(self, type, payload)
		
		self.cycle = cycle
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCommand.serialize(self)
		
		# serialize self.cycle
		s += b'\x00' if self.cycle is None else b'\x01'
		if self.cycle is not None:
			s += struct.pack('I', self.cycle)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCommand.deserialize(self, s, offset)
		
		# deserialize self.cycle
		tmp157 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp157:
			self.cycle = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.cycle = None
		
		return offset


class TurnbasedCommand(RealtimeCommand):

	@staticmethod
	def name():
		return 'TurnbasedCommand'


	def __init__(self, type=None, payload=None, cycle=None):
		self.initialize(type, payload, cycle)
	

	def initialize(self, type=None, payload=None, cycle=None):
		RealtimeCommand.initialize(self, type, payload, cycle)
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += RealtimeCommand.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = RealtimeCommand.deserialize(self, s, offset)
		
		return offset
