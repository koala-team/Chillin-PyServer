# -*- coding: utf-8 -*-

# python imports
import operator
import os
import random

# chillin imports
from chillin_server import RealtimeGameHandler
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ks.models import World, Cell, ECellType, Bomberman, Bomb, Explosion
from ks.commands import EDir


class MyRealtimeGameHandler(RealtimeGameHandler):

    def on_recv_command(self, side_name, agent_name, command_type, command):
        self.commands[side_name] = command
        print('command: %s %s' % (side_name, command_type, ))


    def on_initialize(self):
        print('initialize')

        # read map
        maps_dir = os.path.abspath(self.config['maps_dir'])
        all_maps = [f for f in os.listdir(maps_dir) if os.path.isfile(os.path.join(maps_dir, f))]
        selected_map = os.path.join(maps_dir, all_maps[random.randrange(0, len(all_maps))])
        map_rows = open(selected_map, 'r').read().split('\n')
        self.num_of_rows = len(map_rows)
        self.num_of_cols = len(map_rows[0])

        # Initialize world
        self.world = World(bombermans={}, bombs={side: [] for side in self.sides}, explosions=[])
        self.world.explosion_radiuses = [0, 3, 7, max(self.num_of_rows, self.num_of_cols)]
        self.world.board = [[Cell(type=ECellType.Empty) for _ in range(self.num_of_cols)] for _ in range(self.num_of_rows)]

        # #: undestroyable block, *: destroyable block, number: ith player
        for y, row in enumerate(map_rows):
            for x, col in enumerate(row):
                if col == ' ':
                    continue
                elif col == '#':
                    self.world.board[y][x] = Cell(type=ECellType.UndestroyableBlock)
                elif col == '*':
                    self.world.board[y][x] = Cell(type=ECellType.DestroyableBlock)
                elif len(col) == 1 and ord('1') <= ord(col) <= ord('2'):
                    self.world.bombermans['player' + col] = Bomberman(x=x, y=y, bomb_level=1, is_dead=False)

        # Initialize other variables
        self.commands = {}
        self.alives_side = [side for side in self.sides]
        self.steps = {
            EDir.Top.name: (0, -1),
            EDir.Right.name: (1, 0),
            EDir.Bottom.name: (0, 1),
            EDir.Left.name: (-1, 0),
        }
        self.angles = {
            EDir.Top.name: 90,
            EDir.Right.name: 0,
            EDir.Bottom.name: 270,
            EDir.Left.name: 180,
        }


    def on_initialize_gui(self):
        print('initialize gui')

        # resize canvas based on map
        self.canvas.resize_canvas(self.num_of_cols * self.config['cell_size'], self.num_of_rows * self.config['cell_size'])

        # Draw cells
        background_ref = self.canvas.create_image('Background', 0, 0)
        self.canvas.edit_image(background_ref, scale_type=ScaleType.ScaleX, scale_value=self.num_of_cols * 100)
        self.canvas.edit_image(background_ref, scale_type=ScaleType.ScaleY, scale_value=self.num_of_rows * 100)
        for y in range(self.num_of_rows):
            for x in range(self.num_of_cols):
                cell = self.world.board[y][x]

                if cell.type == ECellType.DestroyableBlock:
                    cell.ref = self.canvas.create_image('DestroyableBlock', x * self.config['cell_size'], y * self.config['cell_size'])
                elif cell.type == ECellType.UndestroyableBlock:
                    self.canvas.create_image('UndestroyableBlock', x * self.config['cell_size'], y * self.config['cell_size'])

        # Draw Bombermans
        for side in self.world.bombermans:
            bomberman = self.world.bombermans[side]
            self.canvas.create_image('Bomberman' + side[-1:], bomberman.x * self.config['cell_size'], bomberman.y * self.config['cell_size'], custom_ref=side)

        # Apply actions
        self.canvas.apply_actions()


    def on_process_cycle(self):
        print('process: %s' % (self.current_cycle))

        # Remove previous explosions
        for explosion in self.world.explosions:
            self.canvas.delete_element(explosion.ref)
        self.world.explosions = []

        # Update bombs' status
        for side in self.sides:
            index_for_remove = []
            for i in range(len(self.world.bombs[side])):
                bomb = self.world.bombs[side][i]
                self.canvas.delete_element(bomb.ref)
                if bomb.timer > 1:
                    bomb.timer -= 1
                    bomb.ref = self.canvas.create_image('Bomb' + str(bomb.timer), bomb.x * self.config['cell_size'], bomb.y * self.config['cell_size'])
                else:
                    # Remove bomb and add explosion
                    index_for_remove.append(i)
                    # Draw explosions
                    # draw the base explosion
                    self._create_explosion('ExplosionBase' + str(bomb.level), bomb.x, bomb.y)
                    # draw follows
                    radius = self.world.explosion_radiuses[bomb.level]
                    for direction in self.steps:
                        pos = (bomb.x, bomb.y)
                        step = self.steps[direction]
                        angle = self.angles[direction]
                        for r in range(radius):
                            image_base_name = 'ExplosionEnd' if r == radius - 1 else 'ExplosionPath'
                            pos = self._tuple_sum(pos, step)
                            cell = self.world.board[pos[1]][pos[0]]
                            if cell.type in [ECellType.DestroyableBlock, ECellType.UndestroyableBlock]:
                                if cell.type == ECellType.DestroyableBlock:
                                    # if destroyable, destroy the block
                                    self.canvas.delete_element(cell.ref)
                                    self._create_explosion(image_base_name + str(bomb.level), pos[0], pos[1], angle)
                                break # hit the block, stop the explosion in this direction
                            elif cell.type == ECellType.Empty:
                                self._create_explosion(image_base_name + str(bomb.level), pos[0], pos[1], angle)

            # remove exploded bombs
            for i in index_for_remove:
                del self.world.bombs[side][i]

        # Read commands
        new_positions = {} # Save new positions

        for side in self.commands:
            if not side in self.alives_side: # check bomberman is alive
                continue

            bomberman = self.world.bombermans[side]
            command = self.commands[side]
            if command.name() == 'Bomb':
                if len(self.world.bombs[side]) < self.config['max_bombs']:
                    # Check no other bomb in this cell
                    for bomb in [item for bombs in self.world.bombs.values() for item in bombs]:
                        if bomb.x == bomberman.x and bomb.y == bomberman.y:
                            break
                    else:
                        bomb = Bomb(timer=self.config['bomb_init_timer'], level=bomberman.bomb_level)
                        bomb.x = bomberman.x
                        bomb.y = bomberman.y
                        bomb.ref = self.canvas.create_image('Bomb' + str(bomb.timer), bomb.x * self.config['cell_size'], bomb.y * self.config['cell_size'])
                        self.world.bombs[side].append(bomb)
            elif command.name() == 'Move':
                step = self.steps[command.direction.name]
                pos = (bomberman.x, bomberman.y)
                new_pos = self._tuple_sum(pos, step)
                # check dont move to block
                if self.world.board[new_pos[1]][new_pos[0]].type == ECellType.Empty:
                    # check dont move to another alive bomberman
                    for other_side in self.alives_side:
                        if other_side != side: # avoid check with yourself
                            other_bomberman = self.world.bombermans[other_side]
                            if new_pos[0] == other_bomberman.x and new_pos[1] == other_bomberman.y:
                                break # can't move
                    else:
                        new_positions[side] = new_pos

        # Check for no intersection in new pos
        for side in new_positions:
            pos = new_positions[side]
            for other_side in new_positions:
                if side != other_side:
                    other_pos = new_positions[other_side]
                    if pos[0] == other_pos[0] and pos[1] == other_pos[1]:
                        break
            else:
                bomberman = self.world.bombermans[side]
                bomberman.x = pos[0]
                bomberman.y = pos[1]
                self.canvas.edit_image(side, x=bomberman.x * self.config['cell_size'], y=bomberman.y * self.config['cell_size'])

        # empty commands
        self.commands = {}

        # Check for damage
        new_deads = {side: False for side in self.alives_side}
        for side in new_deads:
            bomberman = self.world.bombermans[side]
            for explosion in self.world.explosions:
                if explosion.x == bomberman.x and explosion.y == bomberman.y:
                    new_deads[side] = True
                    bomberman.is_dead = True
                    self.alives_side.remove(side)
                    break

        # Check for end of game
        if len(self.alives_side) == 0:
            self.end_game() # all dead, draw game
        elif len(self.alives_side) == 1:
            # only one alive, winner!
            self.end_game(self.alives_side[0])


    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)


    def on_update_gui(self):
        print('update gui')
        # move all bombermans to front
        for side in self.sides:
            self.canvas.bring_to_front(side)

        # apply actions
        self.canvas.apply_actions()


    def _create_explosion(self, img_name, x, y, angle=0):
        ref = self.canvas.create_image(img_name,
            x * self.config['cell_size'] + int(self.config['cell_size'] / 2),
            y * self.config['cell_size'] + int(self.config['cell_size'] / 2),
            center_origin=True, angle=angle)

        explosion = Explosion(x=x, y=y)
        explosion.ref = ref
        self.world.explosions.append(explosion)


    def _tuple_sum(self, t1, t2):
        return tuple(map(operator.add, t1, t2))


GameHandler = MyRealtimeGameHandler
