# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class BaseAction(object):

	@staticmethod
	def name():
		return 'BaseAction'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		self.initialize(cycle, ref, child_ref, duration_cycles)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		self.cycle = cycle
		self.ref = ref
		self.child_ref = child_ref
		self.duration_cycles = duration_cycles
	

	def serialize(self):
		s = b''
		
		# serialize self.cycle
		s += b'\x00' if self.cycle is None else b'\x01'
		if self.cycle is not None:
			s += struct.pack('f', self.cycle)
		
		# serialize self.ref
		s += b'\x00' if self.ref is None else b'\x01'
		if self.ref is not None:
			s += struct.pack('i', self.ref)
		
		# serialize self.child_ref
		s += b'\x00' if self.child_ref is None else b'\x01'
		if self.child_ref is not None:
			tmp0 = b''
			tmp0 += struct.pack('I', len(self.child_ref))
			while len(tmp0) and tmp0[-1] == b'\x00'[0]:
				tmp0 = tmp0[:-1]
			s += struct.pack('B', len(tmp0))
			s += tmp0
			
			s += self.child_ref.encode('ISO-8859-1') if PY3 else self.child_ref
		
		# serialize self.duration_cycles
		s += b'\x00' if self.duration_cycles is None else b'\x01'
		if self.duration_cycles is not None:
			s += struct.pack('f', self.duration_cycles)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.cycle
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.cycle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.cycle = None
		
		# deserialize self.ref
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.ref = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ref = None
		
		# deserialize self.child_ref
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp5 = s[offset:offset + tmp4]
			offset += tmp4
			tmp5 += b'\x00' * (4 - tmp4)
			tmp6 = struct.unpack('I', tmp5)[0]
			
			self.child_ref = s[offset:offset + tmp6].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp6]
			offset += tmp6
		else:
			self.child_ref = None
		
		# deserialize self.duration_cycles
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.duration_cycles = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.duration_cycles = None
		
		return offset


class Vector2(object):

	@staticmethod
	def name():
		return 'Vector2'


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
			s += struct.pack('f', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('f', self.y)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.x = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			self.y = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		return offset


class Vector3(object):

	@staticmethod
	def name():
		return 'Vector3'


	def __init__(self, x=None, y=None, z=None):
		self.initialize(x, y, z)
	

	def initialize(self, x=None, y=None, z=None):
		self.x = x
		self.y = y
		self.z = z
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('f', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('f', self.y)
		
		# serialize self.z
		s += b'\x00' if self.z is None else b'\x01'
		if self.z is not None:
			s += struct.pack('f', self.z)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.x = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.y = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.z
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			self.z = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.z = None
		
		return offset


class Vector4(object):

	@staticmethod
	def name():
		return 'Vector4'


	def __init__(self, x=None, y=None, z=None, w=None):
		self.initialize(x, y, z, w)
	

	def initialize(self, x=None, y=None, z=None, w=None):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('f', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('f', self.y)
		
		# serialize self.z
		s += b'\x00' if self.z is None else b'\x01'
		if self.z is not None:
			s += struct.pack('f', self.z)
		
		# serialize self.w
		s += b'\x00' if self.w is None else b'\x01'
		if self.w is not None:
			s += struct.pack('f', self.w)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.x = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.y = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.z
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.z = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.z = None
		
		# deserialize self.w
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			self.w = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.w = None
		
		return offset


class Asset(object):

	@staticmethod
	def name():
		return 'Asset'


	def __init__(self, bundle_name=None, asset_name=None, index=None):
		self.initialize(bundle_name, asset_name, index)
	

	def initialize(self, bundle_name=None, asset_name=None, index=None):
		self.bundle_name = bundle_name
		self.asset_name = asset_name
		self.index = index
	

	def serialize(self):
		s = b''
		
		# serialize self.bundle_name
		s += b'\x00' if self.bundle_name is None else b'\x01'
		if self.bundle_name is not None:
			tmp17 = b''
			tmp17 += struct.pack('I', len(self.bundle_name))
			while len(tmp17) and tmp17[-1] == b'\x00'[0]:
				tmp17 = tmp17[:-1]
			s += struct.pack('B', len(tmp17))
			s += tmp17
			
			s += self.bundle_name.encode('ISO-8859-1') if PY3 else self.bundle_name
		
		# serialize self.asset_name
		s += b'\x00' if self.asset_name is None else b'\x01'
		if self.asset_name is not None:
			tmp18 = b''
			tmp18 += struct.pack('I', len(self.asset_name))
			while len(tmp18) and tmp18[-1] == b'\x00'[0]:
				tmp18 = tmp18[:-1]
			s += struct.pack('B', len(tmp18))
			s += tmp18
			
			s += self.asset_name.encode('ISO-8859-1') if PY3 else self.asset_name
		
		# serialize self.index
		s += b'\x00' if self.index is None else b'\x01'
		if self.index is not None:
			s += struct.pack('i', self.index)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.bundle_name
		tmp19 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp19:
			tmp20 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp21 = s[offset:offset + tmp20]
			offset += tmp20
			tmp21 += b'\x00' * (4 - tmp20)
			tmp22 = struct.unpack('I', tmp21)[0]
			
			self.bundle_name = s[offset:offset + tmp22].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp22]
			offset += tmp22
		else:
			self.bundle_name = None
		
		# deserialize self.asset_name
		tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp23:
			tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp25 = s[offset:offset + tmp24]
			offset += tmp24
			tmp25 += b'\x00' * (4 - tmp24)
			tmp26 = struct.unpack('I', tmp25)[0]
			
			self.asset_name = s[offset:offset + tmp26].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp26]
			offset += tmp26
		else:
			self.asset_name = None
		
		# deserialize self.index
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.index = None
		
		return offset


class LayerMask(object):

	@staticmethod
	def name():
		return 'LayerMask'


	def __init__(self, masks_int=None, masks_string=None):
		self.initialize(masks_int, masks_string)
	

	def initialize(self, masks_int=None, masks_string=None):
		self.masks_int = masks_int
		self.masks_string = masks_string
	

	def serialize(self):
		s = b''
		
		# serialize self.masks_int
		s += b'\x00' if self.masks_int is None else b'\x01'
		if self.masks_int is not None:
			s += struct.pack('i', self.masks_int)
		
		# serialize self.masks_string
		s += b'\x00' if self.masks_string is None else b'\x01'
		if self.masks_string is not None:
			tmp28 = b''
			tmp28 += struct.pack('I', len(self.masks_string))
			while len(tmp28) and tmp28[-1] == b'\x00'[0]:
				tmp28 = tmp28[:-1]
			s += struct.pack('B', len(tmp28))
			s += tmp28
			
			for tmp29 in self.masks_string:
				s += b'\x00' if tmp29 is None else b'\x01'
				if tmp29 is not None:
					tmp30 = b''
					tmp30 += struct.pack('I', len(tmp29))
					while len(tmp30) and tmp30[-1] == b'\x00'[0]:
						tmp30 = tmp30[:-1]
					s += struct.pack('B', len(tmp30))
					s += tmp30
					
					s += tmp29.encode('ISO-8859-1') if PY3 else tmp29
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.masks_int
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			self.masks_int = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.masks_int = None
		
		# deserialize self.masks_string
		tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp32:
			tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp34 = s[offset:offset + tmp33]
			offset += tmp33
			tmp34 += b'\x00' * (4 - tmp33)
			tmp35 = struct.unpack('I', tmp34)[0]
			
			self.masks_string = []
			for tmp36 in range(tmp35):
				tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp38:
					tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp40 = s[offset:offset + tmp39]
					offset += tmp39
					tmp40 += b'\x00' * (4 - tmp39)
					tmp41 = struct.unpack('I', tmp40)[0]
					
					tmp37 = s[offset:offset + tmp41].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp41]
					offset += tmp41
				else:
					tmp37 = None
				self.masks_string.append(tmp37)
		else:
			self.masks_string = None
		
		return offset


class BaseCreation(BaseAction):

	@staticmethod
	def name():
		return 'BaseCreation'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.parent_ref = parent_ref
		self.parent_child_ref = parent_child_ref
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.parent_ref
		s += b'\x00' if self.parent_ref is None else b'\x01'
		if self.parent_ref is not None:
			s += struct.pack('i', self.parent_ref)
		
		# serialize self.parent_child_ref
		s += b'\x00' if self.parent_child_ref is None else b'\x01'
		if self.parent_child_ref is not None:
			tmp42 = b''
			tmp42 += struct.pack('I', len(self.parent_child_ref))
			while len(tmp42) and tmp42[-1] == b'\x00'[0]:
				tmp42 = tmp42[:-1]
			s += struct.pack('B', len(tmp42))
			s += tmp42
			
			s += self.parent_child_ref.encode('ISO-8859-1') if PY3 else self.parent_child_ref
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.parent_ref
		tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp43:
			self.parent_ref = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.parent_ref = None
		
		# deserialize self.parent_child_ref
		tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp44:
			tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp46 = s[offset:offset + tmp45]
			offset += tmp45
			tmp46 += b'\x00' * (4 - tmp45)
			tmp47 = struct.unpack('I', tmp46)[0]
			
			self.parent_child_ref = s[offset:offset + tmp47].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp47]
			offset += tmp47
		else:
			self.parent_child_ref = None
		
		return offset


class CreateEmptyGameObject(BaseCreation):

	@staticmethod
	def name():
		return 'CreateEmptyGameObject'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None):
		BaseCreation.initialize(self, cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCreation.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCreation.deserialize(self, s, offset)
		
		return offset


class EDefaultParent(Enum):
	RootObject = 0
	RootCanvas = 1


class InstantiateBundleAsset(BaseCreation):

	@staticmethod
	def name():
		return 'InstantiateBundleAsset'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, asset=None, default_parent=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref, asset, default_parent)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, asset=None, default_parent=None):
		BaseCreation.initialize(self, cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
		
		self.asset = asset
		self.default_parent = default_parent
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCreation.serialize(self)
		
		# serialize self.asset
		s += b'\x00' if self.asset is None else b'\x01'
		if self.asset is not None:
			s += self.asset.serialize()
		
		# serialize self.default_parent
		s += b'\x00' if self.default_parent is None else b'\x01'
		if self.default_parent is not None:
			s += struct.pack('b', self.default_parent.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCreation.deserialize(self, s, offset)
		
		# deserialize self.asset
		tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp48:
			self.asset = Asset()
			offset = self.asset.deserialize(s, offset)
		else:
			self.asset = None
		
		# deserialize self.default_parent
		tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp49:
			tmp50 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.default_parent = EDefaultParent(tmp50)
		else:
			self.default_parent = None
		
		return offset


class EBasicObjectType(Enum):
	Sprite = 0
	AudioSource = 1
	Ellipse2D = 2
	Polygon2D = 3
	Line = 4
	Light = 5


class CreateBasicObject(BaseCreation):

	@staticmethod
	def name():
		return 'CreateBasicObject'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, type=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref, type)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, type=None):
		BaseCreation.initialize(self, cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
		
		self.type = type
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCreation.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCreation.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			tmp52 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EBasicObjectType(tmp52)
		else:
			self.type = None
		
		return offset


class EUIElementType(Enum):
	Canvas = 0
	Text = 1
	Slider = 2
	Image = 3
	RawImage = 4
	Panel = 5


class CreateUIElement(BaseCreation):

	@staticmethod
	def name():
		return 'CreateUIElement'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, type=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref, type)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, type=None):
		BaseCreation.initialize(self, cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
		
		self.type = type
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCreation.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCreation.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			tmp54 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EUIElementType(tmp54)
		else:
			self.type = None
		
		return offset


class Destroy(BaseAction):

	@staticmethod
	def name():
		return 'Destroy'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		self.initialize(cycle, ref, child_ref, duration_cycles)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		return offset


class ChangeIsActive(BaseAction):

	@staticmethod
	def name():
		return 'ChangeIsActive'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, is_active=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, is_active)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, is_active=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.is_active = is_active
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.is_active
		s += b'\x00' if self.is_active is None else b'\x01'
		if self.is_active is not None:
			s += struct.pack('?', self.is_active)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.is_active
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			self.is_active = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_active = None
		
		return offset


class ChangeVisibility(BaseAction):

	@staticmethod
	def name():
		return 'ChangeVisibility'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, is_visible=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, is_visible)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, is_visible=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.is_visible = is_visible
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.is_visible
		s += b'\x00' if self.is_visible is None else b'\x01'
		if self.is_visible is not None:
			s += struct.pack('?', self.is_visible)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.is_visible
		tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp56:
			self.is_visible = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_visible = None
		
		return offset


class ChangeTransform(BaseAction):

	@staticmethod
	def name():
		return 'ChangeTransform'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, position=None, rotation=None, scale=None, change_local=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, position, rotation, scale, change_local)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, position=None, rotation=None, scale=None, change_local=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.position = position
		self.rotation = rotation
		self.scale = scale
		self.change_local = change_local
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.rotation
		s += b'\x00' if self.rotation is None else b'\x01'
		if self.rotation is not None:
			s += self.rotation.serialize()
		
		# serialize self.scale
		s += b'\x00' if self.scale is None else b'\x01'
		if self.scale is not None:
			s += self.scale.serialize()
		
		# serialize self.change_local
		s += b'\x00' if self.change_local is None else b'\x01'
		if self.change_local is not None:
			s += struct.pack('?', self.change_local)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.position
		tmp57 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp57:
			self.position = Vector3()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.rotation
		tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp58:
			self.rotation = Vector3()
			offset = self.rotation.deserialize(s, offset)
		else:
			self.rotation = None
		
		# deserialize self.scale
		tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp59:
			self.scale = Vector3()
			offset = self.scale.deserialize(s, offset)
		else:
			self.scale = None
		
		# deserialize self.change_local
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			self.change_local = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.change_local = None
		
		return offset


class EAnimatorVariableType(Enum):
	Int = 0
	Float = 1
	Bool = 2
	Trigger = 3


class ChangeAnimatorVariable(BaseAction):

	@staticmethod
	def name():
		return 'ChangeAnimatorVariable'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, var_name=None, var_type=None, int_value=None, float_value=None, bool_value=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, var_name, var_type, int_value, float_value, bool_value)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, var_name=None, var_type=None, int_value=None, float_value=None, bool_value=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.var_name = var_name
		self.var_type = var_type
		self.int_value = int_value
		self.float_value = float_value
		self.bool_value = bool_value
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.var_name
		s += b'\x00' if self.var_name is None else b'\x01'
		if self.var_name is not None:
			tmp61 = b''
			tmp61 += struct.pack('I', len(self.var_name))
			while len(tmp61) and tmp61[-1] == b'\x00'[0]:
				tmp61 = tmp61[:-1]
			s += struct.pack('B', len(tmp61))
			s += tmp61
			
			s += self.var_name.encode('ISO-8859-1') if PY3 else self.var_name
		
		# serialize self.var_type
		s += b'\x00' if self.var_type is None else b'\x01'
		if self.var_type is not None:
			s += struct.pack('b', self.var_type.value)
		
		# serialize self.int_value
		s += b'\x00' if self.int_value is None else b'\x01'
		if self.int_value is not None:
			s += struct.pack('i', self.int_value)
		
		# serialize self.float_value
		s += b'\x00' if self.float_value is None else b'\x01'
		if self.float_value is not None:
			s += struct.pack('f', self.float_value)
		
		# serialize self.bool_value
		s += b'\x00' if self.bool_value is None else b'\x01'
		if self.bool_value is not None:
			s += struct.pack('?', self.bool_value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.var_name
		tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp62:
			tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp64 = s[offset:offset + tmp63]
			offset += tmp63
			tmp64 += b'\x00' * (4 - tmp63)
			tmp65 = struct.unpack('I', tmp64)[0]
			
			self.var_name = s[offset:offset + tmp65].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp65]
			offset += tmp65
		else:
			self.var_name = None
		
		# deserialize self.var_type
		tmp66 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp66:
			tmp67 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.var_type = EAnimatorVariableType(tmp67)
		else:
			self.var_type = None
		
		# deserialize self.int_value
		tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp68:
			self.int_value = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.int_value = None
		
		# deserialize self.float_value
		tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp69:
			self.float_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.float_value = None
		
		# deserialize self.bool_value
		tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp70:
			self.bool_value = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.bool_value = None
		
		return offset


class ChangeAnimatorState(BaseAction):

	@staticmethod
	def name():
		return 'ChangeAnimatorState'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, state_name=None, layer=None, normalized_time=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, state_name, layer, normalized_time)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, state_name=None, layer=None, normalized_time=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.state_name = state_name
		self.layer = layer
		self.normalized_time = normalized_time
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.state_name
		s += b'\x00' if self.state_name is None else b'\x01'
		if self.state_name is not None:
			tmp71 = b''
			tmp71 += struct.pack('I', len(self.state_name))
			while len(tmp71) and tmp71[-1] == b'\x00'[0]:
				tmp71 = tmp71[:-1]
			s += struct.pack('B', len(tmp71))
			s += tmp71
			
			s += self.state_name.encode('ISO-8859-1') if PY3 else self.state_name
		
		# serialize self.layer
		s += b'\x00' if self.layer is None else b'\x01'
		if self.layer is not None:
			s += struct.pack('i', self.layer)
		
		# serialize self.normalized_time
		s += b'\x00' if self.normalized_time is None else b'\x01'
		if self.normalized_time is not None:
			s += struct.pack('f', self.normalized_time)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.state_name
		tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp72:
			tmp73 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp74 = s[offset:offset + tmp73]
			offset += tmp73
			tmp74 += b'\x00' * (4 - tmp73)
			tmp75 = struct.unpack('I', tmp74)[0]
			
			self.state_name = s[offset:offset + tmp75].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp75]
			offset += tmp75
		else:
			self.state_name = None
		
		# deserialize self.layer
		tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp76:
			self.layer = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.layer = None
		
		# deserialize self.normalized_time
		tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp77:
			self.normalized_time = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.normalized_time = None
		
		return offset


class ChangeAudioSource(BaseAction):

	@staticmethod
	def name():
		return 'ChangeAudioSource'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, audio_clip_asset=None, time=None, mute=None, loop=None, priority=None, volume=None, spatial_blend=None, play=None, stop=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, audio_clip_asset, time, mute, loop, priority, volume, spatial_blend, play, stop)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, audio_clip_asset=None, time=None, mute=None, loop=None, priority=None, volume=None, spatial_blend=None, play=None, stop=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.audio_clip_asset = audio_clip_asset
		self.time = time
		self.mute = mute
		self.loop = loop
		self.priority = priority
		self.volume = volume
		self.spatial_blend = spatial_blend
		self.play = play
		self.stop = stop
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.audio_clip_asset
		s += b'\x00' if self.audio_clip_asset is None else b'\x01'
		if self.audio_clip_asset is not None:
			s += self.audio_clip_asset.serialize()
		
		# serialize self.time
		s += b'\x00' if self.time is None else b'\x01'
		if self.time is not None:
			s += struct.pack('f', self.time)
		
		# serialize self.mute
		s += b'\x00' if self.mute is None else b'\x01'
		if self.mute is not None:
			s += struct.pack('?', self.mute)
		
		# serialize self.loop
		s += b'\x00' if self.loop is None else b'\x01'
		if self.loop is not None:
			s += struct.pack('?', self.loop)
		
		# serialize self.priority
		s += b'\x00' if self.priority is None else b'\x01'
		if self.priority is not None:
			s += struct.pack('i', self.priority)
		
		# serialize self.volume
		s += b'\x00' if self.volume is None else b'\x01'
		if self.volume is not None:
			s += struct.pack('f', self.volume)
		
		# serialize self.spatial_blend
		s += b'\x00' if self.spatial_blend is None else b'\x01'
		if self.spatial_blend is not None:
			s += struct.pack('f', self.spatial_blend)
		
		# serialize self.play
		s += b'\x00' if self.play is None else b'\x01'
		if self.play is not None:
			s += struct.pack('?', self.play)
		
		# serialize self.stop
		s += b'\x00' if self.stop is None else b'\x01'
		if self.stop is not None:
			s += struct.pack('?', self.stop)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.audio_clip_asset
		tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp78:
			self.audio_clip_asset = Asset()
			offset = self.audio_clip_asset.deserialize(s, offset)
		else:
			self.audio_clip_asset = None
		
		# deserialize self.time
		tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp79:
			self.time = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.time = None
		
		# deserialize self.mute
		tmp80 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp80:
			self.mute = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.mute = None
		
		# deserialize self.loop
		tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp81:
			self.loop = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.loop = None
		
		# deserialize self.priority
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			self.priority = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.priority = None
		
		# deserialize self.volume
		tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp83:
			self.volume = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.volume = None
		
		# deserialize self.spatial_blend
		tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp84:
			self.spatial_blend = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.spatial_blend = None
		
		# deserialize self.play
		tmp85 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp85:
			self.play = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.play = None
		
		# deserialize self.stop
		tmp86 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp86:
			self.stop = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.stop = None
		
		return offset


class ChangeRectTransform(BaseAction):

	@staticmethod
	def name():
		return 'ChangeRectTransform'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, position=None, rotation=None, scale=None, pivot=None, anchor_min=None, anchor_max=None, size=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, position, rotation, scale, pivot, anchor_min, anchor_max, size)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, position=None, rotation=None, scale=None, pivot=None, anchor_min=None, anchor_max=None, size=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.position = position
		self.rotation = rotation
		self.scale = scale
		self.pivot = pivot
		self.anchor_min = anchor_min
		self.anchor_max = anchor_max
		self.size = size
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.rotation
		s += b'\x00' if self.rotation is None else b'\x01'
		if self.rotation is not None:
			s += self.rotation.serialize()
		
		# serialize self.scale
		s += b'\x00' if self.scale is None else b'\x01'
		if self.scale is not None:
			s += self.scale.serialize()
		
		# serialize self.pivot
		s += b'\x00' if self.pivot is None else b'\x01'
		if self.pivot is not None:
			s += self.pivot.serialize()
		
		# serialize self.anchor_min
		s += b'\x00' if self.anchor_min is None else b'\x01'
		if self.anchor_min is not None:
			s += self.anchor_min.serialize()
		
		# serialize self.anchor_max
		s += b'\x00' if self.anchor_max is None else b'\x01'
		if self.anchor_max is not None:
			s += self.anchor_max.serialize()
		
		# serialize self.size
		s += b'\x00' if self.size is None else b'\x01'
		if self.size is not None:
			s += self.size.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.position
		tmp87 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp87:
			self.position = Vector3()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.rotation
		tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp88:
			self.rotation = Vector3()
			offset = self.rotation.deserialize(s, offset)
		else:
			self.rotation = None
		
		# deserialize self.scale
		tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp89:
			self.scale = Vector3()
			offset = self.scale.deserialize(s, offset)
		else:
			self.scale = None
		
		# deserialize self.pivot
		tmp90 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp90:
			self.pivot = Vector2()
			offset = self.pivot.deserialize(s, offset)
		else:
			self.pivot = None
		
		# deserialize self.anchor_min
		tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp91:
			self.anchor_min = Vector2()
			offset = self.anchor_min.deserialize(s, offset)
		else:
			self.anchor_min = None
		
		# deserialize self.anchor_max
		tmp92 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp92:
			self.anchor_max = Vector2()
			offset = self.anchor_max.deserialize(s, offset)
		else:
			self.anchor_max = None
		
		# deserialize self.size
		tmp93 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp93:
			self.size = Vector2()
			offset = self.size.deserialize(s, offset)
		else:
			self.size = None
		
		return offset


class ETextAlignmentOption(Enum):
	TopLeft = 257
	Top = 258
	TopRight = 260
	TopJustified = 264
	TopFlush = 272
	TopGeoAligned = 288
	Left = 513
	Center = 514
	Right = 516
	Justified = 520
	Flush = 528
	CenterGeoAligned = 544
	BottomLeft = 1025
	Bottom = 1026
	BottomRight = 1028
	BottomJustified = 1032
	BottomFlush = 1040
	BottomGeoAligned = 1056
	BaselineLeft = 2049
	Baseline = 2050
	BaselineRight = 2052
	BaselineJustified = 2056
	BaselineFlush = 2064
	BaselineGeoAligned = 2080
	MidlineLeft = 4097
	Midline = 4098
	MidlineRight = 4100
	MidlineJustified = 4104
	MidlineFlush = 4112
	MidlineGeoAligned = 4128
	CaplineLeft = 8193
	Capline = 8194
	CaplineRight = 8196
	CaplineJustified = 8200
	CaplineFlush = 8208
	CaplineGeoAligned = 8224


class ChangeText(BaseAction):

	@staticmethod
	def name():
		return 'ChangeText'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, font_asset=None, font_name=None, text=None, font_size=None, alignment=None, word_wrapping_ratios=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, font_asset, font_name, text, font_size, alignment, word_wrapping_ratios)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, font_asset=None, font_name=None, text=None, font_size=None, alignment=None, word_wrapping_ratios=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.font_asset = font_asset
		self.font_name = font_name
		self.text = text
		self.font_size = font_size
		self.alignment = alignment
		self.word_wrapping_ratios = word_wrapping_ratios
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.font_asset
		s += b'\x00' if self.font_asset is None else b'\x01'
		if self.font_asset is not None:
			s += self.font_asset.serialize()
		
		# serialize self.font_name
		s += b'\x00' if self.font_name is None else b'\x01'
		if self.font_name is not None:
			tmp94 = b''
			tmp94 += struct.pack('I', len(self.font_name))
			while len(tmp94) and tmp94[-1] == b'\x00'[0]:
				tmp94 = tmp94[:-1]
			s += struct.pack('B', len(tmp94))
			s += tmp94
			
			s += self.font_name.encode('ISO-8859-1') if PY3 else self.font_name
		
		# serialize self.text
		s += b'\x00' if self.text is None else b'\x01'
		if self.text is not None:
			tmp95 = b''
			tmp95 += struct.pack('I', len(self.text))
			while len(tmp95) and tmp95[-1] == b'\x00'[0]:
				tmp95 = tmp95[:-1]
			s += struct.pack('B', len(tmp95))
			s += tmp95
			
			s += self.text.encode('ISO-8859-1') if PY3 else self.text
		
		# serialize self.font_size
		s += b'\x00' if self.font_size is None else b'\x01'
		if self.font_size is not None:
			s += struct.pack('f', self.font_size)
		
		# serialize self.alignment
		s += b'\x00' if self.alignment is None else b'\x01'
		if self.alignment is not None:
			s += struct.pack('h', self.alignment.value)
		
		# serialize self.word_wrapping_ratios
		s += b'\x00' if self.word_wrapping_ratios is None else b'\x01'
		if self.word_wrapping_ratios is not None:
			s += struct.pack('f', self.word_wrapping_ratios)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.font_asset
		tmp96 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp96:
			self.font_asset = Asset()
			offset = self.font_asset.deserialize(s, offset)
		else:
			self.font_asset = None
		
		# deserialize self.font_name
		tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp97:
			tmp98 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp99 = s[offset:offset + tmp98]
			offset += tmp98
			tmp99 += b'\x00' * (4 - tmp98)
			tmp100 = struct.unpack('I', tmp99)[0]
			
			self.font_name = s[offset:offset + tmp100].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp100]
			offset += tmp100
		else:
			self.font_name = None
		
		# deserialize self.text
		tmp101 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp101:
			tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp103 = s[offset:offset + tmp102]
			offset += tmp102
			tmp103 += b'\x00' * (4 - tmp102)
			tmp104 = struct.unpack('I', tmp103)[0]
			
			self.text = s[offset:offset + tmp104].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp104]
			offset += tmp104
		else:
			self.text = None
		
		# deserialize self.font_size
		tmp105 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp105:
			self.font_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.font_size = None
		
		# deserialize self.alignment
		tmp106 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp106:
			tmp107 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
			self.alignment = ETextAlignmentOption(tmp107)
		else:
			self.alignment = None
		
		# deserialize self.word_wrapping_ratios
		tmp108 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp108:
			self.word_wrapping_ratios = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.word_wrapping_ratios = None
		
		return offset


class ESliderDirection(Enum):
	LeftToRight = 0
	RightToLeft = 1
	BottomToTop = 2
	TopToBottom = 3


class ChangeSlider(BaseAction):

	@staticmethod
	def name():
		return 'ChangeSlider'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, value=None, max_value=None, min_value=None, direction=None, background_color=None, fill_color=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, value, max_value, min_value, direction, background_color, fill_color)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, value=None, max_value=None, min_value=None, direction=None, background_color=None, fill_color=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.value = value
		self.max_value = max_value
		self.min_value = min_value
		self.direction = direction
		self.background_color = background_color
		self.fill_color = fill_color
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.value
		s += b'\x00' if self.value is None else b'\x01'
		if self.value is not None:
			s += struct.pack('f', self.value)
		
		# serialize self.max_value
		s += b'\x00' if self.max_value is None else b'\x01'
		if self.max_value is not None:
			s += struct.pack('f', self.max_value)
		
		# serialize self.min_value
		s += b'\x00' if self.min_value is None else b'\x01'
		if self.min_value is not None:
			s += struct.pack('f', self.min_value)
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('h', self.direction.value)
		
		# serialize self.background_color
		s += b'\x00' if self.background_color is None else b'\x01'
		if self.background_color is not None:
			s += self.background_color.serialize()
		
		# serialize self.fill_color
		s += b'\x00' if self.fill_color is None else b'\x01'
		if self.fill_color is not None:
			s += self.fill_color.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.value
		tmp109 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp109:
			self.value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.value = None
		
		# deserialize self.max_value
		tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp110:
			self.max_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_value = None
		
		# deserialize self.min_value
		tmp111 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp111:
			self.min_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.min_value = None
		
		# deserialize self.direction
		tmp112 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp112:
			tmp113 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
			self.direction = ESliderDirection(tmp113)
		else:
			self.direction = None
		
		# deserialize self.background_color
		tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp114:
			self.background_color = Vector4()
			offset = self.background_color.deserialize(s, offset)
		else:
			self.background_color = None
		
		# deserialize self.fill_color
		tmp115 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp115:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		return offset


class ChangeImage(BaseAction):

	@staticmethod
	def name():
		return 'ChangeImage'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, sprite_asset=None, color=None, material_asset=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, sprite_asset, color, material_asset)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, sprite_asset=None, color=None, material_asset=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.sprite_asset = sprite_asset
		self.color = color
		self.material_asset = material_asset
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.sprite_asset
		s += b'\x00' if self.sprite_asset is None else b'\x01'
		if self.sprite_asset is not None:
			s += self.sprite_asset.serialize()
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.material_asset
		s += b'\x00' if self.material_asset is None else b'\x01'
		if self.material_asset is not None:
			s += self.material_asset.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.sprite_asset
		tmp116 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp116:
			self.sprite_asset = Asset()
			offset = self.sprite_asset.deserialize(s, offset)
		else:
			self.sprite_asset = None
		
		# deserialize self.color
		tmp117 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp117:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.material_asset
		tmp118 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp118:
			self.material_asset = Asset()
			offset = self.material_asset.deserialize(s, offset)
		else:
			self.material_asset = None
		
		return offset


class ChangeRawImage(BaseAction):

	@staticmethod
	def name():
		return 'ChangeRawImage'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, texture_asset=None, material_asset=None, color=None, uv_rect=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, texture_asset, material_asset, color, uv_rect)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, texture_asset=None, material_asset=None, color=None, uv_rect=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.texture_asset = texture_asset
		self.material_asset = material_asset
		self.color = color
		self.uv_rect = uv_rect
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.texture_asset
		s += b'\x00' if self.texture_asset is None else b'\x01'
		if self.texture_asset is not None:
			s += self.texture_asset.serialize()
		
		# serialize self.material_asset
		s += b'\x00' if self.material_asset is None else b'\x01'
		if self.material_asset is not None:
			s += self.material_asset.serialize()
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.uv_rect
		s += b'\x00' if self.uv_rect is None else b'\x01'
		if self.uv_rect is not None:
			s += self.uv_rect.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.texture_asset
		tmp119 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp119:
			self.texture_asset = Asset()
			offset = self.texture_asset.deserialize(s, offset)
		else:
			self.texture_asset = None
		
		# deserialize self.material_asset
		tmp120 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp120:
			self.material_asset = Asset()
			offset = self.material_asset.deserialize(s, offset)
		else:
			self.material_asset = None
		
		# deserialize self.color
		tmp121 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp121:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.uv_rect
		tmp122 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp122:
			self.uv_rect = Vector4()
			offset = self.uv_rect.deserialize(s, offset)
		else:
			self.uv_rect = None
		
		return offset


class ChangeSiblingOrder(BaseAction):

	@staticmethod
	def name():
		return 'ChangeSiblingOrder'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, new_index=None, goto_first=None, goto_last=None, change_index=None, sibling_ref_as_base_index=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, new_index, goto_first, goto_last, change_index, sibling_ref_as_base_index)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, new_index=None, goto_first=None, goto_last=None, change_index=None, sibling_ref_as_base_index=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.new_index = new_index
		self.goto_first = goto_first
		self.goto_last = goto_last
		self.change_index = change_index
		self.sibling_ref_as_base_index = sibling_ref_as_base_index
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.new_index
		s += b'\x00' if self.new_index is None else b'\x01'
		if self.new_index is not None:
			s += struct.pack('i', self.new_index)
		
		# serialize self.goto_first
		s += b'\x00' if self.goto_first is None else b'\x01'
		if self.goto_first is not None:
			s += struct.pack('?', self.goto_first)
		
		# serialize self.goto_last
		s += b'\x00' if self.goto_last is None else b'\x01'
		if self.goto_last is not None:
			s += struct.pack('?', self.goto_last)
		
		# serialize self.change_index
		s += b'\x00' if self.change_index is None else b'\x01'
		if self.change_index is not None:
			s += struct.pack('i', self.change_index)
		
		# serialize self.sibling_ref_as_base_index
		s += b'\x00' if self.sibling_ref_as_base_index is None else b'\x01'
		if self.sibling_ref_as_base_index is not None:
			tmp123 = b''
			tmp123 += struct.pack('I', len(self.sibling_ref_as_base_index))
			while len(tmp123) and tmp123[-1] == b'\x00'[0]:
				tmp123 = tmp123[:-1]
			s += struct.pack('B', len(tmp123))
			s += tmp123
			
			s += self.sibling_ref_as_base_index.encode('ISO-8859-1') if PY3 else self.sibling_ref_as_base_index
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.new_index
		tmp124 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp124:
			self.new_index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.new_index = None
		
		# deserialize self.goto_first
		tmp125 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp125:
			self.goto_first = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.goto_first = None
		
		# deserialize self.goto_last
		tmp126 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp126:
			self.goto_last = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.goto_last = None
		
		# deserialize self.change_index
		tmp127 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp127:
			self.change_index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.change_index = None
		
		# deserialize self.sibling_ref_as_base_index
		tmp128 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp128:
			tmp129 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp130 = s[offset:offset + tmp129]
			offset += tmp129
			tmp130 += b'\x00' * (4 - tmp129)
			tmp131 = struct.unpack('I', tmp130)[0]
			
			self.sibling_ref_as_base_index = s[offset:offset + tmp131].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp131]
			offset += tmp131
		else:
			self.sibling_ref_as_base_index = None
		
		return offset


class ManageComponent(BaseAction):

	@staticmethod
	def name():
		return 'ManageComponent'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, add=None, is_active=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, type, add, is_active)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, add=None, is_active=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.type = type
		self.add = add
		self.is_active = is_active
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			tmp132 = b''
			tmp132 += struct.pack('I', len(self.type))
			while len(tmp132) and tmp132[-1] == b'\x00'[0]:
				tmp132 = tmp132[:-1]
			s += struct.pack('B', len(tmp132))
			s += tmp132
			
			s += self.type.encode('ISO-8859-1') if PY3 else self.type
		
		# serialize self.add
		s += b'\x00' if self.add is None else b'\x01'
		if self.add is not None:
			s += struct.pack('?', self.add)
		
		# serialize self.is_active
		s += b'\x00' if self.is_active is None else b'\x01'
		if self.is_active is not None:
			s += struct.pack('?', self.is_active)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp133 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp133:
			tmp134 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp135 = s[offset:offset + tmp134]
			offset += tmp134
			tmp135 += b'\x00' * (4 - tmp134)
			tmp136 = struct.unpack('I', tmp135)[0]
			
			self.type = s[offset:offset + tmp136].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp136]
			offset += tmp136
		else:
			self.type = None
		
		# deserialize self.add
		tmp137 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp137:
			self.add = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.add = None
		
		# deserialize self.is_active
		tmp138 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp138:
			self.is_active = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_active = None
		
		return offset


class ChangeSprite(BaseAction):

	@staticmethod
	def name():
		return 'ChangeSprite'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, sprite_asset=None, color=None, flip_x=None, flip_y=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, sprite_asset, color, flip_x, flip_y)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, sprite_asset=None, color=None, flip_x=None, flip_y=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.sprite_asset = sprite_asset
		self.color = color
		self.flip_x = flip_x
		self.flip_y = flip_y
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.sprite_asset
		s += b'\x00' if self.sprite_asset is None else b'\x01'
		if self.sprite_asset is not None:
			s += self.sprite_asset.serialize()
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.flip_x
		s += b'\x00' if self.flip_x is None else b'\x01'
		if self.flip_x is not None:
			s += struct.pack('?', self.flip_x)
		
		# serialize self.flip_y
		s += b'\x00' if self.flip_y is None else b'\x01'
		if self.flip_y is not None:
			s += struct.pack('?', self.flip_y)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.sprite_asset
		tmp139 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp139:
			self.sprite_asset = Asset()
			offset = self.sprite_asset.deserialize(s, offset)
		else:
			self.sprite_asset = None
		
		# deserialize self.color
		tmp140 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp140:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.flip_x
		tmp141 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp141:
			self.flip_x = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.flip_x = None
		
		# deserialize self.flip_y
		tmp142 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp142:
			self.flip_y = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.flip_y = None
		
		return offset


class ChangeRenderer(BaseAction):

	@staticmethod
	def name():
		return 'ChangeRenderer'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, enabled=None, material_asset=None, material_index=None, rendering_layer_mask=None, sorting_layer_id=None, sorting_order=None, renderer_priority=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, enabled, material_asset, material_index, rendering_layer_mask, sorting_layer_id, sorting_order, renderer_priority)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, enabled=None, material_asset=None, material_index=None, rendering_layer_mask=None, sorting_layer_id=None, sorting_order=None, renderer_priority=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.enabled = enabled
		self.material_asset = material_asset
		self.material_index = material_index
		self.rendering_layer_mask = rendering_layer_mask
		self.sorting_layer_id = sorting_layer_id
		self.sorting_order = sorting_order
		self.renderer_priority = renderer_priority
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.enabled
		s += b'\x00' if self.enabled is None else b'\x01'
		if self.enabled is not None:
			s += struct.pack('?', self.enabled)
		
		# serialize self.material_asset
		s += b'\x00' if self.material_asset is None else b'\x01'
		if self.material_asset is not None:
			s += self.material_asset.serialize()
		
		# serialize self.material_index
		s += b'\x00' if self.material_index is None else b'\x01'
		if self.material_index is not None:
			s += struct.pack('i', self.material_index)
		
		# serialize self.rendering_layer_mask
		s += b'\x00' if self.rendering_layer_mask is None else b'\x01'
		if self.rendering_layer_mask is not None:
			s += struct.pack('I', self.rendering_layer_mask)
		
		# serialize self.sorting_layer_id
		s += b'\x00' if self.sorting_layer_id is None else b'\x01'
		if self.sorting_layer_id is not None:
			s += struct.pack('i', self.sorting_layer_id)
		
		# serialize self.sorting_order
		s += b'\x00' if self.sorting_order is None else b'\x01'
		if self.sorting_order is not None:
			s += struct.pack('i', self.sorting_order)
		
		# serialize self.renderer_priority
		s += b'\x00' if self.renderer_priority is None else b'\x01'
		if self.renderer_priority is not None:
			s += struct.pack('i', self.renderer_priority)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.enabled
		tmp143 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp143:
			self.enabled = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.enabled = None
		
		# deserialize self.material_asset
		tmp144 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp144:
			self.material_asset = Asset()
			offset = self.material_asset.deserialize(s, offset)
		else:
			self.material_asset = None
		
		# deserialize self.material_index
		tmp145 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp145:
			self.material_index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.material_index = None
		
		# deserialize self.rendering_layer_mask
		tmp146 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp146:
			self.rendering_layer_mask = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.rendering_layer_mask = None
		
		# deserialize self.sorting_layer_id
		tmp147 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp147:
			self.sorting_layer_id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.sorting_layer_id = None
		
		# deserialize self.sorting_order
		tmp148 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp148:
			self.sorting_order = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.sorting_order = None
		
		# deserialize self.renderer_priority
		tmp149 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp149:
			self.renderer_priority = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.renderer_priority = None
		
		return offset


class ChangeEllipse2D(BaseAction):

	@staticmethod
	def name():
		return 'ChangeEllipse2D'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, x_radius=None, y_radius=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, fill_color, x_radius, y_radius)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, x_radius=None, y_radius=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.fill_color = fill_color
		self.x_radius = x_radius
		self.y_radius = y_radius
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.fill_color
		s += b'\x00' if self.fill_color is None else b'\x01'
		if self.fill_color is not None:
			s += self.fill_color.serialize()
		
		# serialize self.x_radius
		s += b'\x00' if self.x_radius is None else b'\x01'
		if self.x_radius is not None:
			s += struct.pack('f', self.x_radius)
		
		# serialize self.y_radius
		s += b'\x00' if self.y_radius is None else b'\x01'
		if self.y_radius is not None:
			s += struct.pack('f', self.y_radius)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.fill_color
		tmp150 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp150:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.x_radius
		tmp151 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp151:
			self.x_radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x_radius = None
		
		# deserialize self.y_radius
		tmp152 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp152:
			self.y_radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y_radius = None
		
		return offset


class ChangePolygon2D(BaseAction):

	@staticmethod
	def name():
		return 'ChangePolygon2D'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, vertices=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, fill_color, vertices)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, vertices=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.fill_color = fill_color
		self.vertices = vertices
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.fill_color
		s += b'\x00' if self.fill_color is None else b'\x01'
		if self.fill_color is not None:
			s += self.fill_color.serialize()
		
		# serialize self.vertices
		s += b'\x00' if self.vertices is None else b'\x01'
		if self.vertices is not None:
			tmp153 = b''
			tmp153 += struct.pack('I', len(self.vertices))
			while len(tmp153) and tmp153[-1] == b'\x00'[0]:
				tmp153 = tmp153[:-1]
			s += struct.pack('B', len(tmp153))
			s += tmp153
			
			for tmp154 in self.vertices:
				s += b'\x00' if tmp154 is None else b'\x01'
				if tmp154 is not None:
					s += tmp154.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.fill_color
		tmp155 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp155:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.vertices
		tmp156 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp156:
			tmp157 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp158 = s[offset:offset + tmp157]
			offset += tmp157
			tmp158 += b'\x00' * (4 - tmp157)
			tmp159 = struct.unpack('I', tmp158)[0]
			
			self.vertices = []
			for tmp160 in range(tmp159):
				tmp162 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp162:
					tmp161 = Vector2()
					offset = tmp161.deserialize(s, offset)
				else:
					tmp161 = None
				self.vertices.append(tmp161)
		else:
			self.vertices = None
		
		return offset


class ChangeLine(BaseAction):

	@staticmethod
	def name():
		return 'ChangeLine'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, vertices=None, width=None, corner_vertices=None, end_cap_vertices=None, loop=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, fill_color, vertices, width, corner_vertices, end_cap_vertices, loop)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, vertices=None, width=None, corner_vertices=None, end_cap_vertices=None, loop=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.fill_color = fill_color
		self.vertices = vertices
		self.width = width
		self.corner_vertices = corner_vertices
		self.end_cap_vertices = end_cap_vertices
		self.loop = loop
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.fill_color
		s += b'\x00' if self.fill_color is None else b'\x01'
		if self.fill_color is not None:
			s += self.fill_color.serialize()
		
		# serialize self.vertices
		s += b'\x00' if self.vertices is None else b'\x01'
		if self.vertices is not None:
			tmp163 = b''
			tmp163 += struct.pack('I', len(self.vertices))
			while len(tmp163) and tmp163[-1] == b'\x00'[0]:
				tmp163 = tmp163[:-1]
			s += struct.pack('B', len(tmp163))
			s += tmp163
			
			for tmp164 in self.vertices:
				s += b'\x00' if tmp164 is None else b'\x01'
				if tmp164 is not None:
					s += tmp164.serialize()
		
		# serialize self.width
		s += b'\x00' if self.width is None else b'\x01'
		if self.width is not None:
			s += struct.pack('f', self.width)
		
		# serialize self.corner_vertices
		s += b'\x00' if self.corner_vertices is None else b'\x01'
		if self.corner_vertices is not None:
			s += struct.pack('i', self.corner_vertices)
		
		# serialize self.end_cap_vertices
		s += b'\x00' if self.end_cap_vertices is None else b'\x01'
		if self.end_cap_vertices is not None:
			s += struct.pack('i', self.end_cap_vertices)
		
		# serialize self.loop
		s += b'\x00' if self.loop is None else b'\x01'
		if self.loop is not None:
			s += struct.pack('?', self.loop)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.fill_color
		tmp165 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp165:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.vertices
		tmp166 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp166:
			tmp167 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp168 = s[offset:offset + tmp167]
			offset += tmp167
			tmp168 += b'\x00' * (4 - tmp167)
			tmp169 = struct.unpack('I', tmp168)[0]
			
			self.vertices = []
			for tmp170 in range(tmp169):
				tmp172 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp172:
					tmp171 = Vector2()
					offset = tmp171.deserialize(s, offset)
				else:
					tmp171 = None
				self.vertices.append(tmp171)
		else:
			self.vertices = None
		
		# deserialize self.width
		tmp173 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp173:
			self.width = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.corner_vertices
		tmp174 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp174:
			self.corner_vertices = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.corner_vertices = None
		
		# deserialize self.end_cap_vertices
		tmp175 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp175:
			self.end_cap_vertices = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.end_cap_vertices = None
		
		# deserialize self.loop
		tmp176 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp176:
			self.loop = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.loop = None
		
		return offset


class ELightType(Enum):
	Spot = 0
	Directional = 1
	Point = 2


class ELightShadowType(Enum):
	Disabled = 0
	Hard = 1
	Soft = 2


class ChangeLight(BaseAction):

	@staticmethod
	def name():
		return 'ChangeLight'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, range=None, spot_angle=None, color=None, intensity=None, indirect_multiplier=None, shadow_type=None, shadow_strength=None, shadow_bias=None, shadow_normal_bias=None, shadow_near_plane=None, cookie_asset=None, cookie_size=None, flare_asset=None, culling_mask=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, type, range, spot_angle, color, intensity, indirect_multiplier, shadow_type, shadow_strength, shadow_bias, shadow_normal_bias, shadow_near_plane, cookie_asset, cookie_size, flare_asset, culling_mask)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, range=None, spot_angle=None, color=None, intensity=None, indirect_multiplier=None, shadow_type=None, shadow_strength=None, shadow_bias=None, shadow_normal_bias=None, shadow_near_plane=None, cookie_asset=None, cookie_size=None, flare_asset=None, culling_mask=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.type = type
		self.range = range
		self.spot_angle = spot_angle
		self.color = color
		self.intensity = intensity
		self.indirect_multiplier = indirect_multiplier
		self.shadow_type = shadow_type
		self.shadow_strength = shadow_strength
		self.shadow_bias = shadow_bias
		self.shadow_normal_bias = shadow_normal_bias
		self.shadow_near_plane = shadow_near_plane
		self.cookie_asset = cookie_asset
		self.cookie_size = cookie_size
		self.flare_asset = flare_asset
		self.culling_mask = culling_mask
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		# serialize self.range
		s += b'\x00' if self.range is None else b'\x01'
		if self.range is not None:
			s += struct.pack('f', self.range)
		
		# serialize self.spot_angle
		s += b'\x00' if self.spot_angle is None else b'\x01'
		if self.spot_angle is not None:
			s += struct.pack('f', self.spot_angle)
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.intensity
		s += b'\x00' if self.intensity is None else b'\x01'
		if self.intensity is not None:
			s += struct.pack('f', self.intensity)
		
		# serialize self.indirect_multiplier
		s += b'\x00' if self.indirect_multiplier is None else b'\x01'
		if self.indirect_multiplier is not None:
			s += struct.pack('f', self.indirect_multiplier)
		
		# serialize self.shadow_type
		s += b'\x00' if self.shadow_type is None else b'\x01'
		if self.shadow_type is not None:
			s += struct.pack('b', self.shadow_type.value)
		
		# serialize self.shadow_strength
		s += b'\x00' if self.shadow_strength is None else b'\x01'
		if self.shadow_strength is not None:
			s += struct.pack('f', self.shadow_strength)
		
		# serialize self.shadow_bias
		s += b'\x00' if self.shadow_bias is None else b'\x01'
		if self.shadow_bias is not None:
			s += struct.pack('f', self.shadow_bias)
		
		# serialize self.shadow_normal_bias
		s += b'\x00' if self.shadow_normal_bias is None else b'\x01'
		if self.shadow_normal_bias is not None:
			s += struct.pack('f', self.shadow_normal_bias)
		
		# serialize self.shadow_near_plane
		s += b'\x00' if self.shadow_near_plane is None else b'\x01'
		if self.shadow_near_plane is not None:
			s += struct.pack('f', self.shadow_near_plane)
		
		# serialize self.cookie_asset
		s += b'\x00' if self.cookie_asset is None else b'\x01'
		if self.cookie_asset is not None:
			s += self.cookie_asset.serialize()
		
		# serialize self.cookie_size
		s += b'\x00' if self.cookie_size is None else b'\x01'
		if self.cookie_size is not None:
			s += struct.pack('f', self.cookie_size)
		
		# serialize self.flare_asset
		s += b'\x00' if self.flare_asset is None else b'\x01'
		if self.flare_asset is not None:
			s += self.flare_asset.serialize()
		
		# serialize self.culling_mask
		s += b'\x00' if self.culling_mask is None else b'\x01'
		if self.culling_mask is not None:
			s += self.culling_mask.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp177 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp177:
			tmp178 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = ELightType(tmp178)
		else:
			self.type = None
		
		# deserialize self.range
		tmp179 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp179:
			self.range = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.range = None
		
		# deserialize self.spot_angle
		tmp180 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp180:
			self.spot_angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.spot_angle = None
		
		# deserialize self.color
		tmp181 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp181:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.intensity
		tmp182 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp182:
			self.intensity = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.intensity = None
		
		# deserialize self.indirect_multiplier
		tmp183 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp183:
			self.indirect_multiplier = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.indirect_multiplier = None
		
		# deserialize self.shadow_type
		tmp184 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp184:
			tmp185 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.shadow_type = ELightShadowType(tmp185)
		else:
			self.shadow_type = None
		
		# deserialize self.shadow_strength
		tmp186 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp186:
			self.shadow_strength = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_strength = None
		
		# deserialize self.shadow_bias
		tmp187 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp187:
			self.shadow_bias = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_bias = None
		
		# deserialize self.shadow_normal_bias
		tmp188 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp188:
			self.shadow_normal_bias = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_normal_bias = None
		
		# deserialize self.shadow_near_plane
		tmp189 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp189:
			self.shadow_near_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_near_plane = None
		
		# deserialize self.cookie_asset
		tmp190 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp190:
			self.cookie_asset = Asset()
			offset = self.cookie_asset.deserialize(s, offset)
		else:
			self.cookie_asset = None
		
		# deserialize self.cookie_size
		tmp191 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp191:
			self.cookie_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.cookie_size = None
		
		# deserialize self.flare_asset
		tmp192 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp192:
			self.flare_asset = Asset()
			offset = self.flare_asset.deserialize(s, offset)
		else:
			self.flare_asset = None
		
		# deserialize self.culling_mask
		tmp193 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp193:
			self.culling_mask = LayerMask()
			offset = self.culling_mask.deserialize(s, offset)
		else:
			self.culling_mask = None
		
		return offset


class ECameraClearFlag(Enum):
	Skybox = 1
	SolidColor = 2
	Depth = 3
	Nothing = 4


class ChangeCamera(BaseAction):

	@staticmethod
	def name():
		return 'ChangeCamera'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, clear_flag=None, background_color=None, culling_mask=None, is_orthographic=None, orthographic_size=None, field_of_view=None, near_clip_plane=None, far_clip_plane=None, min_position=None, max_position=None, min_rotation=None, max_rotation=None, min_zoom=None, max_zoom=None, post_process_profile_asset=None, post_process_layers=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, clear_flag, background_color, culling_mask, is_orthographic, orthographic_size, field_of_view, near_clip_plane, far_clip_plane, min_position, max_position, min_rotation, max_rotation, min_zoom, max_zoom, post_process_profile_asset, post_process_layers)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, clear_flag=None, background_color=None, culling_mask=None, is_orthographic=None, orthographic_size=None, field_of_view=None, near_clip_plane=None, far_clip_plane=None, min_position=None, max_position=None, min_rotation=None, max_rotation=None, min_zoom=None, max_zoom=None, post_process_profile_asset=None, post_process_layers=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.clear_flag = clear_flag
		self.background_color = background_color
		self.culling_mask = culling_mask
		self.is_orthographic = is_orthographic
		self.orthographic_size = orthographic_size
		self.field_of_view = field_of_view
		self.near_clip_plane = near_clip_plane
		self.far_clip_plane = far_clip_plane
		self.min_position = min_position
		self.max_position = max_position
		self.min_rotation = min_rotation
		self.max_rotation = max_rotation
		self.min_zoom = min_zoom
		self.max_zoom = max_zoom
		self.post_process_profile_asset = post_process_profile_asset
		self.post_process_layers = post_process_layers
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.clear_flag
		s += b'\x00' if self.clear_flag is None else b'\x01'
		if self.clear_flag is not None:
			s += struct.pack('b', self.clear_flag.value)
		
		# serialize self.background_color
		s += b'\x00' if self.background_color is None else b'\x01'
		if self.background_color is not None:
			s += self.background_color.serialize()
		
		# serialize self.culling_mask
		s += b'\x00' if self.culling_mask is None else b'\x01'
		if self.culling_mask is not None:
			s += self.culling_mask.serialize()
		
		# serialize self.is_orthographic
		s += b'\x00' if self.is_orthographic is None else b'\x01'
		if self.is_orthographic is not None:
			s += struct.pack('?', self.is_orthographic)
		
		# serialize self.orthographic_size
		s += b'\x00' if self.orthographic_size is None else b'\x01'
		if self.orthographic_size is not None:
			s += struct.pack('f', self.orthographic_size)
		
		# serialize self.field_of_view
		s += b'\x00' if self.field_of_view is None else b'\x01'
		if self.field_of_view is not None:
			s += struct.pack('f', self.field_of_view)
		
		# serialize self.near_clip_plane
		s += b'\x00' if self.near_clip_plane is None else b'\x01'
		if self.near_clip_plane is not None:
			s += struct.pack('f', self.near_clip_plane)
		
		# serialize self.far_clip_plane
		s += b'\x00' if self.far_clip_plane is None else b'\x01'
		if self.far_clip_plane is not None:
			s += struct.pack('f', self.far_clip_plane)
		
		# serialize self.min_position
		s += b'\x00' if self.min_position is None else b'\x01'
		if self.min_position is not None:
			s += self.min_position.serialize()
		
		# serialize self.max_position
		s += b'\x00' if self.max_position is None else b'\x01'
		if self.max_position is not None:
			s += self.max_position.serialize()
		
		# serialize self.min_rotation
		s += b'\x00' if self.min_rotation is None else b'\x01'
		if self.min_rotation is not None:
			s += self.min_rotation.serialize()
		
		# serialize self.max_rotation
		s += b'\x00' if self.max_rotation is None else b'\x01'
		if self.max_rotation is not None:
			s += self.max_rotation.serialize()
		
		# serialize self.min_zoom
		s += b'\x00' if self.min_zoom is None else b'\x01'
		if self.min_zoom is not None:
			s += struct.pack('f', self.min_zoom)
		
		# serialize self.max_zoom
		s += b'\x00' if self.max_zoom is None else b'\x01'
		if self.max_zoom is not None:
			s += struct.pack('f', self.max_zoom)
		
		# serialize self.post_process_profile_asset
		s += b'\x00' if self.post_process_profile_asset is None else b'\x01'
		if self.post_process_profile_asset is not None:
			s += self.post_process_profile_asset.serialize()
		
		# serialize self.post_process_layers
		s += b'\x00' if self.post_process_layers is None else b'\x01'
		if self.post_process_layers is not None:
			s += self.post_process_layers.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.clear_flag
		tmp194 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp194:
			tmp195 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.clear_flag = ECameraClearFlag(tmp195)
		else:
			self.clear_flag = None
		
		# deserialize self.background_color
		tmp196 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp196:
			self.background_color = Vector4()
			offset = self.background_color.deserialize(s, offset)
		else:
			self.background_color = None
		
		# deserialize self.culling_mask
		tmp197 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp197:
			self.culling_mask = LayerMask()
			offset = self.culling_mask.deserialize(s, offset)
		else:
			self.culling_mask = None
		
		# deserialize self.is_orthographic
		tmp198 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp198:
			self.is_orthographic = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_orthographic = None
		
		# deserialize self.orthographic_size
		tmp199 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp199:
			self.orthographic_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.orthographic_size = None
		
		# deserialize self.field_of_view
		tmp200 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp200:
			self.field_of_view = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.field_of_view = None
		
		# deserialize self.near_clip_plane
		tmp201 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp201:
			self.near_clip_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.near_clip_plane = None
		
		# deserialize self.far_clip_plane
		tmp202 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp202:
			self.far_clip_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.far_clip_plane = None
		
		# deserialize self.min_position
		tmp203 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp203:
			self.min_position = Vector3()
			offset = self.min_position.deserialize(s, offset)
		else:
			self.min_position = None
		
		# deserialize self.max_position
		tmp204 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp204:
			self.max_position = Vector3()
			offset = self.max_position.deserialize(s, offset)
		else:
			self.max_position = None
		
		# deserialize self.min_rotation
		tmp205 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp205:
			self.min_rotation = Vector2()
			offset = self.min_rotation.deserialize(s, offset)
		else:
			self.min_rotation = None
		
		# deserialize self.max_rotation
		tmp206 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp206:
			self.max_rotation = Vector2()
			offset = self.max_rotation.deserialize(s, offset)
		else:
			self.max_rotation = None
		
		# deserialize self.min_zoom
		tmp207 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp207:
			self.min_zoom = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.min_zoom = None
		
		# deserialize self.max_zoom
		tmp208 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp208:
			self.max_zoom = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_zoom = None
		
		# deserialize self.post_process_profile_asset
		tmp209 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp209:
			self.post_process_profile_asset = Asset()
			offset = self.post_process_profile_asset.deserialize(s, offset)
		else:
			self.post_process_profile_asset = None
		
		# deserialize self.post_process_layers
		tmp210 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp210:
			self.post_process_layers = LayerMask()
			offset = self.post_process_layers.deserialize(s, offset)
		else:
			self.post_process_layers = None
		
		return offset


class ClearScene(BaseAction):

	@staticmethod
	def name():
		return 'ClearScene'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		self.initialize(cycle, ref, child_ref, duration_cycles)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		return offset


class EAmbientMode(Enum):
	Skybox = 0
	Trilight = 1
	Flat = 3
	Custom = 4


class EDefaultReflectionMode(Enum):
	Skybox = 0
	Custom = 1


class EFogMode(Enum):
	Linear = 1
	Exponential = 2
	ExponentialSquared = 3


class ChangeRenderSettings(BaseAction):

	@staticmethod
	def name():
		return 'ChangeRenderSettings'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, backward_changes=None, ambient_equator_color=None, ambient_ground_color=None, ambient_intensity=None, ambient_light=None, ambient_mode=None, ambient_sky_color=None, custom_reflection_asset=None, default_reflection_mode=None, default_reflection_resolution=None, flare_fade_speed=None, flare_strength=None, has_fog=None, fog_mode=None, fog_color=None, fog_density=None, fog_start_distance=None, fog_end_distance=None, halo_strength=None, reflection_bounces=None, reflection_intensity=None, skybox_asset=None, subtractive_shadow_color=None, sun_ref=None, sun_child_ref=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, backward_changes, ambient_equator_color, ambient_ground_color, ambient_intensity, ambient_light, ambient_mode, ambient_sky_color, custom_reflection_asset, default_reflection_mode, default_reflection_resolution, flare_fade_speed, flare_strength, has_fog, fog_mode, fog_color, fog_density, fog_start_distance, fog_end_distance, halo_strength, reflection_bounces, reflection_intensity, skybox_asset, subtractive_shadow_color, sun_ref, sun_child_ref)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, backward_changes=None, ambient_equator_color=None, ambient_ground_color=None, ambient_intensity=None, ambient_light=None, ambient_mode=None, ambient_sky_color=None, custom_reflection_asset=None, default_reflection_mode=None, default_reflection_resolution=None, flare_fade_speed=None, flare_strength=None, has_fog=None, fog_mode=None, fog_color=None, fog_density=None, fog_start_distance=None, fog_end_distance=None, halo_strength=None, reflection_bounces=None, reflection_intensity=None, skybox_asset=None, subtractive_shadow_color=None, sun_ref=None, sun_child_ref=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.backward_changes = backward_changes
		self.ambient_equator_color = ambient_equator_color
		self.ambient_ground_color = ambient_ground_color
		self.ambient_intensity = ambient_intensity
		self.ambient_light = ambient_light
		self.ambient_mode = ambient_mode
		self.ambient_sky_color = ambient_sky_color
		self.custom_reflection_asset = custom_reflection_asset
		self.default_reflection_mode = default_reflection_mode
		self.default_reflection_resolution = default_reflection_resolution
		self.flare_fade_speed = flare_fade_speed
		self.flare_strength = flare_strength
		self.has_fog = has_fog
		self.fog_mode = fog_mode
		self.fog_color = fog_color
		self.fog_density = fog_density
		self.fog_start_distance = fog_start_distance
		self.fog_end_distance = fog_end_distance
		self.halo_strength = halo_strength
		self.reflection_bounces = reflection_bounces
		self.reflection_intensity = reflection_intensity
		self.skybox_asset = skybox_asset
		self.subtractive_shadow_color = subtractive_shadow_color
		self.sun_ref = sun_ref
		self.sun_child_ref = sun_child_ref
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.backward_changes
		s += b'\x00' if self.backward_changes is None else b'\x01'
		if self.backward_changes is not None:
			s += struct.pack('?', self.backward_changes)
		
		# serialize self.ambient_equator_color
		s += b'\x00' if self.ambient_equator_color is None else b'\x01'
		if self.ambient_equator_color is not None:
			s += self.ambient_equator_color.serialize()
		
		# serialize self.ambient_ground_color
		s += b'\x00' if self.ambient_ground_color is None else b'\x01'
		if self.ambient_ground_color is not None:
			s += self.ambient_ground_color.serialize()
		
		# serialize self.ambient_intensity
		s += b'\x00' if self.ambient_intensity is None else b'\x01'
		if self.ambient_intensity is not None:
			s += struct.pack('f', self.ambient_intensity)
		
		# serialize self.ambient_light
		s += b'\x00' if self.ambient_light is None else b'\x01'
		if self.ambient_light is not None:
			s += self.ambient_light.serialize()
		
		# serialize self.ambient_mode
		s += b'\x00' if self.ambient_mode is None else b'\x01'
		if self.ambient_mode is not None:
			s += struct.pack('b', self.ambient_mode.value)
		
		# serialize self.ambient_sky_color
		s += b'\x00' if self.ambient_sky_color is None else b'\x01'
		if self.ambient_sky_color is not None:
			s += self.ambient_sky_color.serialize()
		
		# serialize self.custom_reflection_asset
		s += b'\x00' if self.custom_reflection_asset is None else b'\x01'
		if self.custom_reflection_asset is not None:
			s += self.custom_reflection_asset.serialize()
		
		# serialize self.default_reflection_mode
		s += b'\x00' if self.default_reflection_mode is None else b'\x01'
		if self.default_reflection_mode is not None:
			s += struct.pack('b', self.default_reflection_mode.value)
		
		# serialize self.default_reflection_resolution
		s += b'\x00' if self.default_reflection_resolution is None else b'\x01'
		if self.default_reflection_resolution is not None:
			s += struct.pack('i', self.default_reflection_resolution)
		
		# serialize self.flare_fade_speed
		s += b'\x00' if self.flare_fade_speed is None else b'\x01'
		if self.flare_fade_speed is not None:
			s += struct.pack('f', self.flare_fade_speed)
		
		# serialize self.flare_strength
		s += b'\x00' if self.flare_strength is None else b'\x01'
		if self.flare_strength is not None:
			s += struct.pack('f', self.flare_strength)
		
		# serialize self.has_fog
		s += b'\x00' if self.has_fog is None else b'\x01'
		if self.has_fog is not None:
			s += struct.pack('?', self.has_fog)
		
		# serialize self.fog_mode
		s += b'\x00' if self.fog_mode is None else b'\x01'
		if self.fog_mode is not None:
			s += struct.pack('b', self.fog_mode.value)
		
		# serialize self.fog_color
		s += b'\x00' if self.fog_color is None else b'\x01'
		if self.fog_color is not None:
			s += self.fog_color.serialize()
		
		# serialize self.fog_density
		s += b'\x00' if self.fog_density is None else b'\x01'
		if self.fog_density is not None:
			s += struct.pack('f', self.fog_density)
		
		# serialize self.fog_start_distance
		s += b'\x00' if self.fog_start_distance is None else b'\x01'
		if self.fog_start_distance is not None:
			s += struct.pack('f', self.fog_start_distance)
		
		# serialize self.fog_end_distance
		s += b'\x00' if self.fog_end_distance is None else b'\x01'
		if self.fog_end_distance is not None:
			s += struct.pack('f', self.fog_end_distance)
		
		# serialize self.halo_strength
		s += b'\x00' if self.halo_strength is None else b'\x01'
		if self.halo_strength is not None:
			s += struct.pack('f', self.halo_strength)
		
		# serialize self.reflection_bounces
		s += b'\x00' if self.reflection_bounces is None else b'\x01'
		if self.reflection_bounces is not None:
			s += struct.pack('i', self.reflection_bounces)
		
		# serialize self.reflection_intensity
		s += b'\x00' if self.reflection_intensity is None else b'\x01'
		if self.reflection_intensity is not None:
			s += struct.pack('f', self.reflection_intensity)
		
		# serialize self.skybox_asset
		s += b'\x00' if self.skybox_asset is None else b'\x01'
		if self.skybox_asset is not None:
			s += self.skybox_asset.serialize()
		
		# serialize self.subtractive_shadow_color
		s += b'\x00' if self.subtractive_shadow_color is None else b'\x01'
		if self.subtractive_shadow_color is not None:
			s += self.subtractive_shadow_color.serialize()
		
		# serialize self.sun_ref
		s += b'\x00' if self.sun_ref is None else b'\x01'
		if self.sun_ref is not None:
			s += struct.pack('i', self.sun_ref)
		
		# serialize self.sun_child_ref
		s += b'\x00' if self.sun_child_ref is None else b'\x01'
		if self.sun_child_ref is not None:
			tmp211 = b''
			tmp211 += struct.pack('I', len(self.sun_child_ref))
			while len(tmp211) and tmp211[-1] == b'\x00'[0]:
				tmp211 = tmp211[:-1]
			s += struct.pack('B', len(tmp211))
			s += tmp211
			
			s += self.sun_child_ref.encode('ISO-8859-1') if PY3 else self.sun_child_ref
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.backward_changes
		tmp212 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp212:
			self.backward_changes = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.backward_changes = None
		
		# deserialize self.ambient_equator_color
		tmp213 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp213:
			self.ambient_equator_color = Vector4()
			offset = self.ambient_equator_color.deserialize(s, offset)
		else:
			self.ambient_equator_color = None
		
		# deserialize self.ambient_ground_color
		tmp214 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp214:
			self.ambient_ground_color = Vector4()
			offset = self.ambient_ground_color.deserialize(s, offset)
		else:
			self.ambient_ground_color = None
		
		# deserialize self.ambient_intensity
		tmp215 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp215:
			self.ambient_intensity = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ambient_intensity = None
		
		# deserialize self.ambient_light
		tmp216 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp216:
			self.ambient_light = Vector4()
			offset = self.ambient_light.deserialize(s, offset)
		else:
			self.ambient_light = None
		
		# deserialize self.ambient_mode
		tmp217 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp217:
			tmp218 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.ambient_mode = EAmbientMode(tmp218)
		else:
			self.ambient_mode = None
		
		# deserialize self.ambient_sky_color
		tmp219 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp219:
			self.ambient_sky_color = Vector4()
			offset = self.ambient_sky_color.deserialize(s, offset)
		else:
			self.ambient_sky_color = None
		
		# deserialize self.custom_reflection_asset
		tmp220 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp220:
			self.custom_reflection_asset = Asset()
			offset = self.custom_reflection_asset.deserialize(s, offset)
		else:
			self.custom_reflection_asset = None
		
		# deserialize self.default_reflection_mode
		tmp221 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp221:
			tmp222 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.default_reflection_mode = EDefaultReflectionMode(tmp222)
		else:
			self.default_reflection_mode = None
		
		# deserialize self.default_reflection_resolution
		tmp223 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp223:
			self.default_reflection_resolution = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.default_reflection_resolution = None
		
		# deserialize self.flare_fade_speed
		tmp224 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp224:
			self.flare_fade_speed = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.flare_fade_speed = None
		
		# deserialize self.flare_strength
		tmp225 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp225:
			self.flare_strength = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.flare_strength = None
		
		# deserialize self.has_fog
		tmp226 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp226:
			self.has_fog = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.has_fog = None
		
		# deserialize self.fog_mode
		tmp227 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp227:
			tmp228 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.fog_mode = EFogMode(tmp228)
		else:
			self.fog_mode = None
		
		# deserialize self.fog_color
		tmp229 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp229:
			self.fog_color = Vector4()
			offset = self.fog_color.deserialize(s, offset)
		else:
			self.fog_color = None
		
		# deserialize self.fog_density
		tmp230 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp230:
			self.fog_density = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.fog_density = None
		
		# deserialize self.fog_start_distance
		tmp231 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp231:
			self.fog_start_distance = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.fog_start_distance = None
		
		# deserialize self.fog_end_distance
		tmp232 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp232:
			self.fog_end_distance = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.fog_end_distance = None
		
		# deserialize self.halo_strength
		tmp233 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp233:
			self.halo_strength = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.halo_strength = None
		
		# deserialize self.reflection_bounces
		tmp234 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp234:
			self.reflection_bounces = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.reflection_bounces = None
		
		# deserialize self.reflection_intensity
		tmp235 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp235:
			self.reflection_intensity = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.reflection_intensity = None
		
		# deserialize self.skybox_asset
		tmp236 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp236:
			self.skybox_asset = Asset()
			offset = self.skybox_asset.deserialize(s, offset)
		else:
			self.skybox_asset = None
		
		# deserialize self.subtractive_shadow_color
		tmp237 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp237:
			self.subtractive_shadow_color = Vector4()
			offset = self.subtractive_shadow_color.deserialize(s, offset)
		else:
			self.subtractive_shadow_color = None
		
		# deserialize self.sun_ref
		tmp238 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp238:
			self.sun_ref = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.sun_ref = None
		
		# deserialize self.sun_child_ref
		tmp239 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp239:
			tmp240 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp241 = s[offset:offset + tmp240]
			offset += tmp240
			tmp241 += b'\x00' * (4 - tmp240)
			tmp242 = struct.unpack('I', tmp241)[0]
			
			self.sun_child_ref = s[offset:offset + tmp242].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp242]
			offset += tmp242
		else:
			self.sun_child_ref = None
		
		return offset


class EParadoxGraphType(Enum):
	Flow = 0
	BehaviourTree = 1
	FSM = 2


class ChangeParadoxGraph(BaseAction):

	@staticmethod
	def name():
		return 'ChangeParadoxGraph'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, graph_asset=None, play=None, stop=None, restart=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, type, graph_asset, play, stop, restart)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, graph_asset=None, play=None, stop=None, restart=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.type = type
		self.graph_asset = graph_asset
		self.play = play
		self.stop = stop
		self.restart = restart
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		# serialize self.graph_asset
		s += b'\x00' if self.graph_asset is None else b'\x01'
		if self.graph_asset is not None:
			s += self.graph_asset.serialize()
		
		# serialize self.play
		s += b'\x00' if self.play is None else b'\x01'
		if self.play is not None:
			s += struct.pack('?', self.play)
		
		# serialize self.stop
		s += b'\x00' if self.stop is None else b'\x01'
		if self.stop is not None:
			s += struct.pack('?', self.stop)
		
		# serialize self.restart
		s += b'\x00' if self.restart is None else b'\x01'
		if self.restart is not None:
			s += struct.pack('?', self.restart)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp243 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp243:
			tmp244 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EParadoxGraphType(tmp244)
		else:
			self.type = None
		
		# deserialize self.graph_asset
		tmp245 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp245:
			self.graph_asset = Asset()
			offset = self.graph_asset.deserialize(s, offset)
		else:
			self.graph_asset = None
		
		# deserialize self.play
		tmp246 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp246:
			self.play = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.play = None
		
		# deserialize self.stop
		tmp247 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp247:
			self.stop = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.stop = None
		
		# deserialize self.restart
		tmp248 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp248:
			self.restart = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.restart = None
		
		return offset


class ChangeParadoxBehaviourTree(BaseAction):

	@staticmethod
	def name():
		return 'ChangeParadoxBehaviourTree'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, repeat=None, update_interval=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, repeat, update_interval)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, repeat=None, update_interval=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.repeat = repeat
		self.update_interval = update_interval
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.repeat
		s += b'\x00' if self.repeat is None else b'\x01'
		if self.repeat is not None:
			s += struct.pack('?', self.repeat)
		
		# serialize self.update_interval
		s += b'\x00' if self.update_interval is None else b'\x01'
		if self.update_interval is not None:
			s += struct.pack('f', self.update_interval)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.repeat
		tmp249 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp249:
			self.repeat = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.repeat = None
		
		# deserialize self.update_interval
		tmp250 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp250:
			self.update_interval = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.update_interval = None
		
		return offset


class ChangeParadoxFSM(BaseAction):

	@staticmethod
	def name():
		return 'ChangeParadoxFSM'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, trigger_states_name=None, hard_trigger=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, trigger_states_name, hard_trigger)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, trigger_states_name=None, hard_trigger=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.trigger_states_name = trigger_states_name
		self.hard_trigger = hard_trigger
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.trigger_states_name
		s += b'\x00' if self.trigger_states_name is None else b'\x01'
		if self.trigger_states_name is not None:
			tmp251 = b''
			tmp251 += struct.pack('I', len(self.trigger_states_name))
			while len(tmp251) and tmp251[-1] == b'\x00'[0]:
				tmp251 = tmp251[:-1]
			s += struct.pack('B', len(tmp251))
			s += tmp251
			
			for tmp252 in self.trigger_states_name:
				s += b'\x00' if tmp252 is None else b'\x01'
				if tmp252 is not None:
					tmp253 = b''
					tmp253 += struct.pack('I', len(tmp252))
					while len(tmp253) and tmp253[-1] == b'\x00'[0]:
						tmp253 = tmp253[:-1]
					s += struct.pack('B', len(tmp253))
					s += tmp253
					
					s += tmp252.encode('ISO-8859-1') if PY3 else tmp252
		
		# serialize self.hard_trigger
		s += b'\x00' if self.hard_trigger is None else b'\x01'
		if self.hard_trigger is not None:
			tmp254 = b''
			tmp254 += struct.pack('I', len(self.hard_trigger))
			while len(tmp254) and tmp254[-1] == b'\x00'[0]:
				tmp254 = tmp254[:-1]
			s += struct.pack('B', len(tmp254))
			s += tmp254
			
			for tmp255 in self.hard_trigger:
				s += b'\x00' if tmp255 is None else b'\x01'
				if tmp255 is not None:
					s += struct.pack('?', tmp255)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.trigger_states_name
		tmp256 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp256:
			tmp257 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp258 = s[offset:offset + tmp257]
			offset += tmp257
			tmp258 += b'\x00' * (4 - tmp257)
			tmp259 = struct.unpack('I', tmp258)[0]
			
			self.trigger_states_name = []
			for tmp260 in range(tmp259):
				tmp262 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp262:
					tmp263 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp264 = s[offset:offset + tmp263]
					offset += tmp263
					tmp264 += b'\x00' * (4 - tmp263)
					tmp265 = struct.unpack('I', tmp264)[0]
					
					tmp261 = s[offset:offset + tmp265].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp265]
					offset += tmp265
				else:
					tmp261 = None
				self.trigger_states_name.append(tmp261)
		else:
			self.trigger_states_name = None
		
		# deserialize self.hard_trigger
		tmp266 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp266:
			tmp267 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp268 = s[offset:offset + tmp267]
			offset += tmp267
			tmp268 += b'\x00' * (4 - tmp267)
			tmp269 = struct.unpack('I', tmp268)[0]
			
			self.hard_trigger = []
			for tmp270 in range(tmp269):
				tmp272 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp272:
					tmp271 = struct.unpack('?', s[offset:offset + 1])[0]
					offset += 1
				else:
					tmp271 = None
				self.hard_trigger.append(tmp271)
		else:
			self.hard_trigger = None
		
		return offset


class EParadoxBlackboardVariableType(Enum):
	Simple = 0
	List = 1
	Dictionary = 2


class EParadoxBlackboardOperationType(Enum):
	Edit = 0
	Add = 1
	Remove = 2


class EParadoxBlackboardValueType(Enum):
	Int = 0
	Float = 1
	Bool = 2
	String = 3
	GameObject = 4
	Vector2 = 5
	Vector3 = 6
	Vector4 = 7
	Color = 8
	LayerMask = 9
	Asset = 10


class ChangeParadoxBlackboard(BaseAction):

	@staticmethod
	def name():
		return 'ChangeParadoxBlackboard'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, var_name=None, value_type=None, var_type=None, op_type=None, list_index=None, dictionary_key=None, int_value=None, float_value=None, bool_value=None, string_value=None, game_object_ref=None, game_object_child_ref=None, vector_value=None, layer_mask_value=None, asset_type=None, asset_value=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, var_name, value_type, var_type, op_type, list_index, dictionary_key, int_value, float_value, bool_value, string_value, game_object_ref, game_object_child_ref, vector_value, layer_mask_value, asset_type, asset_value)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, var_name=None, value_type=None, var_type=None, op_type=None, list_index=None, dictionary_key=None, int_value=None, float_value=None, bool_value=None, string_value=None, game_object_ref=None, game_object_child_ref=None, vector_value=None, layer_mask_value=None, asset_type=None, asset_value=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.var_name = var_name
		self.value_type = value_type
		self.var_type = var_type
		self.op_type = op_type
		self.list_index = list_index
		self.dictionary_key = dictionary_key
		self.int_value = int_value
		self.float_value = float_value
		self.bool_value = bool_value
		self.string_value = string_value
		self.game_object_ref = game_object_ref
		self.game_object_child_ref = game_object_child_ref
		self.vector_value = vector_value
		self.layer_mask_value = layer_mask_value
		self.asset_type = asset_type
		self.asset_value = asset_value
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.var_name
		s += b'\x00' if self.var_name is None else b'\x01'
		if self.var_name is not None:
			tmp273 = b''
			tmp273 += struct.pack('I', len(self.var_name))
			while len(tmp273) and tmp273[-1] == b'\x00'[0]:
				tmp273 = tmp273[:-1]
			s += struct.pack('B', len(tmp273))
			s += tmp273
			
			s += self.var_name.encode('ISO-8859-1') if PY3 else self.var_name
		
		# serialize self.value_type
		s += b'\x00' if self.value_type is None else b'\x01'
		if self.value_type is not None:
			s += struct.pack('b', self.value_type.value)
		
		# serialize self.var_type
		s += b'\x00' if self.var_type is None else b'\x01'
		if self.var_type is not None:
			s += struct.pack('b', self.var_type.value)
		
		# serialize self.op_type
		s += b'\x00' if self.op_type is None else b'\x01'
		if self.op_type is not None:
			s += struct.pack('b', self.op_type.value)
		
		# serialize self.list_index
		s += b'\x00' if self.list_index is None else b'\x01'
		if self.list_index is not None:
			s += struct.pack('i', self.list_index)
		
		# serialize self.dictionary_key
		s += b'\x00' if self.dictionary_key is None else b'\x01'
		if self.dictionary_key is not None:
			tmp274 = b''
			tmp274 += struct.pack('I', len(self.dictionary_key))
			while len(tmp274) and tmp274[-1] == b'\x00'[0]:
				tmp274 = tmp274[:-1]
			s += struct.pack('B', len(tmp274))
			s += tmp274
			
			s += self.dictionary_key.encode('ISO-8859-1') if PY3 else self.dictionary_key
		
		# serialize self.int_value
		s += b'\x00' if self.int_value is None else b'\x01'
		if self.int_value is not None:
			s += struct.pack('i', self.int_value)
		
		# serialize self.float_value
		s += b'\x00' if self.float_value is None else b'\x01'
		if self.float_value is not None:
			s += struct.pack('f', self.float_value)
		
		# serialize self.bool_value
		s += b'\x00' if self.bool_value is None else b'\x01'
		if self.bool_value is not None:
			s += struct.pack('?', self.bool_value)
		
		# serialize self.string_value
		s += b'\x00' if self.string_value is None else b'\x01'
		if self.string_value is not None:
			tmp275 = b''
			tmp275 += struct.pack('I', len(self.string_value))
			while len(tmp275) and tmp275[-1] == b'\x00'[0]:
				tmp275 = tmp275[:-1]
			s += struct.pack('B', len(tmp275))
			s += tmp275
			
			s += self.string_value.encode('ISO-8859-1') if PY3 else self.string_value
		
		# serialize self.game_object_ref
		s += b'\x00' if self.game_object_ref is None else b'\x01'
		if self.game_object_ref is not None:
			s += struct.pack('i', self.game_object_ref)
		
		# serialize self.game_object_child_ref
		s += b'\x00' if self.game_object_child_ref is None else b'\x01'
		if self.game_object_child_ref is not None:
			tmp276 = b''
			tmp276 += struct.pack('I', len(self.game_object_child_ref))
			while len(tmp276) and tmp276[-1] == b'\x00'[0]:
				tmp276 = tmp276[:-1]
			s += struct.pack('B', len(tmp276))
			s += tmp276
			
			s += self.game_object_child_ref.encode('ISO-8859-1') if PY3 else self.game_object_child_ref
		
		# serialize self.vector_value
		s += b'\x00' if self.vector_value is None else b'\x01'
		if self.vector_value is not None:
			s += self.vector_value.serialize()
		
		# serialize self.layer_mask_value
		s += b'\x00' if self.layer_mask_value is None else b'\x01'
		if self.layer_mask_value is not None:
			s += self.layer_mask_value.serialize()
		
		# serialize self.asset_type
		s += b'\x00' if self.asset_type is None else b'\x01'
		if self.asset_type is not None:
			tmp277 = b''
			tmp277 += struct.pack('I', len(self.asset_type))
			while len(tmp277) and tmp277[-1] == b'\x00'[0]:
				tmp277 = tmp277[:-1]
			s += struct.pack('B', len(tmp277))
			s += tmp277
			
			s += self.asset_type.encode('ISO-8859-1') if PY3 else self.asset_type
		
		# serialize self.asset_value
		s += b'\x00' if self.asset_value is None else b'\x01'
		if self.asset_value is not None:
			s += self.asset_value.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.var_name
		tmp278 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp278:
			tmp279 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp280 = s[offset:offset + tmp279]
			offset += tmp279
			tmp280 += b'\x00' * (4 - tmp279)
			tmp281 = struct.unpack('I', tmp280)[0]
			
			self.var_name = s[offset:offset + tmp281].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp281]
			offset += tmp281
		else:
			self.var_name = None
		
		# deserialize self.value_type
		tmp282 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp282:
			tmp283 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.value_type = EParadoxBlackboardValueType(tmp283)
		else:
			self.value_type = None
		
		# deserialize self.var_type
		tmp284 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp284:
			tmp285 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.var_type = EParadoxBlackboardVariableType(tmp285)
		else:
			self.var_type = None
		
		# deserialize self.op_type
		tmp286 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp286:
			tmp287 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.op_type = EParadoxBlackboardOperationType(tmp287)
		else:
			self.op_type = None
		
		# deserialize self.list_index
		tmp288 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp288:
			self.list_index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.list_index = None
		
		# deserialize self.dictionary_key
		tmp289 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp289:
			tmp290 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp291 = s[offset:offset + tmp290]
			offset += tmp290
			tmp291 += b'\x00' * (4 - tmp290)
			tmp292 = struct.unpack('I', tmp291)[0]
			
			self.dictionary_key = s[offset:offset + tmp292].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp292]
			offset += tmp292
		else:
			self.dictionary_key = None
		
		# deserialize self.int_value
		tmp293 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp293:
			self.int_value = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.int_value = None
		
		# deserialize self.float_value
		tmp294 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp294:
			self.float_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.float_value = None
		
		# deserialize self.bool_value
		tmp295 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp295:
			self.bool_value = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.bool_value = None
		
		# deserialize self.string_value
		tmp296 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp296:
			tmp297 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp298 = s[offset:offset + tmp297]
			offset += tmp297
			tmp298 += b'\x00' * (4 - tmp297)
			tmp299 = struct.unpack('I', tmp298)[0]
			
			self.string_value = s[offset:offset + tmp299].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp299]
			offset += tmp299
		else:
			self.string_value = None
		
		# deserialize self.game_object_ref
		tmp300 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp300:
			self.game_object_ref = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.game_object_ref = None
		
		# deserialize self.game_object_child_ref
		tmp301 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp301:
			tmp302 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp303 = s[offset:offset + tmp302]
			offset += tmp302
			tmp303 += b'\x00' * (4 - tmp302)
			tmp304 = struct.unpack('I', tmp303)[0]
			
			self.game_object_child_ref = s[offset:offset + tmp304].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp304]
			offset += tmp304
		else:
			self.game_object_child_ref = None
		
		# deserialize self.vector_value
		tmp305 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp305:
			self.vector_value = Vector4()
			offset = self.vector_value.deserialize(s, offset)
		else:
			self.vector_value = None
		
		# deserialize self.layer_mask_value
		tmp306 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp306:
			self.layer_mask_value = LayerMask()
			offset = self.layer_mask_value.deserialize(s, offset)
		else:
			self.layer_mask_value = None
		
		# deserialize self.asset_type
		tmp307 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp307:
			tmp308 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp309 = s[offset:offset + tmp308]
			offset += tmp308
			tmp309 += b'\x00' * (4 - tmp308)
			tmp310 = struct.unpack('I', tmp309)[0]
			
			self.asset_type = s[offset:offset + tmp310].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp310]
			offset += tmp310
		else:
			self.asset_type = None
		
		# deserialize self.asset_value
		tmp311 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp311:
			self.asset_value = Asset()
			offset = self.asset_value.deserialize(s, offset)
		else:
			self.asset_value = None
		
		return offset


class EndCycle(object):

	@staticmethod
	def name():
		return 'EndCycle'


	def __init__(self):
		self.initialize()
	

	def initialize(self):
		pass
	

	def serialize(self):
		s = b''
		
		return s
	

	def deserialize(self, s, offset=0):
		return offset
