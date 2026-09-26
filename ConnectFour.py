import typing

from NeoTrellisGame import NeoTrellisGame, AbstractNeoTrellisGame, Action
from adafruit_neotrellis.multitrellis import MultiTrellis
from adafruit_neotrellis.neotrellis import NeoTrellis
import Colors


player_one = 1
difficulty = 1
player_two = 2
settings = -1
empty_board = [ [0,0,0,0,0,0,0,0],
                [-2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]

class ConnectFour:
    def __init__(self, board: typing.Optional[AbstractNeoTrellisGame] = None):
        self.board = board if board is not None else NeoTrellisGame()
        super().__init__()
        self.game_state = empty_board #0 <- empty | 1 <-player1 | 2 <-player2 | -1 <- SETTINGS... | -2  <- RESET
        self.current_player = 1
        self.register_callbacks()
        self.show_current_player()

    def reset_game(self, x:int, y: int, action: Action):
        #reset the game state to its original empty state
        self.board.clear_board()
        self.game_state = empty_board
        current_player = 1
        self.update_board_colors()
        print("reset game...")
        

    def register_callbacks(self):
        #Register callbacks that will be run when buttons are pressed and released
        self.board.set_callback(0,1, self.reset_game)
        self.board.activate_key(0, 1, Action.BUTTON_PRESSED)
        for col in range(len(self.game_state)):
            self.board.set_callback(col,0, self.place_piece)
            self.board.activate_key(col, 0, Action.BUTTON_PRESSED)
  
    def handle_button_event(self, x:int, y: int, action: Action):
        """
        This is an example of how a callback function will look. It takes an x value, y value, and action, which will indicate what button activated the callback and what action the user did to run it.
        See NeoTrellisGame.set_callback() for info about callbacks.
        """
        #Implement what will happen when the button at position x,y is pressed or released

        self.place_piece(x)
        print("handled button event")
        pass
    #If the row is full, it will return -1.
    def find_lowest_empty_row(self, col: int):
        #Return the lowest empty row in the column.
        for row in range(len(self.game_state)):
            if self.game_state[row][col] == 0:
                continue
            else:
                return row - 1
        return len(self.game_state) -1

    def place_piece(self, x:int, y: int, action: Action):
        #Finds the legal move in the column, and updates the game state to reflect the new piece, checking to see if a player has won with that new piece. Don't forget to play a sound!
        pass

    def update_board_colors(self):
        #un hardcoded magic number of 8
        color = Colors.WHITE
        for i in range(2, 8):
            for j in range(0, 8):
                x = j
                y = i
                if self.game_state[i][j] == 1:
                    color = Colors.RED
                elif self.game_state[i][j] == 2:
                    color = Colors.YELLOW
                else:
                    color = Colors.WHITE
                self.board.set_cell_color(x, y, color)
        self.board.update_display()
    

    def switch_player(self):
        #Change which player is curently placing a piece. Keep track of this in some sort of variable
        if self.current_player == 1:
            self.current_player == 2
        elif self.current_player == 2:
            self.current_player = 1

    def show_current_player(self):
        #Function to indicate on the board which player is currently placing a piece
        #Identify which player's turn it is
        for i in range(0, 8):
            if self.current_player == 1:
                color = Colors.RED
            if self.current_player == 2:
                color = Colors.YELLOW
            self.board.set_cell_color(i,0, color)
        pass

    def is_board_full(self):
        #Return whether or not the game state has no more legal moves
        for full_row in self.game_state:
            for cell_val in full_row:
                if cell_val == 0:
                    return False
        return True
        pass  

    def get_player_color(self, player) -> tuple[int, int, int]:
        #Return the color for the given player 
        if self.current_player == 1:
            return Colors.RED
        elif self.current_player == 2:
            return Colors.YELLOW


    def check_win(self):
        #Check the game state to see if any player has won or if there is a draw
        pass

    def show_winner(self):
        #Display on the board who won
        pass

    def show_tie_game(self):
        #Display on the board that there was a draw
        pass


