import random

class Board:
    def __init__(self):
        self.board = [
            ["", "", ""],  
            ["", "", ""],  
            ["", "", ""]  
        ]
    
    def update_board(self, r, c, p_id):
        self.board[r][c] = p_id

    def check_board(self, r, c, p_id):
        # check row and coumn
        if all([True if self.board[r][i] == p_id else False for i in range(3) ]) or all([True if self.board[i][c] == p_id else False for i in range(3) ]):
            print("Game won:" , p_id)
            return True
        # check diagonals
        elif all([True if self.board[i][i] == p_id else False for i in range(3) ]) or all([True if self.board[i][(3-1)-i] == p_id else False for i in range(3) ]):
            print("Game won:" , p_id)
            return True
        return False 
             
class Player:
    def __init__():
        pass

class MultiPlayer(Player):
    def __init__(self):
        self.players_name = ["Player 1", "Player 2"]
        self.players_id = ["PX", "PO"]
        self.board_obj = Board()
        self.turn = random.choice(self.players_name)
    
    def check_turn(self, row, column):
        if self.turn == "Player 1":
            self.turn = "Player 2"
        elif self.turn == "Player 2":
            self.turn = "Player 1"
        
        p_id = self.players_id[self.players_name.index(self.turn)]
        self.board_obj.update_board(row, column, p_id)
        win = self.board_obj.check_board(row, column, p_id)
        return p_id, win

    def check_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board_obj.board[i][j] == "":
                    return False
        return True

class SinglePlayer(Player):
    pass

class GameFactory:
    @staticmethod
    def _create_play(m):
        if m == "Single-Player":
            return SinglePlayer()
        elif m == "Multi-Player":
            return MultiPlayer()