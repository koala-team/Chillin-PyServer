[ECellType]
_def = enum <ubyte>
	{
		Empty,
		DestroyableBlock,
		UndestroyableBlock
	}

[Cell]
_def = class
type = ECellType

[Bomberman]
_def = class
x = ubyte
y = ubyte
bomb_level = ubyte
is_dead = boolean

[Bomb]
_def = class
x = ubyte
y = ubyte
timer = ubyte
level = ubyte

[Explosion]
_def = class
x = ubyte
y = ubyte

[World]
_def = class
board = list<list<Cell>>
bombermans = map<string, Bomberman>
bombs = map<string, list<Bomb>>
explosions = list<Explosion>
explosion_radiuses = list<uint>
