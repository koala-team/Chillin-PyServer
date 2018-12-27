[BaseAction]
_def = class
cycle = float
ref = int
child_ref = string
duration_cycles = float

##########################################################
##########################################################

[Vector2]
_def = class
x = float
y = float

##########################################################
##########################################################

[Vector3]
_def = class
x = float
y = float
z = float

##########################################################
##########################################################

[Vector4]
_def = class
x = float
y = float
z = float
w = float

##########################################################
##########################################################

[Asset]
_def = class
bundle_name = string
asset_name = string

##########################################################
##########################################################

[BaseCreation]
_def = class(BaseAction)
parent_ref = int
parent_child_ref = string

##########################################################
##########################################################

[CreateEmptyGameObject]
_def = class(BaseCreation)

##########################################################
##########################################################

[InstantiateBundleAsset]
_def = class(BaseCreation)
asset = Asset

##########################################################
##########################################################

[EBasicObjectType]
_def = enum <byte>
	{
		Sprite,
		AudioSource,
		Ellipse2D,
		Polygon2D,
		Line,
		Light
	}

[CreateBasicObject]
_def = class(BaseCreation)
type = EBasicObjectType

##########################################################
##########################################################

[EUIElementType]
_def = enum <byte>
	{
		Canvas,
		Text,
		Slider,
		RawImage,
		Panel
	}

[CreateUIElement]
_def = class(BaseCreation)
type = EUIElementType

##########################################################
##########################################################

[Destroy]
_def = class(BaseAction)

##########################################################
##########################################################

[ChangeVisibility]
_def = class(BaseAction)
is_visible = boolean

##########################################################
##########################################################

[ChangeTransform]
_def = class(BaseAction)
position = Vector3
rotation = Vector3
scale = Vector3

##########################################################
##########################################################

[EAnimatorVariableType]
_def = enum <byte>
    {
        Int,
		Float,
		Bool,
		Trigger
    }

[ChangeAnimatorVariable]
_def = class(BaseAction)
var_name = string
var_type = EAnimatorVariableType
int_value = int
float_value = float
bool_value = boolean

##########################################################
##########################################################

[ChangeAnimatorState]
_def = class(BaseAction)
state_name = string
layer = int
normalized_time = float

##########################################################
##########################################################

[ChangeAudioSource]
_def = class(BaseAction)
audio_clip_asset = Asset
time = float
mute = boolean
loop = boolean
priority = int
volume = float
spatial_blend = float
play = boolean
stop = boolean

##########################################################
##########################################################

[ChangeRectTransform]
_def = class(BaseAction)
position = Vector3
rotation = Vector3
scale = Vector3
pivot = Vector2
anchor_min = Vector2
anchor_max = Vector2
size = Vector2

##########################################################
##########################################################

[ETextAlignmentOption]
_def = enum <short>
	{
		TopLeft (257),
		Top (258),
		TopRight (260),
		TopJustified (264),
		TopFlush (272),
		TopGeoAligned (288),
		Left (513),
		Center (514),
		Right (516),
		Justified (520),
		Flush (528),
		CenterGeoAligned (544),
		BottomLeft (1025),
		Bottom (1026),
		BottomRight (1028),
		BottomJustified (1032),
		BottomFlush (1040),
		BottomGeoAligned (1056),
		BaselineLeft (2049),
		Baseline (2050),
		BaselineRight (2052),
		BaselineJustified (2056),
		BaselineFlush (2064),
		BaselineGeoAligned (2080),
		MidlineLeft (4097),
		Midline (4098),
		MidlineRight (4100),
		MidlineJustified (4104),
		MidlineFlush (4112),
		MidlineGeoAligned (4128),
		CaplineLeft (8193),
		Capline (8194),
		CaplineRight (8196),
		CaplineJustified (8200),
		CaplineFlush (8208),
		CaplineGeoAligned (8224)
	}

[ChangeText]
_def = class(BaseAction)
font_asset = Asset
font_name = string
text = string
font_size = float
alignment = ETextAlignmentOption
word_wrapping_ratios = float

##########################################################
##########################################################

[ESliderDirection]
_def = enum <short>
	{
		LeftToRight (0),
		RightToLeft (1),
		BottomToTop (2),
		TopToBottom (3)
	}

[ChangeSlider]
_def = class(BaseAction)
value = float
max_value = float
min_value = float
direction = ESliderDirection
background_color = Vector4
fill_color = Vector4

##########################################################
##########################################################

[ChangeRawImage]
_def = class(BaseAction)
texture_asset = Asset
material_asset = Asset
color = Vector4
uv_rect = Vector4

##########################################################
##########################################################

[ChangeSiblingOrder]
_def = class(BaseAction)
new_index = int
goto_first = boolean
goto_last = boolean
change_index = int
sibling_ref_as_base_index = string

##########################################################
##########################################################

[ManageComponent]
_def = class(BaseAction)
type = string
add = boolean
is_active = boolean

##########################################################
##########################################################

[ChangeSprite]
_def = class(BaseAction)
sprite_asset = Asset
color = Vector4
flip_x = boolean
flip_y = boolean
order = int

##########################################################
##########################################################

[ChangeMaterial]
_def = class(BaseAction)
material_asset = Asset
index = int

##########################################################
##########################################################

[ChangeEllipse2D]
_def = class(BaseAction)
fill_color = Vector4
x_radius = float
y_radius = float

##########################################################
##########################################################

[ChangePolygon2D]
_def = class(BaseAction)
fill_color = Vector4
vertices = list<Vector2>

##########################################################
##########################################################

[ChangeLine]
_def = class(BaseAction)
fill_color = Vector4
vertices = list<Vector2>
width = float
corner_vertices = int
end_cap_vertices = int
loop = boolean

##########################################################
##########################################################

[ELightType]
_def = enum <byte>
	{
		Spot (0),
		Directional (1),
		Point (2)
	}

[ELightShadowType]
_def = enum <byte>
	{
		Disabled (0),
		Hard (1),
		Soft (2)
	}

[ChangeLight]
_def = class(BaseAction)
type = ELightType
range = float
spot_angle = float
color = Vector4
intensity = float
indirect_multiplier = float
shadow_type = ELightShadowType
shadow_strength = float
shadow_bias = float
shadow_normal_bias = float
shadow_near_plane = float
cookie_asset = Asset
cookie_size = float
flare_asset = Asset

##########################################################
##########################################################

[ECameraClearFlag]
_def = enum <byte>
	{
		Skybox (1),
		SolidColor (2),
		Depth (3),
		Nothing (4)
	}

[ChangeCamera]
_def = class(BaseAction)
clear_flag = ECameraClearFlag
background_color = Vector4
is_orthographic = boolean
orthographic_size = float
field_of_view = float
near_clip_plane = float
far_clip_plane = float
min_boundary = Vector3
max_boundary = Vector3

##########################################################
##########################################################

[StoreBundleData]
_def = class
bundle_name = string
bundle_data = string

##########################################################
##########################################################

[ClearScene]
_def = class(BaseAction)

##########################################################
##########################################################

[EndCycle]
_def = class
