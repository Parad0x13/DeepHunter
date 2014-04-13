from __future__ import print_function

from ChessBoard import *
from ChessSimulatorStream import *
from ChessGraphicsManager import *

class ChessSimulatorManager:

    def __init__(self):
        self.board = ChessBoard()
        self.whiteSimulatorStream = None
        self.blackSimulatorStream = None
        self.chessGraphics = ChessGraphicsManager()
        print("SimulatorManager loaded, no simulator streams locked")

    def tick(self):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit(0)
                elif(event.type == pygame.MOUSEBUTTONDOWN):
                    self.toggleClickedPos(event.pos)
                else:
                    pass
            self.chessGraphics.render(self.board)

    def toggleClickedPos(self, pos):
        position = ChessPosition(int(pos[0]/40), 7-int(pos[1]/40))
        shouldSet = False
        if(self.chessGraphics.selectedPosition is None):
            self.chessGraphics.selectedPosition = position
        else:
            if(self.chessGraphics.selectedPosition.isEqualTo(position)):
                self.chessGraphics.selectedPosition = None
            else:
                piece = self.board.pieceAt(self.chessGraphics.selectedPosition)
                occupant = self.board.pieceAt(position)
                if(piece and occupant and occupant.color == piece.color):
                    self.chessGraphics.selectedPosition = position
                elif(piece is not None and piece.color == self.board.activeColor):
                    move = ChessMove(self.chessGraphics.selectedPosition, position, self.board)
                    self.board.processMove(move)
                    self.chessGraphics.selectedPosition = None
                else:
                    self.chessGraphics.selectedPosition = None

    def lockSimulatorStream(self, simulatorStream, color):
        if(color == COLOR.WHITE):
            self.whiteSimulatorStream = simulatorStream
            print("White simulator stream locked")
        else:
            self.blackSimulatorStream = simulatorStream
            print("Black simulator stream locked")
        if(self.bothSimulatorStreamsLocked()):
            print("Both simulator streams are locked, SimulatorManager primed")

    def bothSimulatorStreamsLocked(self):
        if(self.whiteSimulatorStream and self.blackSimulatorStream):
            return True
        return False
