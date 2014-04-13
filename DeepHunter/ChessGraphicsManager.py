import sys
import pygame
pygame.init()

from ChessBoard import *


squareSize = 40
window = pygame.display.set_mode((squareSize*8, squareSize*8))
whitePawn = pygame.image.load("resources/whitePawn.png")
whitePawn = pygame.transform.smoothscale(whitePawn, (squareSize, squareSize))
blackPawn = pygame.image.load("resources/blackPawn.png")
blackPawn = pygame.transform.smoothscale(blackPawn, (squareSize, squareSize))
whiteRook = pygame.image.load("resources/whiteRook.png")
whiteRook = pygame.transform.smoothscale(whiteRook, (squareSize, squareSize))
blackRook = pygame.image.load("resources/blackRook.png")
blackRook = pygame.transform.smoothscale(blackRook, (squareSize, squareSize))
whiteKnight = pygame.image.load("resources/whiteKnight.png")
whiteKnight = pygame.transform.smoothscale(whiteKnight, (squareSize, squareSize))
blackKnight = pygame.image.load("resources/blackKnight.png")
blackKnight = pygame.transform.smoothscale(blackKnight, (squareSize, squareSize))
whiteBishop = pygame.image.load("resources/whiteBishop.png")
whiteBishop = pygame.transform.smoothscale(whiteBishop, (squareSize, squareSize))
blackBishop = pygame.image.load("resources/blackBishop.png")
blackBishop = pygame.transform.smoothscale(blackBishop, (squareSize, squareSize))
whiteQueen = pygame.image.load("resources/whiteQueen.png")
whiteQueen = pygame.transform.smoothscale(whiteQueen, (squareSize, squareSize))
blackQueen = pygame.image.load("resources/blackQueen.png")
blackQueen = pygame.transform.smoothscale(blackQueen, (squareSize, squareSize))
whiteKing = pygame.image.load("resources/whiteKing.png")
whiteKing = pygame.transform.smoothscale(whiteKing, (squareSize, squareSize))
blackKing = pygame.image.load("resources/blackKing.png")
blackKing = pygame.transform.smoothscale(blackKing, (squareSize, squareSize))

class ChessGraphicsManager:

    def __init__(self):
        self.selectedPosition = None

    def render(self, board):
        self.renderBoard(board)
        self.renderPieces(board)
        pygame.display.flip()

    def selectPosition(self):
        pass

    def renderBoard(self, board):
        whiteColor = (220, 220, 220)
        blackColor = (75, 75, 75)
        for rank in range(0, 8):
            for file in range(0, 8):
                if(rank%2 == 0 and file%2 != 0):
                    color = whiteColor
                elif(rank%2 != 0 and file%2 == 0):
                    color = whiteColor
                else:
                    color = blackColor
                pygame.draw.rect(window, color, (file*squareSize, (7-rank)*squareSize, squareSize, squareSize), 0)
                pygame.draw.rect(window, (0, 0, 0), (file*squareSize, (7-rank)*squareSize, squareSize, squareSize), 1)
        if(self.selectedPosition is not None):
            piece = board.pieceAt(self.selectedPosition)
            positions = board.possibleMovementPositionsOf(piece)
            if(positions != None):
                for position in positions:
                    if(position.metaData == POSITION_METADATA.ATTACK and piece.color == board.activeColor):
                        color = (255, 128, 128)
                        borderColor = (255, 0, 0)
                    elif(position.metaData !=  POSITION_METADATA.ATTACK and piece.color == board.activeColor):
                        color = (80, 200, 200)
                        borderColor = (0, 255, 255)
                    elif(position.metaData == POSITION_METADATA.ATTACK and piece.color != board.activeColor):
                        color = (128, 64, 64)
                        borderColor = (128, 0, 0)
                    elif(position.metaData !=  POSITION_METADATA.ATTACK and piece.color != board.activeColor):
                        color = (40, 100, 100)
                        borderColor = (0, 128, 128)
                    pygame.draw.rect(window, color, (position.file*squareSize, (7-position.rank)*squareSize, squareSize, squareSize), 0)
                    pygame.draw.rect(window, borderColor, (position.file*squareSize, (7-position.rank)*squareSize, squareSize, squareSize), 2)
            if(piece and piece.color == board.activeColor):
                pygame.draw.rect(window, (0, 128, 0), (self.selectedPosition.file*squareSize, (7-self.selectedPosition.rank)*squareSize, squareSize, squareSize), 0)
                pygame.draw.rect(window, (0, 255, 0), (self.selectedPosition.file*squareSize, (7-self.selectedPosition.rank)*squareSize, squareSize, squareSize), 2)
            if(piece and piece.color != board.activeColor):
                pygame.draw.rect(window, (0, 64, 0), (self.selectedPosition.file*squareSize, (7-self.selectedPosition.rank)*squareSize, squareSize, squareSize), 0)
                pygame.draw.rect(window, (0, 128, 0), (self.selectedPosition.file*squareSize, (7-self.selectedPosition.rank)*squareSize, squareSize, squareSize), 2)
            if(piece == None):
                self.selectedPosition = None

    def renderPieces(self, board):
        for piece in board.pieces:
            self.renderPiece(piece)

    def renderPiece(self, piece):
        file = piece.pos.file
        rank = 7-piece.pos.rank
        if(piece.type == TYPE.P and piece.color == COLOR.WHITE):
            window.blit(whitePawn, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.P and piece.color == COLOR.BLACK):
            window.blit(blackPawn, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.R and piece.color == COLOR.WHITE):
            window.blit(whiteRook, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.R and piece.color == COLOR.BLACK):
            window.blit(blackRook, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.N and piece.color == COLOR.WHITE):
            window.blit(whiteKnight, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.N and piece.color == COLOR.BLACK):
            window.blit(blackKnight, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.B and piece.color == COLOR.WHITE):
            window.blit(whiteBishop, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.B and piece.color == COLOR.BLACK):
            window.blit(blackBishop, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.Q and piece.color == COLOR.WHITE):
            window.blit(whiteQueen, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.Q and piece.color == COLOR.BLACK):
            window.blit(blackQueen, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.K and piece.color == COLOR.WHITE):
            window.blit(whiteKing, (file*squareSize, rank*squareSize, squareSize, squareSize))
        if(piece.type == TYPE.K and piece.color == COLOR.BLACK):
            window.blit(blackKing, (file*squareSize, rank*squareSize, squareSize, squareSize))
