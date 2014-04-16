import copy

from ChessMove import *


class ChessPosition:

    def __init__(self):
        self.FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.sync_stack_to_FEN()
        self.highlight = None

    def remove_all_pieces(self):
        self.FEN = "8/8/8/8/8/8/8/8 w KQkq - 0 1"
        self.sync_stack_to_FEN()

    def sync_stack_to_FEN(self):
        self.grid = [[' ']*8 for d in range(8)]
        sections = self.FEN.split()
        ranks = sections[0].split('/')
        for y in range(0, 8):
            x = 0
            for value in ranks[y]:
                if(value in "12345678"):
                    x += int(value)
                else:
                    self.set_piece((x, 7-y), value, False)  # 7-y since FEN starts at upper left of board
                    x += 1

        self.active_color = "white"
        if(sections[1] == "b"):
            self.active_color = "black"

        if('K' in sections[2]):self.whiteCanCastleKingside = True
        else:self.whiteCanCastleKingside = False
        if('Q' in sections[2]):self.whiteCanCastleQueenside = True
        else:self.whiteCanCastleQueenside = False
        if('k' in sections[2]):self.blackCanCastleKingside = True
        else:self.blackCanCastleKingside = False
        if('q' in sections[2]):self.blackCanCastleQueenside = True
        else:self.blackCanCastleQueenside = False

        if(sections[3] != '-'):
            self.enPassant = ("abcdefgh"[sections[3][0]-1], sections[3][1]-1)
        else:
            self.enPassant = None

        self.halfmoves = (int)(sections[4])
        self.fullmoves = (int)(sections[5])

    def sync_FEN_to_stack(self):
        emptyCount = 0
        self.FEN = ""
        for y in range(7, -1, -1):
            for x in range(0, 8):
                piece = self.get_piece((x, y))
                if(piece != ' '):
                    if(emptyCount > 0):
                        self.FEN += str(emptyCount)
                        emptyCount = 0
                    self.FEN += piece
                else:
                    emptyCount = emptyCount + 1
            if(emptyCount > 0):
                self.FEN += str(emptyCount)
            emptyCount = 0
            if(y != 0):
                self.FEN += "/"
        self.FEN += " "
        if(self.active_color == "white"):
            self.FEN += "w"
        if(self.active_color == "black"):
            self.FEN += "b"
        self.FEN += " "
        castling = ""
        if(self.whiteCanCastleKingside):castling += 'K'
        if(self.whiteCanCastleQueenside):castling += 'Q'
        if(self.blackCanCastleKingside):castling += 'k'
        if(self.blackCanCastleQueenside):castling += 'q'
        if(castling == ""):castling += "-"
        self.FEN += castling
        self.FEN += " "
        # Oddly enough the En Passant point is the spot 'behind' the moved pawn
        if(self.enPassant):
            enPassant = "abcdefgh"[self.enPassant[0]] + str(self.enPassant[1]+1)
        else:enPassant = "-"
        self.FEN += enPassant
        self.FEN += " "
        self.FEN += str(self.halfmoves)
        self.FEN += " "
        self.FEN += str(self.fullmoves)

    def get_piece(self, pos):
        x = pos[0]
        y = pos[1]
        if(self.grid != None):
            if(x >= 0 and x <= 7 and y >=0 and y<= 7):
                return self.grid[x][y]
            else:
                return 'O'      # O stands for Off-Board
        else:
            self.setup_grid()
            return self.get_piece((x, y))

    def formatPosition(self, input):
        if(isinstance(input, str)):
            return (ord(input[0]) - ord('a'), int(input[1]) - 1)
        return None

    def set_piece(self, pos, value, shouldSync):
        x = pos[0]
        y = pos[1]
        self.grid[x][y] = value
        if(shouldSync):
            self.sync_FEN_to_stack()

    def is_check(self):
        return False

    def are_opponents(self, a, b):
        _a = self.get_piece(a)
        _b = self.get_piece(b)
        if((_a in "PNBRQK" and _b in "pnbrqk") or (_a in "pnbrqk" and _b in "PNBRQK")):
            return True
        return False

    def render(self):
        highlights = []
        if(self.highlight != None):
            highlights = self.pseudolegal_positions(self.highlight)
        print('-' * 10)
        for y in range(7, -1, -1):
            print('|', end='')
            for x in range(0, 8):
                icon = self.get_piece((x, y))
                if(icon == ' '):
                    if((y%2 == 0 and x%2 != 0) or (y%2 != 0 and x%2 == 0)):
                        icon = '\u2592'
                if((x, y) in highlights):
                    if(self.are_opponents(self.highlight, (x, y))):
                        icon = 'A'
                    else:
                        icon = 'X'
                print(icon, end='')
            print('|')
        print('-' * 10)
        print(self.FEN)

    # shouldCheckLegality is an optimization since moves made by players could be wrong
    #   but not moves made by the simulator. Even opponent simulator might be wrong
    def make_move(self, move, shouldCheckLegality, shouldLog):
        retVal = copy.deepcopy(self)
        moveIsLegal = True
        if(shouldCheckLegality):
            legalPositions = retVal.legal_positions(move.fromPosition)
            if(move.toPosition not in legalPositions):
                moveIsLegal = False
            if(retVal.get_piece(move.fromPosition) in "PNBRQK" and retVal.active_color != "white"):
                print("Wrong player moved")
                moveIsLegal = False
            if(retVal.get_piece(move.fromPosition) in "pnbrqk" and retVal.active_color != "black"):
                print("Wrong player moved")
                moveIsLegal = False
        if(moveIsLegal):
            if(shouldLog):
                print("Making Move: ", move.notation())
            if(move.isEnPassantCapable):
                if(retVal.active_color == "white"):
                    retVal.enPassant = (move.fromPosition[0], move.fromPosition[1]+1)
                if(retVal.active_color == "black"):
                    retVal.enPassant = (move.fromPosition[0], move.fromPosition[1]-1)
            else:
                # en passant doesn't clear until your next turn
                if(retVal.enPassant and retVal.active_color == "white" and retVal.enPassant[1] == 5):
                    retVal.enPassant = retVal.enPassant
                elif(retVal.enPassant and retVal.active_color == "black" and retVal.enPassant[1] == 2):
                    retVal.enPassant = retVal.enPassant
                else:
                    retVal.enPassant = None

            if(move.isPromoteMove):
                pass
            elif(move.castleType != None):
                pass
            elif(retVal.enPassant and move.toPosition == retVal.enPassant):
                retVal.set_piece(move.toPosition, retVal.get_piece(move.fromPosition), False)
                retVal.set_piece(move.fromPosition, ' ', False)
                if(retVal.enPassant[1] == 5):
                    retVal.set_piece((retVal.enPassant[0], retVal.enPassant[1]-1), ' ', False)
                if(retVal.enPassant[1] == 2):
                    retVal.set_piece((retVal.enPassant[0], retVal.enPassant[1]+1), ' ', False)
            else:       # Regular and capture moves remain
                retVal.set_piece(move.toPosition, retVal.get_piece(move.fromPosition), False)
                retVal.set_piece(move.fromPosition, ' ', False)

            if(retVal.active_color == "white"):
                retVal.active_color = "black"
            else:
                retVal.active_color = "white"
            retVal.sync_FEN_to_stack()
        else:
            print("Tried to play illegal move:", move.notation())
        return retVal

    def legal_positions(self, position):
        retVal = []
        pseudolegals = self.pseudolegal_positions(position)
        for _pos in pseudolegals:
            move = ChessMove(position, _pos, self)
            testPosition = self.make_move(move, False, False)
            if(not testPosition.is_check()):
                retVal.append(_pos)
        return retVal

    # Pseudo-legal positions are positions that are allowed, but may leave the king in check
    def pseudolegal_positions(self, position):
        retVal = []
        piece = self.get_piece(position)
        if(piece == 'P' or piece == 'p'):
            direction = 1
            if(piece == 'p'):
                direction = -1
            up =        (position[0]  , position[1]+1*direction)
            doubleUp =  (position[0]  , position[1]+2*direction)
            upLeft =    (position[0]-1, position[1]+1*direction)
            upRight =   (position[0]+1, position[1]+1*direction)
            if(self.get_piece(up) == ' '):
                retVal.append(up)
            if((piece == 'P' and position[1] == 1) or (piece == 'p' and position[1] == 6)):
                if(self.get_piece(up) == ' ' and self.get_piece(doubleUp) == ' '):
                    retVal.append(doubleUp)
            if(self.are_opponents(position, upLeft)):
                retVal.append(upLeft)
            if(self.are_opponents(position, upRight)):
                retVal.append(upRight)
            if(self.enPassant == upLeft):
                retVal.append(upLeft)
            if(self.enPassant == upRight):
                retVal.append(upRight)
        elif(piece == 'N' or piece == 'n'):
            a = (position[0]-2, position[1]+1)
            b = (position[0]-1, position[1]+2)
            c = (position[0]+2, position[1]+1)
            d = (position[0]+1, position[1]+2)
            e = (position[0]-2, position[1]-1)
            f = (position[0]-1, position[1]-2)
            g = (position[0]+2, position[1]-1)
            h = (position[0]+1, position[1]-2)
            if(self.get_piece(a) == ' ' or self.are_opponents(position, a)):retVal.append(a)
            if(self.get_piece(b) == ' ' or self.are_opponents(position, b)):retVal.append(b)
            if(self.get_piece(c) == ' ' or self.are_opponents(position, c)):retVal.append(c)
            if(self.get_piece(d) == ' ' or self.are_opponents(position, d)):retVal.append(d)
            if(self.get_piece(e) == ' ' or self.are_opponents(position, e)):retVal.append(e)
            if(self.get_piece(f) == ' ' or self.are_opponents(position, f)):retVal.append(f)
            if(self.get_piece(g) == ' ' or self.are_opponents(position, g)):retVal.append(g)
            if(self.get_piece(h) == ' ' or self.are_opponents(position, h)):retVal.append(h)
        elif(piece == 'R' or piece == 'r'):
            for x in range(1, 8):
                pos = (position[0]-x, position[1])
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]+x, position[1])
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0], position[1]+x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0], position[1]-x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
        elif(piece == 'B' or piece == 'b'):
            for x in range(1, 8):
                pos = (position[0]-x, position[1]-x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]+x, position[1]+x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]-x, position[1]+x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]+x, position[1]-x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
        elif(piece == 'K' or piece == 'k'):
            a = (position[0]-1, position[1]+1)
            b = (position[0]+0, position[1]+1)
            c = (position[0]+1, position[1]+1)
            d = (position[0]-1, position[1]+0)
            e = (position[0]+1, position[1]+0)
            f = (position[0]-1, position[1]-1)
            g = (position[0]+0, position[1]-1)
            h = (position[0]+1, position[1]-1)
            if(self.get_piece(a) == ' ' or self.are_opponents(position, a)):retVal.append(a)
            if(self.get_piece(b) == ' ' or self.are_opponents(position, b)):retVal.append(b)
            if(self.get_piece(c) == ' ' or self.are_opponents(position, c)):retVal.append(c)
            if(self.get_piece(d) == ' ' or self.are_opponents(position, d)):retVal.append(d)
            if(self.get_piece(e) == ' ' or self.are_opponents(position, e)):retVal.append(e)
            if(self.get_piece(f) == ' ' or self.are_opponents(position, f)):retVal.append(f)
            if(self.get_piece(g) == ' ' or self.are_opponents(position, g)):retVal.append(g)
            if(self.get_piece(h) == ' ' or self.are_opponents(position, h)):retVal.append(h)
        elif(piece == 'Q' or piece == 'q'):
            a = (position[0]-1, position[1]+1)
            b = (position[0]+0, position[1]+1)
            c = (position[0]+1, position[1]+1)
            d = (position[0]-1, position[1]+0)
            e = (position[0]+1, position[1]+0)
            f = (position[0]-1, position[1]-1)
            g = (position[0]+0, position[1]-1)
            h = (position[0]+1, position[1]-1)
            if(self.get_piece(a) == ' ' or self.are_opponents(position, a)):retVal.append(a)
            if(self.get_piece(b) == ' ' or self.are_opponents(position, b)):retVal.append(b)
            if(self.get_piece(c) == ' ' or self.are_opponents(position, c)):retVal.append(c)
            if(self.get_piece(d) == ' ' or self.are_opponents(position, d)):retVal.append(d)
            if(self.get_piece(e) == ' ' or self.are_opponents(position, e)):retVal.append(e)
            if(self.get_piece(f) == ' ' or self.are_opponents(position, f)):retVal.append(f)
            if(self.get_piece(g) == ' ' or self.are_opponents(position, g)):retVal.append(g)
            if(self.get_piece(h) == ' ' or self.are_opponents(position, h)):retVal.append(h)
            for x in range(1, 8):
                pos = (position[0]-x, position[1])
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]+x, position[1])
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0], position[1]+x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0], position[1]-x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]-x, position[1]-x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]+x, position[1]+x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]-x, position[1]+x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
            for x in range(1, 8):
                pos = (position[0]+x, position[1]-x)
                if(self.get_piece(pos) == ' ' or self.are_opponents(position, pos)):
                    retVal.append(pos)
                if(self.get_piece(pos) != ' '):break
        return retVal