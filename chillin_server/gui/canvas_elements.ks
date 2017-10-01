[Color]
_def = class
r = ubyte
g = ubyte
b = ubyte
a = ubyte


[Circle]
_def = class
x = short
y = short
radius = ushort
color = Color
stroke_width = ushort
stroke_color = Color


[Ellipse]
_def = class
x = short
y = short
radius_x = ushort
radius_y = ushort
color = Color
angle = float
stroke_width = ushort
stroke_color = Color


[Rect]
_def = class
x = short
y = short
width = ushort
height = ushort
color = Color
angle = float
center_origin = boolean
stroke_width = ushort
stroke_color = Color


[Line]
_def = class
x1 = short
y1 = short
x2 = short
y2 = short
color = Color
stroke_width = ushort
angle = float


[Polygon]
_def = class
x = list <short>
y = list <short>
color = Color
offset_left = short
offset_top = short
angle = float
center_origin = boolean
stroke_width = ushort
stroke_color = Color


[ScaleType]
_def = enum <ubyte> {NoScale, ScaleToWidth, ScaleToHeight, ScaleX, ScaleY}

[Image]
_def = class
image_name = string
x = short
y = short
scale_type = ScaleType
scale_value = ushort
angle = float
center_origin = boolean
stroke_width = ushort
stroke_color = Color


[FontStyle]
_def = enum <ubyte> {Normal, Bold, Italic}

[Text]
_def = class
text = string
x = short
y = short
color = Color
font_size = ushort
font_style = FontStyle
font = string
background_color = Color
angle = float
center_origin = boolean
stroke_width = ushort
stroke_color = Color
