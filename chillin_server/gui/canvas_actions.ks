[ResizeCanvas]
_def = class
width = ushort
height = ushort


[ClearCanvas]
_def = class


[CreateElement]
_def = class
ref = uint
element_type = string
element_payload = string


[EditElement]
_def = class
ref = uint
element_type = string
element_payload = string


[DeleteElement]
_def = class
ref = uint


[StoreImageData]
_def = class
image_name = string
image_data = string


[BringToFront]
_def = class
ref = uint
target_ref = uint


[SendToBack]
_def = class
ref = uint
target_ref = uint
