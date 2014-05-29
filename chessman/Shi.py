__author__ = 'Zhaoliang'
from ChessPiece import ChessPiece


class Shi(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RAS.gif"
            else:
                return "images/BAS.gif"
        else:
            if self.is_red:
                return "images/RA.gif"
            else:
                return "images/BA.gif"


    def can_move(self, board, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        x, y = self.x, self.y
        if not (self.is_red and 3 <= nx <=5 and 0<= ny <=2) and\
                not (self.is_red == False and 3 <= nx <= 5 and 7 <= ny <= 9):
            #print 'out of castle'
            return False
        if self.is_red and (nx, ny) == (4, 1) or (x,y) == (4,1):
            if abs(dx)>1 or abs(dy)>1:
                #print 'too far'
                return False
        elif self.is_red==False and (nx, ny) == (4, 8) or (x,y) == (4,8):
            if abs(dx)>1 or abs(dy)>1:
                #print 'too far'
                return False
        elif abs(dx) + abs(dy) != 1:
            #print 'no diag'
            return False
        return True

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

