# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Color(object):

	@staticmethod
	def name():
		return 'Color'


	def __init__(self, r=None, g=None, b=None, a=None):
		self.initialize(r, g, b, a)
	

	def initialize(self, r=None, g=None, b=None, a=None):
		self.r = r
		self.g = g
		self.b = b
		self.a = a
	

	def serialize(self):
		s = b''
		
		# serialize self.r
		s += b'\x00' if self.r is None else b'\x01'
		if self.r is not None:
			s += struct.pack('B', self.r)
		
		# serialize self.g
		s += b'\x00' if self.g is None else b'\x01'
		if self.g is not None:
			s += struct.pack('B', self.g)
		
		# serialize self.b
		s += b'\x00' if self.b is None else b'\x01'
		if self.b is not None:
			s += struct.pack('B', self.b)
		
		# serialize self.a
		s += b'\x00' if self.a is None else b'\x01'
		if self.a is not None:
			s += struct.pack('B', self.a)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.r
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.r = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.r = None
		
		# deserialize self.g
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.g = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.g = None
		
		# deserialize self.b
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.b = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.b = None
		
		# deserialize self.a
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.a = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.a = None
		
		return offset


class Circle(object):

	@staticmethod
	def name():
		return 'Circle'


	def __init__(self, x=None, y=None, radius=None, color=None, stroke_width=None, stroke_color=None):
		self.initialize(x, y, radius, color, stroke_width, stroke_color)
	

	def initialize(self, x=None, y=None, radius=None, color=None, stroke_width=None, stroke_color=None):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.stroke_width = stroke_width
		self.stroke_color = stroke_color
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('h', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('h', self.y)
		
		# serialize self.radius
		s += b'\x00' if self.radius is None else b'\x01'
		if self.radius is not None:
			s += struct.pack('H', self.radius)
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.stroke_width
		s += b'\x00' if self.stroke_width is None else b'\x01'
		if self.stroke_width is not None:
			s += struct.pack('H', self.stroke_width)
		
		# serialize self.stroke_color
		s += b'\x00' if self.stroke_color is None else b'\x01'
		if self.stroke_color is not None:
			s += self.stroke_color.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.x = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.x = None
		
		# deserialize self.y
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.y = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.y = None
		
		# deserialize self.radius
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.radius = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.radius = None
		
		# deserialize self.color
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.color = Color()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.stroke_width
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.stroke_width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.stroke_width = None
		
		# deserialize self.stroke_color
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			self.stroke_color = Color()
			offset = self.stroke_color.deserialize(s, offset)
		else:
			self.stroke_color = None
		
		return offset


class Ellipse(object):

	@staticmethod
	def name():
		return 'Ellipse'


	def __init__(self, x=None, y=None, radius_x=None, radius_y=None, color=None, angle=None, stroke_width=None, stroke_color=None):
		self.initialize(x, y, radius_x, radius_y, color, angle, stroke_width, stroke_color)
	

	def initialize(self, x=None, y=None, radius_x=None, radius_y=None, color=None, angle=None, stroke_width=None, stroke_color=None):
		self.x = x
		self.y = y
		self.radius_x = radius_x
		self.radius_y = radius_y
		self.color = color
		self.angle = angle
		self.stroke_width = stroke_width
		self.stroke_color = stroke_color
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('h', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('h', self.y)
		
		# serialize self.radius_x
		s += b'\x00' if self.radius_x is None else b'\x01'
		if self.radius_x is not None:
			s += struct.pack('H', self.radius_x)
		
		# serialize self.radius_y
		s += b'\x00' if self.radius_y is None else b'\x01'
		if self.radius_y is not None:
			s += struct.pack('H', self.radius_y)
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		# serialize self.stroke_width
		s += b'\x00' if self.stroke_width is None else b'\x01'
		if self.stroke_width is not None:
			s += struct.pack('H', self.stroke_width)
		
		# serialize self.stroke_color
		s += b'\x00' if self.stroke_color is None else b'\x01'
		if self.stroke_color is not None:
			s += self.stroke_color.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.x = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.x = None
		
		# deserialize self.y
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.y = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.y = None
		
		# deserialize self.radius_x
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			self.radius_x = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.radius_x = None
		
		# deserialize self.radius_y
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.radius_y = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.radius_y = None
		
		# deserialize self.color
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.color = Color()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.angle
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		# deserialize self.stroke_width
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			self.stroke_width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.stroke_width = None
		
		# deserialize self.stroke_color
		tmp17 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp17:
			self.stroke_color = Color()
			offset = self.stroke_color.deserialize(s, offset)
		else:
			self.stroke_color = None
		
		return offset


class Rect(object):

	@staticmethod
	def name():
		return 'Rect'


	def __init__(self, x=None, y=None, width=None, height=None, color=None, angle=None, center_origin=None, stroke_width=None, stroke_color=None):
		self.initialize(x, y, width, height, color, angle, center_origin, stroke_width, stroke_color)
	

	def initialize(self, x=None, y=None, width=None, height=None, color=None, angle=None, center_origin=None, stroke_width=None, stroke_color=None):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.angle = angle
		self.center_origin = center_origin
		self.stroke_width = stroke_width
		self.stroke_color = stroke_color
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('h', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('h', self.y)
		
		# serialize self.width
		s += b'\x00' if self.width is None else b'\x01'
		if self.width is not None:
			s += struct.pack('H', self.width)
		
		# serialize self.height
		s += b'\x00' if self.height is None else b'\x01'
		if self.height is not None:
			s += struct.pack('H', self.height)
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		# serialize self.center_origin
		s += b'\x00' if self.center_origin is None else b'\x01'
		if self.center_origin is not None:
			s += struct.pack('?', self.center_origin)
		
		# serialize self.stroke_width
		s += b'\x00' if self.stroke_width is None else b'\x01'
		if self.stroke_width is not None:
			s += struct.pack('H', self.stroke_width)
		
		# serialize self.stroke_color
		s += b'\x00' if self.stroke_color is None else b'\x01'
		if self.stroke_color is not None:
			s += self.stroke_color.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp18 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp18:
			self.x = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.x = None
		
		# deserialize self.y
		tmp19 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp19:
			self.y = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.y = None
		
		# deserialize self.width
		tmp20 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp20:
			self.width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.width = None
		
		# deserialize self.height
		tmp21 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp21:
			self.height = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.height = None
		
		# deserialize self.color
		tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp22:
			self.color = Color()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.angle
		tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp23:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		# deserialize self.center_origin
		tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp24:
			self.center_origin = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.center_origin = None
		
		# deserialize self.stroke_width
		tmp25 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp25:
			self.stroke_width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.stroke_width = None
		
		# deserialize self.stroke_color
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
			self.stroke_color = Color()
			offset = self.stroke_color.deserialize(s, offset)
		else:
			self.stroke_color = None
		
		return offset


class Line(object):

	@staticmethod
	def name():
		return 'Line'


	def __init__(self, x1=None, y1=None, x2=None, y2=None, color=None, stroke_width=None, angle=None):
		self.initialize(x1, y1, x2, y2, color, stroke_width, angle)
	

	def initialize(self, x1=None, y1=None, x2=None, y2=None, color=None, stroke_width=None, angle=None):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.color = color
		self.stroke_width = stroke_width
		self.angle = angle
	

	def serialize(self):
		s = b''
		
		# serialize self.x1
		s += b'\x00' if self.x1 is None else b'\x01'
		if self.x1 is not None:
			s += struct.pack('h', self.x1)
		
		# serialize self.y1
		s += b'\x00' if self.y1 is None else b'\x01'
		if self.y1 is not None:
			s += struct.pack('h', self.y1)
		
		# serialize self.x2
		s += b'\x00' if self.x2 is None else b'\x01'
		if self.x2 is not None:
			s += struct.pack('h', self.x2)
		
		# serialize self.y2
		s += b'\x00' if self.y2 is None else b'\x01'
		if self.y2 is not None:
			s += struct.pack('h', self.y2)
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.stroke_width
		s += b'\x00' if self.stroke_width is None else b'\x01'
		if self.stroke_width is not None:
			s += struct.pack('H', self.stroke_width)
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x1
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.x1 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.x1 = None
		
		# deserialize self.y1
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			self.y1 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.y1 = None
		
		# deserialize self.x2
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			self.x2 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.x2 = None
		
		# deserialize self.y2
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			self.y2 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.y2 = None
		
		# deserialize self.color
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			self.color = Color()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.stroke_width
		tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp32:
			self.stroke_width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.stroke_width = None
		
		# deserialize self.angle
		tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp33:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		return offset


class Polygon(object):

	@staticmethod
	def name():
		return 'Polygon'


	def __init__(self, x=None, y=None, color=None, offset_left=None, offset_top=None, angle=None, center_origin=None, stroke_width=None, stroke_color=None):
		self.initialize(x, y, color, offset_left, offset_top, angle, center_origin, stroke_width, stroke_color)
	

	def initialize(self, x=None, y=None, color=None, offset_left=None, offset_top=None, angle=None, center_origin=None, stroke_width=None, stroke_color=None):
		self.x = x
		self.y = y
		self.color = color
		self.offset_left = offset_left
		self.offset_top = offset_top
		self.angle = angle
		self.center_origin = center_origin
		self.stroke_width = stroke_width
		self.stroke_color = stroke_color
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			tmp34 = b''
			tmp34 += struct.pack('I', len(self.x))
			while len(tmp34) and tmp34[-1] == b'\x00'[0]:
				tmp34 = tmp34[:-1]
			s += struct.pack('B', len(tmp34))
			s += tmp34
			
			for tmp35 in self.x:
				s += b'\x00' if tmp35 is None else b'\x01'
				if tmp35 is not None:
					s += struct.pack('h', tmp35)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			tmp36 = b''
			tmp36 += struct.pack('I', len(self.y))
			while len(tmp36) and tmp36[-1] == b'\x00'[0]:
				tmp36 = tmp36[:-1]
			s += struct.pack('B', len(tmp36))
			s += tmp36
			
			for tmp37 in self.y:
				s += b'\x00' if tmp37 is None else b'\x01'
				if tmp37 is not None:
					s += struct.pack('h', tmp37)
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.offset_left
		s += b'\x00' if self.offset_left is None else b'\x01'
		if self.offset_left is not None:
			s += struct.pack('h', self.offset_left)
		
		# serialize self.offset_top
		s += b'\x00' if self.offset_top is None else b'\x01'
		if self.offset_top is not None:
			s += struct.pack('h', self.offset_top)
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		# serialize self.center_origin
		s += b'\x00' if self.center_origin is None else b'\x01'
		if self.center_origin is not None:
			s += struct.pack('?', self.center_origin)
		
		# serialize self.stroke_width
		s += b'\x00' if self.stroke_width is None else b'\x01'
		if self.stroke_width is not None:
			s += struct.pack('H', self.stroke_width)
		
		# serialize self.stroke_color
		s += b'\x00' if self.stroke_color is None else b'\x01'
		if self.stroke_color is not None:
			s += self.stroke_color.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp40 = s[offset:offset + tmp39]
			offset += tmp39
			tmp40 += b'\x00' * (4 - tmp39)
			tmp41 = struct.unpack('I', tmp40)[0]
			
			self.x = []
			for tmp42 in range(tmp41):
				tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp44:
					tmp43 = struct.unpack('h', s[offset:offset + 2])[0]
					offset += 2
				else:
					tmp43 = None
				self.x.append(tmp43)
		else:
			self.x = None
		
		# deserialize self.y
		tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp45:
			tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp47 = s[offset:offset + tmp46]
			offset += tmp46
			tmp47 += b'\x00' * (4 - tmp46)
			tmp48 = struct.unpack('I', tmp47)[0]
			
			self.y = []
			for tmp49 in range(tmp48):
				tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp51:
					tmp50 = struct.unpack('h', s[offset:offset + 2])[0]
					offset += 2
				else:
					tmp50 = None
				self.y.append(tmp50)
		else:
			self.y = None
		
		# deserialize self.color
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			self.color = Color()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.offset_left
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			self.offset_left = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.offset_left = None
		
		# deserialize self.offset_top
		tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp54:
			self.offset_top = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.offset_top = None
		
		# deserialize self.angle
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		# deserialize self.center_origin
		tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp56:
			self.center_origin = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.center_origin = None
		
		# deserialize self.stroke_width
		tmp57 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp57:
			self.stroke_width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.stroke_width = None
		
		# deserialize self.stroke_color
		tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp58:
			self.stroke_color = Color()
			offset = self.stroke_color.deserialize(s, offset)
		else:
			self.stroke_color = None
		
		return offset


class ScaleType(Enum):
	NoScale = 0
	ScaleToWidth = 1
	ScaleToHeight = 2
	ScaleX = 3
	ScaleY = 4


class Image(object):

	@staticmethod
	def name():
		return 'Image'


	def __init__(self, image_name=None, x=None, y=None, scale_type=None, scale_value=None, angle=None, center_origin=None, stroke_width=None, stroke_color=None):
		self.initialize(image_name, x, y, scale_type, scale_value, angle, center_origin, stroke_width, stroke_color)
	

	def initialize(self, image_name=None, x=None, y=None, scale_type=None, scale_value=None, angle=None, center_origin=None, stroke_width=None, stroke_color=None):
		self.image_name = image_name
		self.x = x
		self.y = y
		self.scale_type = scale_type
		self.scale_value = scale_value
		self.angle = angle
		self.center_origin = center_origin
		self.stroke_width = stroke_width
		self.stroke_color = stroke_color
	

	def serialize(self):
		s = b''
		
		# serialize self.image_name
		s += b'\x00' if self.image_name is None else b'\x01'
		if self.image_name is not None:
			tmp59 = b''
			tmp59 += struct.pack('I', len(self.image_name))
			while len(tmp59) and tmp59[-1] == b'\x00'[0]:
				tmp59 = tmp59[:-1]
			s += struct.pack('B', len(tmp59))
			s += tmp59
			
			s += self.image_name.encode('ISO-8859-1') if PY3 else self.image_name
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('h', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('h', self.y)
		
		# serialize self.scale_type
		s += b'\x00' if self.scale_type is None else b'\x01'
		if self.scale_type is not None:
			s += struct.pack('B', self.scale_type.value)
		
		# serialize self.scale_value
		s += b'\x00' if self.scale_value is None else b'\x01'
		if self.scale_value is not None:
			s += struct.pack('H', self.scale_value)
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		# serialize self.center_origin
		s += b'\x00' if self.center_origin is None else b'\x01'
		if self.center_origin is not None:
			s += struct.pack('?', self.center_origin)
		
		# serialize self.stroke_width
		s += b'\x00' if self.stroke_width is None else b'\x01'
		if self.stroke_width is not None:
			s += struct.pack('H', self.stroke_width)
		
		# serialize self.stroke_color
		s += b'\x00' if self.stroke_color is None else b'\x01'
		if self.stroke_color is not None:
			s += self.stroke_color.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.image_name
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp62 = s[offset:offset + tmp61]
			offset += tmp61
			tmp62 += b'\x00' * (4 - tmp61)
			tmp63 = struct.unpack('I', tmp62)[0]
			
			self.image_name = s[offset:offset + tmp63].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp63]
			offset += tmp63
		else:
			self.image_name = None
		
		# deserialize self.x
		tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp64:
			self.x = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.x = None
		
		# deserialize self.y
		tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp65:
			self.y = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.y = None
		
		# deserialize self.scale_type
		tmp66 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp66:
			tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			self.scale_type = ScaleType(tmp67)
		else:
			self.scale_type = None
		
		# deserialize self.scale_value
		tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp68:
			self.scale_value = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.scale_value = None
		
		# deserialize self.angle
		tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp69:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		# deserialize self.center_origin
		tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp70:
			self.center_origin = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.center_origin = None
		
		# deserialize self.stroke_width
		tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp71:
			self.stroke_width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.stroke_width = None
		
		# deserialize self.stroke_color
		tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp72:
			self.stroke_color = Color()
			offset = self.stroke_color.deserialize(s, offset)
		else:
			self.stroke_color = None
		
		return offset


class FontStyle(Enum):
	Normal = 0
	Bold = 1
	Italic = 2


class Text(object):

	@staticmethod
	def name():
		return 'Text'


	def __init__(self, text=None, x=None, y=None, color=None, font_size=None, font_style=None, font=None, background_color=None, angle=None, center_origin=None, stroke_width=None, stroke_color=None):
		self.initialize(text, x, y, color, font_size, font_style, font, background_color, angle, center_origin, stroke_width, stroke_color)
	

	def initialize(self, text=None, x=None, y=None, color=None, font_size=None, font_style=None, font=None, background_color=None, angle=None, center_origin=None, stroke_width=None, stroke_color=None):
		self.text = text
		self.x = x
		self.y = y
		self.color = color
		self.font_size = font_size
		self.font_style = font_style
		self.font = font
		self.background_color = background_color
		self.angle = angle
		self.center_origin = center_origin
		self.stroke_width = stroke_width
		self.stroke_color = stroke_color
	

	def serialize(self):
		s = b''
		
		# serialize self.text
		s += b'\x00' if self.text is None else b'\x01'
		if self.text is not None:
			tmp73 = b''
			tmp73 += struct.pack('I', len(self.text))
			while len(tmp73) and tmp73[-1] == b'\x00'[0]:
				tmp73 = tmp73[:-1]
			s += struct.pack('B', len(tmp73))
			s += tmp73
			
			s += self.text.encode('ISO-8859-1') if PY3 else self.text
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('h', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('h', self.y)
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.font_size
		s += b'\x00' if self.font_size is None else b'\x01'
		if self.font_size is not None:
			s += struct.pack('H', self.font_size)
		
		# serialize self.font_style
		s += b'\x00' if self.font_style is None else b'\x01'
		if self.font_style is not None:
			s += struct.pack('B', self.font_style.value)
		
		# serialize self.font
		s += b'\x00' if self.font is None else b'\x01'
		if self.font is not None:
			tmp74 = b''
			tmp74 += struct.pack('I', len(self.font))
			while len(tmp74) and tmp74[-1] == b'\x00'[0]:
				tmp74 = tmp74[:-1]
			s += struct.pack('B', len(tmp74))
			s += tmp74
			
			s += self.font.encode('ISO-8859-1') if PY3 else self.font
		
		# serialize self.background_color
		s += b'\x00' if self.background_color is None else b'\x01'
		if self.background_color is not None:
			s += self.background_color.serialize()
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		# serialize self.center_origin
		s += b'\x00' if self.center_origin is None else b'\x01'
		if self.center_origin is not None:
			s += struct.pack('?', self.center_origin)
		
		# serialize self.stroke_width
		s += b'\x00' if self.stroke_width is None else b'\x01'
		if self.stroke_width is not None:
			s += struct.pack('H', self.stroke_width)
		
		# serialize self.stroke_color
		s += b'\x00' if self.stroke_color is None else b'\x01'
		if self.stroke_color is not None:
			s += self.stroke_color.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.text
		tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp75:
			tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp77 = s[offset:offset + tmp76]
			offset += tmp76
			tmp77 += b'\x00' * (4 - tmp76)
			tmp78 = struct.unpack('I', tmp77)[0]
			
			self.text = s[offset:offset + tmp78].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp78]
			offset += tmp78
		else:
			self.text = None
		
		# deserialize self.x
		tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp79:
			self.x = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.x = None
		
		# deserialize self.y
		tmp80 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp80:
			self.y = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.y = None
		
		# deserialize self.color
		tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp81:
			self.color = Color()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.font_size
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			self.font_size = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.font_size = None
		
		# deserialize self.font_style
		tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp83:
			tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			self.font_style = FontStyle(tmp84)
		else:
			self.font_style = None
		
		# deserialize self.font
		tmp85 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp85:
			tmp86 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp87 = s[offset:offset + tmp86]
			offset += tmp86
			tmp87 += b'\x00' * (4 - tmp86)
			tmp88 = struct.unpack('I', tmp87)[0]
			
			self.font = s[offset:offset + tmp88].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp88]
			offset += tmp88
		else:
			self.font = None
		
		# deserialize self.background_color
		tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp89:
			self.background_color = Color()
			offset = self.background_color.deserialize(s, offset)
		else:
			self.background_color = None
		
		# deserialize self.angle
		tmp90 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp90:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		# deserialize self.center_origin
		tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp91:
			self.center_origin = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.center_origin = None
		
		# deserialize self.stroke_width
		tmp92 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp92:
			self.stroke_width = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.stroke_width = None
		
		# deserialize self.stroke_color
		tmp93 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp93:
			self.stroke_color = Color()
			offset = self.stroke_color.deserialize(s, offset)
		else:
			self.stroke_color = None
		
		return offset
