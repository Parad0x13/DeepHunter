from __future__ import print_function

from ChessPosition import *
from ChessBoard import *
from globals import *


class ChessPiece:

    def __init__(self, type, color, pos):
        self.type = type
        self.setColor(color)
        self.pos = pos
        self.pawnJustMovedForwardTwice = False
        self.canCastleKingside = True
        self.canCastleQueenside = True
        self.startingPos = self.pos.copy()

    # Decided to set local variables instead of methods so I don't call self.isWhite instead of self.isWhite() by accident
    def setColor(self, color):
        self.color = color
        self.isWhite = False
        self.isBlack = False
        if(self.color == COLOR.WHITE):
            self.isWhite = True
        if(self.color == COLOR.BLACK):
            self.isBlack = True

    def isOpponent(self, other):
        if(self.color != other.color):
            return True
        return False

    def icon(self):
        index = self.type
        if(self.isBlack):
            index += TYPE.K + 1
        return TypeIcons[index]

    def render(self):
        print(self.icon(), end='')

    def isOnStartingPawnPosition(self):
        if(self.isWhite and self.pos.rank == 1):
            return True
        if(self.isBlack and self.pos.rank == 6):
            return True
        return False

    def isPositionOnFarthestRank(self, _pos):
        if(self.isWhite and self.type == TYPE.P and _pos.rank == 7):
            return True
        if(self.isBlack and self.type == TYPE.P and _pos.rank == 0):
            return True
        return False
