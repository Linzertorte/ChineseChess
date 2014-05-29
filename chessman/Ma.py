
from ChessPiece import ChessPiece


class Ma(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RNS.gif"
            else:
                return "images/BNS.gif"
        else:
            if self.is_red:
                return "images/RN.gif"
            else:
                return "images/BN.gif"

    def can_move(self, board, dx, dy):
        x, y = self.x, self.y
        nx, ny = x+dx, y+dy
        if dx == 0 or dy == 0:
            #print 'no straight'
            return False
        if abs(dx) + abs(dy) !=3:
            #print 'not normal'
            return False
        if (x+dx/2, y+dy/2) in board.pieces:
            #print 'blocked'
            return False
        return True

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

