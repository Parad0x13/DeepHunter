import random
from ChessBoard import *


class ChessLogic:

    def __init__(self):
        pass

    def findBestMove(self, board):
        return self.findRandomMove(board)

    def findRandomMove(self, board):
        pieces = board.piecesOfColor(board.activeColor)
        random.shuffle(pieces)
        fromPosition = None
        toPosition = None
        for piece in pieces:
            positions = board.possibleMovementPositionsOf(piece)
            random.shuffle(positions)
            if(len(positions) > 0):
                fromPosition = piece.pos
                toPosition = positions[0]
            if(toPosition != None):
                break
        return ChessMove(fromPosition, toPosition, board)

    def minimax(self, board, depth):
        if(depth == 0 or board.is_checkmate() or position.is_stalemate()):
            pass

    def evaluate_board(self, board):
        return 0