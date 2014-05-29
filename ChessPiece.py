

class ChessPiece:

    selected = False

    def __init__(self, x, y, is_red):
        self.x = x
        self.y = y
        self.is_red = is_red

    def move(self, board, dx, dy):
        board.remove(self.x, self.y)
        print 'Move a chessman from (%d,%d) to (%d,%d)'%(self.x, self.y, self.x+dx, self.y+dy)
        self.x += dx
        self.y += dy
        board.pieces[self.x, self.y] = self
        return True

    def count_pieces(self, board, x, y, dx, dy):
        sx = dx/abs(dx) if dx!=0 else 0
        sy = dy/abs(dy) if dy!=0 else 0
        nx, ny = x + dx, y + dy
        x, y = x + sx, y + sy
        cnt = 0
        while x != nx or y != ny:
            if (x, y) in board.pieces:
                cnt += 1
            x += sx
            y += sy
        return cnt
