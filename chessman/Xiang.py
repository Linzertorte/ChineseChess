from ChessPiece import ChessPiece


class Xiang(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RBS.gif"
            else:
                return "images/BBS.gif"
        else:
            if self.is_red:
                return "images/RB.gif"
            else:
                return "images/BB.gif"

    def get_move_locs(self):
        return []

    def move(self, board, dx, dy):
        x,y = self.x, self.y
        nx, ny = x + dx, y + dy
        if (self.is_red and ny > 4) or (self.is_red== False and ny <5):
            print 'no river cross'
            return False

        if abs(dx)!=2 or abs(dy)!=2:
            print 'not normal'
            return False
        sx, sy = dx/abs(dx), dy/abs(dy)
        if (x+sx, y+sy) in board.pieces:
            print 'blocked'
            return False
        if (nx, ny) in board.pieces:
            board.remove(nx, ny)
        return ChessPiece.move(self, board, dx, dy)
    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

