from ChessBoard import *
from ChessView import ChessView


def real_coord(x):
    if x <= 50:
        return 0
    else:
        return (x-50)/40 + 1


def board_coord(x):
    return 30 + 40*x


class ChessGame:

    board = ChessBoard()
    player_is_red = True
    def __init__(self):
        self.view = ChessView(self)
        self.view.showMsg("Red")
        self.view.draw_board(self.board)

    def start(self):
        self.view.start()

    def callback(self, event):
        print event.x, event.y
        rx, ry = real_coord(event.x), real_coord(event.y)
        if self.board.select(rx, ry, self.player_is_red):
            self.player_is_red = not self.player_is_red
            print 'play', self.player_is_red
            self.view.showMsg("Red" if self.player_is_red else "Green")
        print rx, ry
        self.view.draw_board(self.board)

game = ChessGame()
game.start()
