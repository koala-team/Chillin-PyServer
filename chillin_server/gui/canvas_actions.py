# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ResizeCanvas(object):

	@staticmethod
	def name():
		return 'ResizeCanvas'


	def __init__(self, width=None, height=None):
		self.initialize(width, height)
	

	def initialize(self, width=None, height=None):
		self.width = width
		self.height = height
	

	def serialize(self):
		s = b''
		
		# serialize self.width
		s += b'\x00' if self.width is None else b'\x01'
		if self.width is not None:
			s += struct.pack('H', self.width)
		
		# serialize self.height
		s += b'\x00' if self.height is None else b'\x01'
		if self.height is not None:
			s += struct.pack('H', self.height)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.width = None
		
		# deserialize self.height
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.height = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.height = None
		
		return offset


class ClearCanvas(object):

	@staticmethod
	def name():
		return 'ClearCanvas'


	def __init__(self):
		self.initialize()
	

	def initialize(self):
		return
	

	def serialize(self):
		s = b''
		
		return s
	

	def deserialize(self, s, offset=0):
		return offset


class CreateElement(object):

	@staticmethod
	def name():
		return 'CreateElement'


	def __init__(self, ref=None, element_type=None, element_payload=None):
		self.initialize(ref, element_type, element_payload)
	

	def initialize(self, ref=None, element_type=None, element_payload=None):
		self.ref = ref
		self.element_type = element_type
		self.element_payload = element_payload
	

	def serialize(self):
		s = b''
		
		# serialize self.ref
		s += b'\x00' if self.ref is None else b'\x01'
		if self.ref is not None:
			s += struct.pack('I', self.ref)
		
		# serialize self.element_type
		s += b'\x00' if self.element_type is None else b'\x01'
		if self.element_type is not None:
			tmp2 = b''
			tmp2 += struct.pack('I', len(self.element_type))
			while len(tmp2) and tmp2[-1] == b'\x00'[0]:
				tmp2 = tmp2[:-1]
			s += struct.pack('B', len(tmp2))
			s += tmp2
			
			s += self.element_type.encode('ISO-8859-1') if PY3 else self.element_type
		
		# serialize self.element_payload
		s += b'\x00' if self.element_payload is None else b'\x01'
		if self.element_payload is not None:
			tmp3 = b''
			tmp3 += struct.pack('I', len(self.element_payload))
			while len(tmp3) and tmp3[-1] == b'\x00'[0]:
				tmp3 = tmp3[:-1]
			s += struct.pack('B', len(tmp3))
			s += tmp3
			
			s += self.element_payload.encode('ISO-8859-1') if PY3 else self.element_payload
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.ref
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.ref = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ref = None
		
		# deserialize self.element_type
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp7 = s[offset:offset + tmp6]
			offset += tmp6
			tmp7 += b'\x00' * (4 - tmp6)
			tmp8 = struct.unpack('I', tmp7)[0]
			
			self.element_type = s[offset:offset + tmp8].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp8]
			offset += tmp8
		else:
			self.element_type = None
		
		# deserialize self.element_payload
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp11 = s[offset:offset + tmp10]
			offset += tmp10
			tmp11 += b'\x00' * (4 - tmp10)
			tmp12 = struct.unpack('I', tmp11)[0]
			
			self.element_payload = s[offset:offset + tmp12].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp12]
			offset += tmp12
		else:
			self.element_payload = None
		
		return offset


class EditElement(object):

	@staticmethod
	def name():
		return 'EditElement'


	def __init__(self, ref=None, element_type=None, element_payload=None):
		self.initialize(ref, element_type, element_payload)
	

	def initialize(self, ref=None, element_type=None, element_payload=None):
		self.ref = ref
		self.element_type = element_type
		self.element_payload = element_payload
	

	def serialize(self):
		s = b''
		
		# serialize self.ref
		s += b'\x00' if self.ref is None else b'\x01'
		if self.ref is not None:
			s += struct.pack('I', self.ref)
		
		# serialize self.element_type
		s += b'\x00' if self.element_type is None else b'\x01'
		if self.element_type is not None:
			tmp13 = b''
			tmp13 += struct.pack('I', len(self.element_type))
			while len(tmp13) and tmp13[-1] == b'\x00'[0]:
				tmp13 = tmp13[:-1]
			s += struct.pack('B', len(tmp13))
			s += tmp13
			
			s += self.element_type.encode('ISO-8859-1') if PY3 else self.element_type
		
		# serialize self.element_payload
		s += b'\x00' if self.element_payload is None else b'\x01'
		if self.element_payload is not None:
			tmp14 = b''
			tmp14 += struct.pack('I', len(self.element_payload))
			while len(tmp14) and tmp14[-1] == b'\x00'[0]:
				tmp14 = tmp14[:-1]
			s += struct.pack('B', len(tmp14))
			s += tmp14
			
			s += self.element_payload.encode('ISO-8859-1') if PY3 else self.element_payload
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.ref
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.ref = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ref = None
		
		# deserialize self.element_type
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			tmp17 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp18 = s[offset:offset + tmp17]
			offset += tmp17
			tmp18 += b'\x00' * (4 - tmp17)
			tmp19 = struct.unpack('I', tmp18)[0]
			
			self.element_type = s[offset:offset + tmp19].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp19]
			offset += tmp19
		else:
			self.element_type = None
		
		# deserialize self.element_payload
		tmp20 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp20:
			tmp21 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp22 = s[offset:offset + tmp21]
			offset += tmp21
			tmp22 += b'\x00' * (4 - tmp21)
			tmp23 = struct.unpack('I', tmp22)[0]
			
			self.element_payload = s[offset:offset + tmp23].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp23]
			offset += tmp23
		else:
			self.element_payload = None
		
		return offset


class DeleteElement(object):

	@staticmethod
	def name():
		return 'DeleteElement'


	def __init__(self, ref=None):
		self.initialize(ref)
	

	def initialize(self, ref=None):
		self.ref = ref
	

	def serialize(self):
		s = b''
		
		# serialize self.ref
		s += b'\x00' if self.ref is None else b'\x01'
		if self.ref is not None:
			s += struct.pack('I', self.ref)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.ref
		tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp24:
			self.ref = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ref = None
		
		return offset


class StoreImageData(object):

	@staticmethod
	def name():
		return 'StoreImageData'


	def __init__(self, image_name=None, image_data=None):
		self.initialize(image_name, image_data)
	

	def initialize(self, image_name=None, image_data=None):
		self.image_name = image_name
		self.image_data = image_data
	

	def serialize(self):
		s = b''
		
		# serialize self.image_name
		s += b'\x00' if self.image_name is None else b'\x01'
		if self.image_name is not None:
			tmp25 = b''
			tmp25 += struct.pack('I', len(self.image_name))
			while len(tmp25) and tmp25[-1] == b'\x00'[0]:
				tmp25 = tmp25[:-1]
			s += struct.pack('B', len(tmp25))
			s += tmp25
			
			s += self.image_name.encode('ISO-8859-1') if PY3 else self.image_name
		
		# serialize self.image_data
		s += b'\x00' if self.image_data is None else b'\x01'
		if self.image_data is not None:
			tmp26 = b''
			tmp26 += struct.pack('I', len(self.image_data))
			while len(tmp26) and tmp26[-1] == b'\x00'[0]:
				tmp26 = tmp26[:-1]
			s += struct.pack('B', len(tmp26))
			s += tmp26
			
			s += self.image_data.encode('ISO-8859-1') if PY3 else self.image_data
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.image_name
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp29 = s[offset:offset + tmp28]
			offset += tmp28
			tmp29 += b'\x00' * (4 - tmp28)
			tmp30 = struct.unpack('I', tmp29)[0]
			
			self.image_name = s[offset:offset + tmp30].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp30]
			offset += tmp30
		else:
			self.image_name = None
		
		# deserialize self.image_data
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp33 = s[offset:offset + tmp32]
			offset += tmp32
			tmp33 += b'\x00' * (4 - tmp32)
			tmp34 = struct.unpack('I', tmp33)[0]
			
			self.image_data = s[offset:offset + tmp34].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp34]
			offset += tmp34
		else:
			self.image_data = None
		
		return offset


class BringToFront(object):

	@staticmethod
	def name():
		return 'BringToFront'


	def __init__(self, ref=None, target_ref=None):
		self.initialize(ref, target_ref)
	

	def initialize(self, ref=None, target_ref=None):
		self.ref = ref
		self.target_ref = target_ref
	

	def serialize(self):
		s = b''
		
		# serialize self.ref
		s += b'\x00' if self.ref is None else b'\x01'
		if self.ref is not None:
			s += struct.pack('I', self.ref)
		
		# serialize self.target_ref
		s += b'\x00' if self.target_ref is None else b'\x01'
		if self.target_ref is not None:
			s += struct.pack('I', self.target_ref)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.ref
		tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp35:
			self.ref = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ref = None
		
		# deserialize self.target_ref
		tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp36:
			self.target_ref = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.target_ref = None
		
		return offset


class SendToBack(object):

	@staticmethod
	def name():
		return 'SendToBack'


	def __init__(self, ref=None, target_ref=None):
		self.initialize(ref, target_ref)
	

	def initialize(self, ref=None, target_ref=None):
		self.ref = ref
		self.target_ref = target_ref
	

	def serialize(self):
		s = b''
		
		# serialize self.ref
		s += b'\x00' if self.ref is None else b'\x01'
		if self.ref is not None:
			s += struct.pack('I', self.ref)
		
		# serialize self.target_ref
		s += b'\x00' if self.target_ref is None else b'\x01'
		if self.target_ref is not None:
			s += struct.pack('I', self.target_ref)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.ref
		tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp37:
			self.ref = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ref = None
		
		# deserialize self.target_ref
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			self.target_ref = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.target_ref = None
		
		return offset
