from ChessPiece import ChessPiece


class Shuai(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RKS.gif"
            else:
                return "images/BKS.gif"
        else:
            if self.is_red:
                return "images/RK.gif"
            else:
                return "images/BK.gif"

    def get_move_locs(self):
        return []
        moves = []
        for x in range(9):
            if x != self.x:
                moves.append((x,self.y))
        for y in range(10):
            if y != self.y:
                moves.append((self.x, y))
        return moves
    def move(self, board, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if not (self.is_red and 3 <= nx <=5 and 0<= ny <=2) and\
                not (self.is_red == False and 3 <= nx <= 5 and 7 <= ny <= 9):
            print 'out of castle'
            return False
        if abs(dx) + abs(dy) !=1:
            print 'too far'
            return False
        return ChessPiece.move(self, board, dx, dy)

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

