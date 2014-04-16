# http://en.wikipedia.org/wiki/Algebraic_notation_(chess)
# http://en.wikipedia.org/wiki/Portable_Game_Notation
# http://chessprogramming.wikispaces.com/Algebraic+Chess+Notation

'''
Long Algebraic Notation will take on the form
<LAN move descriptor piece moves> ::= <Piece symbol><from square>['-'|'x']<to square>
<LAN move descriptor pawn moves>  ::= <from square>['-'|'x']<to square>[<promoted to>]
<Piece symbol> ::= 'N' | 'B' | 'R' | 'Q' | 'K'
'''



class ChessMove:

    def __init__(self, *args):
        self.isCaptureMove = False
        self.isPromoteMove = False
        self.isEnPassantCapable = False
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
            if(notation[-1:] in "PNBRQKpnbrqk"):
                self.isPromoteMove = True
                self.promoteType = notation[-1:]
            positions = notation
            if(notation[0] in "abcdefgh"):
                self.type = "pawn"
            else:
                if(notation[0] == 'N'):
                    self.type = "knight"
                elif(notation[0] == 'B'):
                    self.type = "bishop"
                elif(notation[0] == 'R'):
                    self.type = "rook"
                elif(notation[0] == 'Q'):
                    self.type = "queen"
                elif(notation[0] == 'K'):
                    self.type = "king"
                else:
                    self.type = "unknown"
            if(self.type != "pawn"):
                positions = positions[1:]
            if(self.isPromoteMove):
                positions = positions[:-1]
            if(self.isCaptureMove):
                moves = positions.split('x')
            else:
                moves = positions.split('-')
            self.fromPosition = (ord((moves[0][0])) - ord('a'), (int)(moves[0][1]) - 1)
            self.toPosition = (ord((moves[1][0])) - ord('a'), (int)(moves[1][1]) - 1)
        # from, to, chess position
        if(len(args) == 3):
            chessPosition = args[2]
            self.fromPosition = args[0]
            self.toPosition = args[1]
            pieceFrom = chessPosition.get_piece(self.fromPosition)
            pieceTo = chessPosition.get_piece(self.toPosition)
            if(pieceFrom == 'P' or pieceFrom == 'p'):self.type = "pawn"
            elif(pieceFrom == 'N' or pieceFrom == 'n'):self.type = "knight"
            elif(pieceFrom == 'B' or pieceFrom == 'b'):self.type = "bishop"
            elif(pieceFrom == 'R' or pieceFrom == 'r'):self.type = "rook"
            elif(pieceFrom == 'Q' or pieceFrom == 'q'):self.type = "queen"
            elif(pieceFrom == 'K' or pieceFrom == 'k'):self.type = "king"
            if(self.type == "pawn"):
                if((pieceFrom == 'P' and self.toPosition[1] == 7) or (pieceFrom == 'p' and self.toPosition[1] == 0)):
                    self.isPromoteMove = True
                    self.promoteType = "queen"   # Because... reasons
                if(self.toPosition == chessPosition.enPassant):
                    self.isCaptureMove = True
            if(self.type == "king" and abs(pieceTo[0] - pieceFrom[0]) > 1):
                if(pieceFrom[0] > pieceTo[0]):
                    self.castleType = "queenside"
                else:
                    self.castleType = "kingside"
            if(chessPosition.are_opponents(self.fromPosition, self.toPosition)):
                self.isCaptureMove = True

        if(self.type == "pawn"):
            if(abs(self.fromPosition[1] - self.toPosition[1]) > 1):
                self.isEnPassantCapable = True

    def notation(self):
        if(self.castleType != None and self.castleType == "kingside"):
            return "O.O"
        if(self.castleType != None and self.castleType == "queenside"):
            return "O.O.O"
        retVal = ""
        if(self.type != "pawn"):
            if(self.type == "knight"):
                retVal += "N"
            elif(self.type == "bishop"):
                retVal += "B"
            elif(self.type == "rook"):
                retVal += "R"
            elif(self.type == "queen"):
                retVal += "Q"
            elif(self.type == "king"):
                retVal += "K"
            else:
                retVal += "?"
        retVal += "abcdefgh"[self.fromPosition[0]] + str(self.fromPosition[1]+1)
        if(self.isCaptureMove):
            retVal += "x"
        else:
            retVal += "-"
        retVal += "abcdefgh"[self.toPosition[0]] + str(self.toPosition[1]+1)
        if(self.isPromoteMove):
            retVal += "="
            # Cannot promote to pawn obviously
            if(self.promoteType == "knight"):
                retVal += "N"
            elif(self.promoteType == "bishop"):
                retVal += "B"
            elif(self.promoteType == "rook"):
                retVal += "R"
            elif(self.promoteType == "queen"):
                retVal += "Q"
            elif(self.promoteType == "king"):
                retVal += "K"
            else:
                retVal += "?"
        return retVal

    def log(self):
        print(self.notation())
