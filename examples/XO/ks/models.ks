[ECell]
_def = enum <ubyte>
	{
		Empty,
		X,
		O
	}


[World]
_def = class
board = array[3][3] <ECell>
