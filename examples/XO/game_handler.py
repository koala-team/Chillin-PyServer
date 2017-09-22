# -*- coding: utf-8 -*-

# chillin imports
from chillin_server import TurnbasedGameHandler

# project imports
from ks.models import World, ECell


class MyTurnbasedGameHandler(TurnbasedGameHandler):

    def on_recv_command(self, side_name, agent_name, command_type, command):
        self.last_command = (side_name, command)
        print('command: %s' % (self.last_command, ))


    def on_initialize(self):
        print('initialize')

        self.world = World()
        self.world.board = [[ECell.Empty for _ in range(3)] for _ in range(3)]

        self.last_command = (None, None)
        self.last_move = None
        self.num_filled_cells = 0


    def on_initialize_gui(self):
        print('initialize gui')
        self.canvas.create_image('Background', 0, 0)
        self.canvas.apply_actions()


    def on_process_cycle(self):
        print('process: %s %s' % (self.current_cycle, self.turn_allowed_sides))

        side_name, command = self.last_command
        self.last_command = (None, None)

        if command and self.world.board[command.y][command.x] == ECell.Empty:
            self.num_filled_cells += 1
            self.world.board[command.y][command.x] = ECell.X if side_name == 'X' else ECell.O
            self.last_move = {
                'x': command.x,
                'y': command.y,
                'side': side_name
            }

            # check end-game

            for i in range(3):
                if self.world.board[i][0] != ECell.Empty and self.world.board[i][0] == self.world.board[i][1] == self.world.board[i][2]:
                    self.end_game(side_name)
                    return
                if self.world.board[0][i] != ECell.Empty and self.world.board[0][i] == self.world.board[1][i] == self.world.board[2][i]:
                    self.end_game(side_name)
                    return

            if self.world.board[0][0] != ECell.Empty and self.world.board[0][0] == self.world.board[1][1] == self.world.board[2][2]:
                self.end_game(side_name)
                return

            if self.world.board[0][2] != ECell.Empty and self.world.board[0][2] == self.world.board[1][1] == self.world.board[2][0]:
                self.end_game(side_name)
                return

            if self.num_filled_cells == 9:
                self.end_game()


    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)


    def on_update_gui(self):
        print('update gui')

        if self.last_move:
            self.canvas.create_image(
                self.last_move['side'],
                self.last_move['x'] * self.config['cell_step'] + self.config['cell_init_x'],
                self.last_move['y'] * self.config['cell_step'] + self.config['cell_init_y']
            )
        self.last_move = None
        self.canvas.apply_actions()


GameHandler = MyTurnbasedGameHandler
