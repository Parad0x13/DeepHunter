# http://en.wikipedia.org/wiki/Algebraic_notation_(chess)
# http://en.wikipedia.org/wiki/Portable_Game_Notation
# http://chessprogramming.wikispaces.com/Algebraic+Chess+Notation

# TODO: Currently can only promote to Queen if not passed a string to
# parse, fix this eventually

'''
Long Algebraic Notation will take on the form
<LAN move descriptor piece moves> ::= <Piece symbol><from square>['-'|'x']<to square>
<LAN move descriptor pawn moves>  ::= <from square>['-'|'x']<to square>[<promoted to>]
<Piece symbol> ::= 'N' | 'B' | 'R' | 'Q' | 'K'
'''

from __future__ import print_function

from ChessBoard import *


class TYPE:P, N, B, R, Q, K = range(6)
class CASTLETYPE:K, Q = range(2)


class ChessMove:

    def __init__(self, *args):
        self.isPawnMove = False
        self.isCaptureMove = False
        self.isPromoteMove = False
        self.castleType = None
        # Passing a movetext to be parsed
        if(len(args) == 1):
            assert(args[0].__class__ == str)
            notation = args[0]
            if(notation == "O.O"):
                self.castleType = CASTLETYPE.K
            if(notation == "O.O.O"):
                self.castleType = CASTLETYPE.Q
            if(self.castleType != None):
                return
            assert('-' in notation or 'x' in notation)
            if 'x' in notation:
                self.isCaptureMove = True
            if(notation[-1:] in TypeIcons):
                self.isPromoteMove = True
                self.promoteType = TypeForIcon(notation[-1:])
            positions = notation
            if(notation[0] in FileNames):
                self.type = TYPE.P
                self.isPawnMove = True
            else:
                self.type = TypeForIcon(notation[0])
            if(self.type != TYPE.P):
                positions = positions[1:]
            if(self.isPromoteMove):
                positions = positions[:-1]
            if(self.isCaptureMove):
                moves = positions.split('x')
            else:
                moves = positions.split('-')
            self.fromPosition = ChessPosition(moves[0])
            self.toPosition = ChessPosition(moves[1])
        # from, to, board
        if(len(args) == 3):
            assert(args[0].__class__ == ChessPosition)
            assert(args[1].__class__ == ChessPosition)
            #assert(args[2].__class__ == ChessBoard)
            board = args[2]
            self.fromPosition = args[0]
            self.toPosition = args[1]
            pieceFrom = board.pieceAt(self.fromPosition)
            pieceTo = board.pieceAt(self.toPosition)
            self.type = pieceFrom.type
            if(pieceFrom.type == TYPE.P):
                self.isPawnMove = True
                if(pieceFrom.isPositionOnFarthestRank(self.toPosition)):
                    self.isPromoteMove = True
                    self.promoteType = TYPE.Q   # Because... reasons
            if(pieceFrom.type == TYPE.K and pieceFrom.canCastleQueenside and self.toPosition.file == 2):
                self.castleType = CASTLETYPE.Q
            if(pieceFrom.type == TYPE.K and pieceFrom.canCastleKingside and self.toPosition.file == 6):
                self.castleType = CASTLETYPE.K
            if(pieceTo != None and pieceTo.isOpponent(pieceFrom)):
                self.isCaptureMove = True

    def notation(self):
        if(self.castleType != None and self.castleType == CASTLETYPE.K):
            return "O.O"
        if(self.castleType != None and self.castleType == CASTLETYPE.Q):
            return "O.O.O"
        retVal = ""
        if(not self.isPawnMove):
            retVal += TypeIcons[self.type]
        retVal += self.fromPosition.toParsableString()
        if(self.isCaptureMove):
            retVal += "x"
        else:
            retVal += "-"
        retVal += self.toPosition.toParsableString()
        if(self.isPromoteMove):
            retVal += "="
            retVal += TypeIcons[self.promoteType]
        return retVal

    def log(self):
        print(self.notation())
        if(self.isPawnMove):
            print("Pawn Move")
        if(self.isCaptureMove):
            print("Capture Move")
        if(self.isPromoteMove):
            print("Promote Move")
        if(self.castleType != None):
            print("Castle Move")
