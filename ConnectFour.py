import typing

from NeoTrellisGame import NeoTrellisGame, AbstractNeoTrellisGame, Action
from adafruit_neotrellis.multitrellis import MultiTrellis
from adafruit_neotrellis.neotrellis import NeoTrellis
import Colors


player_one = 1
player_two = 2
settings = -1
empty_board = [ [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]
current_player = 1

class ConnectFour:
    def __init__(self, board: typing.Optional[AbstractNeoTrellisGame] = None, ):
        self.board = board if board is not None else NeoTrellisGame()
        super().__init__()
        self.game_state = empty_board #0 <- empty | 1 <-player1 | 2 <-player2 | -1 <- SETTINGS...
        self.register_callbacks()

    def reset_game(self, x:int, y: int, action: Action):
        #TODO reset the game state to its original empty state
        self.board.clear_board()
        self.game_state = empty_board
        current_player = 1
        self.update_board_colors()
        

    def register_callbacks(self):
        #TODO: Register callbacks that will be run when buttons are pressed and released
        self.board.set_callback(0, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(0, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable
        self.board.set_callback(0,1, self.reset_game)
        self.board.activate_key(0, 1, Action.BUTTON_PRESSED)
  
    def handle_button_event(self, x:int, y: int, action: Action):
        """
        This is an example of how a callback function will look. It takes an x value, y value, and action, which will indicate what button activated the callback and what action the user did to run it.
        See NeoTrellisGame.set_callback() for info about callbacks.
        """
        #TODO: Implement what will happen when the button at position x,y is pressed or released


        print("handled button event")
        pass

    def find_lowest_empty_row(self, col: int):
        #TODO: Return the lowest empty row in the column.
        pass

    def place_piece(self, col: int):
        #TODO: Finds the legal move in the column, and updates the game state to reflect the new piece, checking to see if a player has won with that new piece. Don't forget to play a sound!
        pass

    def update_board_colors(self):
        #TODO: un hardcoded magic number of 8
        for i in range(0, 8):
            for j in range(0, 8):
                x = i
                y = j
                if self.game_state[i][j] == 1:
                    color = Colors.BLUE
                elif self.game_state[i][j] == 2:
                    color = Colors.RED
                else:
                    color = Colors.WHITE
                self.board.set_cell_color(x, y, color)
        pass
    

    def switch_player(self):
        #TODO: Change which player is curently placing a piece. Keep track of this in some sort of variable
        pass

    def show_current_player(self):
        #TODO: Function to indicate on the board which player is currently placing a piece
        pass

    def is_board_full(self):
        #TODO: Return whether or not the game state has no more legal moves
        pass  

    def get_player_color(self, player) -> tuple[int, int, int]:
        #TODO: Return the color for the given player 
        pass

    def is_column_full(self, col: int):
        #TODO: Return if the given column is currently full
        pass

    def check_win(self):
        #TODO: Check the game state to see if any player has won or if there is a draw
        pass

    def show_winner(self):
        #TODO: Display on the board who won
        pass

    def show_tie_game(self):
        #TODO: Display on the board that there was a draw
        pass


