from piece import Piece
from rook import Rook
from bishop import Bishop


class Queen(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = color + '_' + 'Q'

    def getLegalMoves(self, board):
        rookQ = Rook(self.getColor())
        rookQ.setPosition(self.getPosition())
        legalRook = rookQ.getLegalMoves(board)
        bishopQ = Bishop(self.getColor())
        bishopQ.setPosition(self.getPosition())
        legalBishop = bishopQ.getLegalMoves(board)
        self.LegalMovesList = [legalRook[0] + legalBishop[0], legalRook[1] + legalBishop[1]]
        return self.LegalMovesList
