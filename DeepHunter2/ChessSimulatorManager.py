import pygame
pygame.init()

from ChessPosition import *


class ChessSimulatorManager:

    def __init__(self):
        self.whiteSimulatorStream = None
        self.blackSimulatorStream = None
        print("SimulatorManager loaded, no simulator streams locked")
        self.position = ChessPosition()

    def run(self):
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit(0)
                elif(event.type == pygame.MOUSEBUTTONDOWN):
                    self.toggleClickedPos(event.pos)
                else:
                    pass

            self.position.remove_all_pieces()
            self.position.set_piece(self.position.formatPosition("d2"), 'P', True)
            self.position.set_piece(self.position.formatPosition("e3"), 'p', True)
            self.position.highlight = self.position.formatPosition("e3")
            self.position = self.position.make_move(ChessMove("d2-d4"), True, True)
            #self.position = self.position.make_move(ChessMove("d7-d5"), True, True)
            #self.position.highlight = (4, 4)
            #self.position.render()
            #self.position = self.position.make_move(ChessMove("e5xd6"), True, True)
            self.position.render()
            return False

    def start_game(self, color):
        self.player_color = color
        self.run()

    def lockSimulatorStream(self, simulatorStream, color):
        if(color == "white"):
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