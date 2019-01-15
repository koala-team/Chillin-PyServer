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
			tmp28 = b''
			tmp28 += struct.pack('I', len(self.parent_child_ref))
			while len(tmp28) and tmp28[-1] == b'\x00'[0]:
				tmp28 = tmp28[:-1]
			s += struct.pack('B', len(tmp28))
			s += tmp28
			
			s += self.parent_child_ref.encode('ISO-8859-1') if PY3 else self.parent_child_ref
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.parent_ref
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			self.parent_ref = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.parent_ref = None
		
		# deserialize self.parent_child_ref
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp32 = s[offset:offset + tmp31]
			offset += tmp31
			tmp32 += b'\x00' * (4 - tmp31)
			tmp33 = struct.unpack('I', tmp32)[0]
			
			self.parent_child_ref = s[offset:offset + tmp33].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp33]
			offset += tmp33
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
		tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp34:
			self.asset = Asset()
			offset = self.asset.deserialize(s, offset)
		else:
			self.asset = None
		
		# deserialize self.default_parent
		tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp35:
			tmp36 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.default_parent = EDefaultParent(tmp36)
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
		tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp37:
			tmp38 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EBasicObjectType(tmp38)
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
		tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp39:
			tmp40 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EUIElementType(tmp40)
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
		tmp41 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp41:
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
		tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp42:
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
		tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp43:
			self.position = Vector3()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.rotation
		tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp44:
			self.rotation = Vector3()
			offset = self.rotation.deserialize(s, offset)
		else:
			self.rotation = None
		
		# deserialize self.scale
		tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp45:
			self.scale = Vector3()
			offset = self.scale.deserialize(s, offset)
		else:
			self.scale = None
		
		# deserialize self.change_local
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
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
			tmp47 = b''
			tmp47 += struct.pack('I', len(self.var_name))
			while len(tmp47) and tmp47[-1] == b'\x00'[0]:
				tmp47 = tmp47[:-1]
			s += struct.pack('B', len(tmp47))
			s += tmp47
			
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
		tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp48:
			tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp50 = s[offset:offset + tmp49]
			offset += tmp49
			tmp50 += b'\x00' * (4 - tmp49)
			tmp51 = struct.unpack('I', tmp50)[0]
			
			self.var_name = s[offset:offset + tmp51].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp51]
			offset += tmp51
		else:
			self.var_name = None
		
		# deserialize self.var_type
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			tmp53 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.var_type = EAnimatorVariableType(tmp53)
		else:
			self.var_type = None
		
		# deserialize self.int_value
		tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp54:
			self.int_value = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.int_value = None
		
		# deserialize self.float_value
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			self.float_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.float_value = None
		
		# deserialize self.bool_value
		tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp56:
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
			tmp57 = b''
			tmp57 += struct.pack('I', len(self.state_name))
			while len(tmp57) and tmp57[-1] == b'\x00'[0]:
				tmp57 = tmp57[:-1]
			s += struct.pack('B', len(tmp57))
			s += tmp57
			
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
		tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp58:
			tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp60 = s[offset:offset + tmp59]
			offset += tmp59
			tmp60 += b'\x00' * (4 - tmp59)
			tmp61 = struct.unpack('I', tmp60)[0]
			
			self.state_name = s[offset:offset + tmp61].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp61]
			offset += tmp61
		else:
			self.state_name = None
		
		# deserialize self.layer
		tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp62:
			self.layer = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.layer = None
		
		# deserialize self.normalized_time
		tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp63:
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
		tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp64:
			self.audio_clip_asset = Asset()
			offset = self.audio_clip_asset.deserialize(s, offset)
		else:
			self.audio_clip_asset = None
		
		# deserialize self.time
		tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp65:
			self.time = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.time = None
		
		# deserialize self.mute
		tmp66 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp66:
			self.mute = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.mute = None
		
		# deserialize self.loop
		tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp67:
			self.loop = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.loop = None
		
		# deserialize self.priority
		tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp68:
			self.priority = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.priority = None
		
		# deserialize self.volume
		tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp69:
			self.volume = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.volume = None
		
		# deserialize self.spatial_blend
		tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp70:
			self.spatial_blend = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.spatial_blend = None
		
		# deserialize self.play
		tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp71:
			self.play = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.play = None
		
		# deserialize self.stop
		tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp72:
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
		tmp73 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp73:
			self.position = Vector3()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.rotation
		tmp74 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp74:
			self.rotation = Vector3()
			offset = self.rotation.deserialize(s, offset)
		else:
			self.rotation = None
		
		# deserialize self.scale
		tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp75:
			self.scale = Vector3()
			offset = self.scale.deserialize(s, offset)
		else:
			self.scale = None
		
		# deserialize self.pivot
		tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp76:
			self.pivot = Vector2()
			offset = self.pivot.deserialize(s, offset)
		else:
			self.pivot = None
		
		# deserialize self.anchor_min
		tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp77:
			self.anchor_min = Vector2()
			offset = self.anchor_min.deserialize(s, offset)
		else:
			self.anchor_min = None
		
		# deserialize self.anchor_max
		tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp78:
			self.anchor_max = Vector2()
			offset = self.anchor_max.deserialize(s, offset)
		else:
			self.anchor_max = None
		
		# deserialize self.size
		tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp79:
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
			tmp80 = b''
			tmp80 += struct.pack('I', len(self.font_name))
			while len(tmp80) and tmp80[-1] == b'\x00'[0]:
				tmp80 = tmp80[:-1]
			s += struct.pack('B', len(tmp80))
			s += tmp80
			
			s += self.font_name.encode('ISO-8859-1') if PY3 else self.font_name
		
		# serialize self.text
		s += b'\x00' if self.text is None else b'\x01'
		if self.text is not None:
			tmp81 = b''
			tmp81 += struct.pack('I', len(self.text))
			while len(tmp81) and tmp81[-1] == b'\x00'[0]:
				tmp81 = tmp81[:-1]
			s += struct.pack('B', len(tmp81))
			s += tmp81
			
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
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			self.font_asset = Asset()
			offset = self.font_asset.deserialize(s, offset)
		else:
			self.font_asset = None
		
		# deserialize self.font_name
		tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp83:
			tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp85 = s[offset:offset + tmp84]
			offset += tmp84
			tmp85 += b'\x00' * (4 - tmp84)
			tmp86 = struct.unpack('I', tmp85)[0]
			
			self.font_name = s[offset:offset + tmp86].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp86]
			offset += tmp86
		else:
			self.font_name = None
		
		# deserialize self.text
		tmp87 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp87:
			tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp89 = s[offset:offset + tmp88]
			offset += tmp88
			tmp89 += b'\x00' * (4 - tmp88)
			tmp90 = struct.unpack('I', tmp89)[0]
			
			self.text = s[offset:offset + tmp90].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp90]
			offset += tmp90
		else:
			self.text = None
		
		# deserialize self.font_size
		tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp91:
			self.font_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.font_size = None
		
		# deserialize self.alignment
		tmp92 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp92:
			tmp93 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
			self.alignment = ETextAlignmentOption(tmp93)
		else:
			self.alignment = None
		
		# deserialize self.word_wrapping_ratios
		tmp94 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp94:
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
		tmp95 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp95:
			self.value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.value = None
		
		# deserialize self.max_value
		tmp96 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp96:
			self.max_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_value = None
		
		# deserialize self.min_value
		tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp97:
			self.min_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.min_value = None
		
		# deserialize self.direction
		tmp98 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp98:
			tmp99 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
			self.direction = ESliderDirection(tmp99)
		else:
			self.direction = None
		
		# deserialize self.background_color
		tmp100 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp100:
			self.background_color = Vector4()
			offset = self.background_color.deserialize(s, offset)
		else:
			self.background_color = None
		
		# deserialize self.fill_color
		tmp101 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp101:
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
		tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp102:
			self.sprite_asset = Asset()
			offset = self.sprite_asset.deserialize(s, offset)
		else:
			self.sprite_asset = None
		
		# deserialize self.color
		tmp103 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp103:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.material_asset
		tmp104 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp104:
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
		tmp105 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp105:
			self.texture_asset = Asset()
			offset = self.texture_asset.deserialize(s, offset)
		else:
			self.texture_asset = None
		
		# deserialize self.material_asset
		tmp106 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp106:
			self.material_asset = Asset()
			offset = self.material_asset.deserialize(s, offset)
		else:
			self.material_asset = None
		
		# deserialize self.color
		tmp107 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp107:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.uv_rect
		tmp108 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp108:
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
			tmp109 = b''
			tmp109 += struct.pack('I', len(self.sibling_ref_as_base_index))
			while len(tmp109) and tmp109[-1] == b'\x00'[0]:
				tmp109 = tmp109[:-1]
			s += struct.pack('B', len(tmp109))
			s += tmp109
			
			s += self.sibling_ref_as_base_index.encode('ISO-8859-1') if PY3 else self.sibling_ref_as_base_index
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.new_index
		tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp110:
			self.new_index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.new_index = None
		
		# deserialize self.goto_first
		tmp111 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp111:
			self.goto_first = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.goto_first = None
		
		# deserialize self.goto_last
		tmp112 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp112:
			self.goto_last = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.goto_last = None
		
		# deserialize self.change_index
		tmp113 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp113:
			self.change_index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.change_index = None
		
		# deserialize self.sibling_ref_as_base_index
		tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp114:
			tmp115 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp116 = s[offset:offset + tmp115]
			offset += tmp115
			tmp116 += b'\x00' * (4 - tmp115)
			tmp117 = struct.unpack('I', tmp116)[0]
			
			self.sibling_ref_as_base_index = s[offset:offset + tmp117].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp117]
			offset += tmp117
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
			tmp118 = b''
			tmp118 += struct.pack('I', len(self.type))
			while len(tmp118) and tmp118[-1] == b'\x00'[0]:
				tmp118 = tmp118[:-1]
			s += struct.pack('B', len(tmp118))
			s += tmp118
			
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
		tmp119 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp119:
			tmp120 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp121 = s[offset:offset + tmp120]
			offset += tmp120
			tmp121 += b'\x00' * (4 - tmp120)
			tmp122 = struct.unpack('I', tmp121)[0]
			
			self.type = s[offset:offset + tmp122].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp122]
			offset += tmp122
		else:
			self.type = None
		
		# deserialize self.add
		tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp123:
			self.add = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.add = None
		
		# deserialize self.is_active
		tmp124 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp124:
			self.is_active = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_active = None
		
		return offset


class ChangeSprite(BaseAction):

	@staticmethod
	def name():
		return 'ChangeSprite'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, sprite_asset=None, color=None, flip_x=None, flip_y=None, order=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, sprite_asset, color, flip_x, flip_y, order)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, sprite_asset=None, color=None, flip_x=None, flip_y=None, order=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.sprite_asset = sprite_asset
		self.color = color
		self.flip_x = flip_x
		self.flip_y = flip_y
		self.order = order
	

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
		
		# serialize self.order
		s += b'\x00' if self.order is None else b'\x01'
		if self.order is not None:
			s += struct.pack('i', self.order)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.sprite_asset
		tmp125 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp125:
			self.sprite_asset = Asset()
			offset = self.sprite_asset.deserialize(s, offset)
		else:
			self.sprite_asset = None
		
		# deserialize self.color
		tmp126 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp126:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.flip_x
		tmp127 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp127:
			self.flip_x = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.flip_x = None
		
		# deserialize self.flip_y
		tmp128 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp128:
			self.flip_y = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.flip_y = None
		
		# deserialize self.order
		tmp129 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp129:
			self.order = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.order = None
		
		return offset


class ChangeMaterial(BaseAction):

	@staticmethod
	def name():
		return 'ChangeMaterial'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, material_asset=None, index=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, material_asset, index)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, material_asset=None, index=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.material_asset = material_asset
		self.index = index
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.material_asset
		s += b'\x00' if self.material_asset is None else b'\x01'
		if self.material_asset is not None:
			s += self.material_asset.serialize()
		
		# serialize self.index
		s += b'\x00' if self.index is None else b'\x01'
		if self.index is not None:
			s += struct.pack('i', self.index)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.material_asset
		tmp130 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp130:
			self.material_asset = Asset()
			offset = self.material_asset.deserialize(s, offset)
		else:
			self.material_asset = None
		
		# deserialize self.index
		tmp131 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp131:
			self.index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.index = None
		
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
		tmp132 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp132:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.x_radius
		tmp133 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp133:
			self.x_radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x_radius = None
		
		# deserialize self.y_radius
		tmp134 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp134:
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
			tmp135 = b''
			tmp135 += struct.pack('I', len(self.vertices))
			while len(tmp135) and tmp135[-1] == b'\x00'[0]:
				tmp135 = tmp135[:-1]
			s += struct.pack('B', len(tmp135))
			s += tmp135
			
			for tmp136 in self.vertices:
				s += b'\x00' if tmp136 is None else b'\x01'
				if tmp136 is not None:
					s += tmp136.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.fill_color
		tmp137 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp137:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.vertices
		tmp138 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp138:
			tmp139 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp140 = s[offset:offset + tmp139]
			offset += tmp139
			tmp140 += b'\x00' * (4 - tmp139)
			tmp141 = struct.unpack('I', tmp140)[0]
			
			self.vertices = []
			for tmp142 in range(tmp141):
				tmp144 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp144:
					tmp143 = Vector2()
					offset = tmp143.deserialize(s, offset)
				else:
					tmp143 = None
				self.vertices.append(tmp143)
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
			tmp145 = b''
			tmp145 += struct.pack('I', len(self.vertices))
			while len(tmp145) and tmp145[-1] == b'\x00'[0]:
				tmp145 = tmp145[:-1]
			s += struct.pack('B', len(tmp145))
			s += tmp145
			
			for tmp146 in self.vertices:
				s += b'\x00' if tmp146 is None else b'\x01'
				if tmp146 is not None:
					s += tmp146.serialize()
		
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
		tmp147 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp147:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.vertices
		tmp148 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp148:
			tmp149 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp150 = s[offset:offset + tmp149]
			offset += tmp149
			tmp150 += b'\x00' * (4 - tmp149)
			tmp151 = struct.unpack('I', tmp150)[0]
			
			self.vertices = []
			for tmp152 in range(tmp151):
				tmp154 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp154:
					tmp153 = Vector2()
					offset = tmp153.deserialize(s, offset)
				else:
					tmp153 = None
				self.vertices.append(tmp153)
		else:
			self.vertices = None
		
		# deserialize self.width
		tmp155 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp155:
			self.width = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.corner_vertices
		tmp156 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp156:
			self.corner_vertices = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.corner_vertices = None
		
		# deserialize self.end_cap_vertices
		tmp157 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp157:
			self.end_cap_vertices = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.end_cap_vertices = None
		
		# deserialize self.loop
		tmp158 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp158:
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


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, range=None, spot_angle=None, color=None, intensity=None, indirect_multiplier=None, shadow_type=None, shadow_strength=None, shadow_bias=None, shadow_normal_bias=None, shadow_near_plane=None, cookie_asset=None, cookie_size=None, flare_asset=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, type, range, spot_angle, color, intensity, indirect_multiplier, shadow_type, shadow_strength, shadow_bias, shadow_normal_bias, shadow_near_plane, cookie_asset, cookie_size, flare_asset)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, range=None, spot_angle=None, color=None, intensity=None, indirect_multiplier=None, shadow_type=None, shadow_strength=None, shadow_bias=None, shadow_normal_bias=None, shadow_near_plane=None, cookie_asset=None, cookie_size=None, flare_asset=None):
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
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp159 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp159:
			tmp160 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = ELightType(tmp160)
		else:
			self.type = None
		
		# deserialize self.range
		tmp161 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp161:
			self.range = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.range = None
		
		# deserialize self.spot_angle
		tmp162 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp162:
			self.spot_angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.spot_angle = None
		
		# deserialize self.color
		tmp163 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp163:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.intensity
		tmp164 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp164:
			self.intensity = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.intensity = None
		
		# deserialize self.indirect_multiplier
		tmp165 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp165:
			self.indirect_multiplier = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.indirect_multiplier = None
		
		# deserialize self.shadow_type
		tmp166 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp166:
			tmp167 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.shadow_type = ELightShadowType(tmp167)
		else:
			self.shadow_type = None
		
		# deserialize self.shadow_strength
		tmp168 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp168:
			self.shadow_strength = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_strength = None
		
		# deserialize self.shadow_bias
		tmp169 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp169:
			self.shadow_bias = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_bias = None
		
		# deserialize self.shadow_normal_bias
		tmp170 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp170:
			self.shadow_normal_bias = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_normal_bias = None
		
		# deserialize self.shadow_near_plane
		tmp171 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp171:
			self.shadow_near_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_near_plane = None
		
		# deserialize self.cookie_asset
		tmp172 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp172:
			self.cookie_asset = Asset()
			offset = self.cookie_asset.deserialize(s, offset)
		else:
			self.cookie_asset = None
		
		# deserialize self.cookie_size
		tmp173 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp173:
			self.cookie_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.cookie_size = None
		
		# deserialize self.flare_asset
		tmp174 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp174:
			self.flare_asset = Asset()
			offset = self.flare_asset.deserialize(s, offset)
		else:
			self.flare_asset = None
		
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


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, clear_flag=None, background_color=None, is_orthographic=None, orthographic_size=None, field_of_view=None, near_clip_plane=None, far_clip_plane=None, min_position=None, max_position=None, min_rotation=None, max_rotation=None, min_zoom=None, max_zoom=None, post_process_profile_asset=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, clear_flag, background_color, is_orthographic, orthographic_size, field_of_view, near_clip_plane, far_clip_plane, min_position, max_position, min_rotation, max_rotation, min_zoom, max_zoom, post_process_profile_asset)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, clear_flag=None, background_color=None, is_orthographic=None, orthographic_size=None, field_of_view=None, near_clip_plane=None, far_clip_plane=None, min_position=None, max_position=None, min_rotation=None, max_rotation=None, min_zoom=None, max_zoom=None, post_process_profile_asset=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.clear_flag = clear_flag
		self.background_color = background_color
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
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.clear_flag
		tmp175 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp175:
			tmp176 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.clear_flag = ECameraClearFlag(tmp176)
		else:
			self.clear_flag = None
		
		# deserialize self.background_color
		tmp177 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp177:
			self.background_color = Vector4()
			offset = self.background_color.deserialize(s, offset)
		else:
			self.background_color = None
		
		# deserialize self.is_orthographic
		tmp178 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp178:
			self.is_orthographic = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_orthographic = None
		
		# deserialize self.orthographic_size
		tmp179 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp179:
			self.orthographic_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.orthographic_size = None
		
		# deserialize self.field_of_view
		tmp180 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp180:
			self.field_of_view = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.field_of_view = None
		
		# deserialize self.near_clip_plane
		tmp181 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp181:
			self.near_clip_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.near_clip_plane = None
		
		# deserialize self.far_clip_plane
		tmp182 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp182:
			self.far_clip_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.far_clip_plane = None
		
		# deserialize self.min_position
		tmp183 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp183:
			self.min_position = Vector3()
			offset = self.min_position.deserialize(s, offset)
		else:
			self.min_position = None
		
		# deserialize self.max_position
		tmp184 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp184:
			self.max_position = Vector3()
			offset = self.max_position.deserialize(s, offset)
		else:
			self.max_position = None
		
		# deserialize self.min_rotation
		tmp185 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp185:
			self.min_rotation = Vector2()
			offset = self.min_rotation.deserialize(s, offset)
		else:
			self.min_rotation = None
		
		# deserialize self.max_rotation
		tmp186 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp186:
			self.max_rotation = Vector2()
			offset = self.max_rotation.deserialize(s, offset)
		else:
			self.max_rotation = None
		
		# deserialize self.min_zoom
		tmp187 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp187:
			self.min_zoom = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.min_zoom = None
		
		# deserialize self.max_zoom
		tmp188 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp188:
			self.max_zoom = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_zoom = None
		
		# deserialize self.post_process_profile_asset
		tmp189 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp189:
			self.post_process_profile_asset = Asset()
			offset = self.post_process_profile_asset.deserialize(s, offset)
		else:
			self.post_process_profile_asset = None
		
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


class ChangeRenderSettings(object):

	@staticmethod
	def name():
		return 'ChangeRenderSettings'


	def __init__(self, ambient_equator_color=None, ambient_ground_color=None, ambient_intensity=None, ambient_light=None, ambient_mode=None, ambient_sky_color=None, custom_reflection_asset=None, default_reflection_mode=None, default_reflection_resolution=None, flare_fade_speed=None, flare_strength=None, has_fog=None, fog_mode=None, fog_color=None, fog_density=None, fog_start_distance=None, fog_end_distance=None, halo_strength=None, reflection_bounces=None, reflection_intensity=None, skybox_asset=None, subtractive_shadow_color=None, sun_ref=None, sun_child_ref=None):
		self.initialize(ambient_equator_color, ambient_ground_color, ambient_intensity, ambient_light, ambient_mode, ambient_sky_color, custom_reflection_asset, default_reflection_mode, default_reflection_resolution, flare_fade_speed, flare_strength, has_fog, fog_mode, fog_color, fog_density, fog_start_distance, fog_end_distance, halo_strength, reflection_bounces, reflection_intensity, skybox_asset, subtractive_shadow_color, sun_ref, sun_child_ref)
	

	def initialize(self, ambient_equator_color=None, ambient_ground_color=None, ambient_intensity=None, ambient_light=None, ambient_mode=None, ambient_sky_color=None, custom_reflection_asset=None, default_reflection_mode=None, default_reflection_resolution=None, flare_fade_speed=None, flare_strength=None, has_fog=None, fog_mode=None, fog_color=None, fog_density=None, fog_start_distance=None, fog_end_distance=None, halo_strength=None, reflection_bounces=None, reflection_intensity=None, skybox_asset=None, subtractive_shadow_color=None, sun_ref=None, sun_child_ref=None):
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
			tmp190 = b''
			tmp190 += struct.pack('I', len(self.sun_child_ref))
			while len(tmp190) and tmp190[-1] == b'\x00'[0]:
				tmp190 = tmp190[:-1]
			s += struct.pack('B', len(tmp190))
			s += tmp190
			
			s += self.sun_child_ref.encode('ISO-8859-1') if PY3 else self.sun_child_ref
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.ambient_equator_color
		tmp191 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp191:
			self.ambient_equator_color = Vector4()
			offset = self.ambient_equator_color.deserialize(s, offset)
		else:
			self.ambient_equator_color = None
		
		# deserialize self.ambient_ground_color
		tmp192 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp192:
			self.ambient_ground_color = Vector4()
			offset = self.ambient_ground_color.deserialize(s, offset)
		else:
			self.ambient_ground_color = None
		
		# deserialize self.ambient_intensity
		tmp193 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp193:
			self.ambient_intensity = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ambient_intensity = None
		
		# deserialize self.ambient_light
		tmp194 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp194:
			self.ambient_light = Vector4()
			offset = self.ambient_light.deserialize(s, offset)
		else:
			self.ambient_light = None
		
		# deserialize self.ambient_mode
		tmp195 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp195:
			tmp196 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.ambient_mode = EAmbientMode(tmp196)
		else:
			self.ambient_mode = None
		
		# deserialize self.ambient_sky_color
		tmp197 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp197:
			self.ambient_sky_color = Vector4()
			offset = self.ambient_sky_color.deserialize(s, offset)
		else:
			self.ambient_sky_color = None
		
		# deserialize self.custom_reflection_asset
		tmp198 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp198:
			self.custom_reflection_asset = Asset()
			offset = self.custom_reflection_asset.deserialize(s, offset)
		else:
			self.custom_reflection_asset = None
		
		# deserialize self.default_reflection_mode
		tmp199 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp199:
			tmp200 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.default_reflection_mode = EDefaultReflectionMode(tmp200)
		else:
			self.default_reflection_mode = None
		
		# deserialize self.default_reflection_resolution
		tmp201 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp201:
			self.default_reflection_resolution = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.default_reflection_resolution = None
		
		# deserialize self.flare_fade_speed
		tmp202 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp202:
			self.flare_fade_speed = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.flare_fade_speed = None
		
		# deserialize self.flare_strength
		tmp203 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp203:
			self.flare_strength = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.flare_strength = None
		
		# deserialize self.has_fog
		tmp204 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp204:
			self.has_fog = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.has_fog = None
		
		# deserialize self.fog_mode
		tmp205 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp205:
			tmp206 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.fog_mode = EFogMode(tmp206)
		else:
			self.fog_mode = None
		
		# deserialize self.fog_color
		tmp207 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp207:
			self.fog_color = Vector4()
			offset = self.fog_color.deserialize(s, offset)
		else:
			self.fog_color = None
		
		# deserialize self.fog_density
		tmp208 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp208:
			self.fog_density = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.fog_density = None
		
		# deserialize self.fog_start_distance
		tmp209 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp209:
			self.fog_start_distance = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.fog_start_distance = None
		
		# deserialize self.fog_end_distance
		tmp210 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp210:
			self.fog_end_distance = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.fog_end_distance = None
		
		# deserialize self.halo_strength
		tmp211 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp211:
			self.halo_strength = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.halo_strength = None
		
		# deserialize self.reflection_bounces
		tmp212 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp212:
			self.reflection_bounces = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.reflection_bounces = None
		
		# deserialize self.reflection_intensity
		tmp213 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp213:
			self.reflection_intensity = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.reflection_intensity = None
		
		# deserialize self.skybox_asset
		tmp214 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp214:
			self.skybox_asset = Asset()
			offset = self.skybox_asset.deserialize(s, offset)
		else:
			self.skybox_asset = None
		
		# deserialize self.subtractive_shadow_color
		tmp215 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp215:
			self.subtractive_shadow_color = Vector4()
			offset = self.subtractive_shadow_color.deserialize(s, offset)
		else:
			self.subtractive_shadow_color = None
		
		# deserialize self.sun_ref
		tmp216 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp216:
			self.sun_ref = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.sun_ref = None
		
		# deserialize self.sun_child_ref
		tmp217 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp217:
			tmp218 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp219 = s[offset:offset + tmp218]
			offset += tmp218
			tmp219 += b'\x00' * (4 - tmp218)
			tmp220 = struct.unpack('I', tmp219)[0]
			
			self.sun_child_ref = s[offset:offset + tmp220].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp220]
			offset += tmp220
		else:
			self.sun_child_ref = None
		
		return offset
