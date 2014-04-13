from __future__ import print_function

from ChessBoard import *

board = ChessBoard()

print("Capture and improper movement testing")
board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("b3")))
board.processMove(ChessMove("a2-b3"))  # Pawn moves wrongly
board.processMove(ChessMove("a2xb3"))  # Pawn captures pawn
board.processMove(ChessMove("b3xb4"))  # Pawn moves wrongly
board.processMove(ChessMove("b3-b4"))
board.processMove(ChessMove("b4-b6"))  # Pawn moves wrongly
board.processMove(ChessMove("b4-b5"))
board.processMove(ChessMove("b5-b6"))
board.processMove(ChessMove("b6-b7"))  # Pawn moves wrongly
board.processMove(ChessMove("b6xb7"))  # Pawn captures wrongly
board.processMove(ChessMove("b6xc7"))
print("Should result in 5 errors")

print("Promotion testing")
board.clear()
board.pieces.append(ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("c7")))
board.pieces.append(ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("c1")))
board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("d2")))
# Pawn moves to 8th row but does not promote
board.processMove(ChessMove("c7-c8"))
# Pawn captures on 8th row but does not promote
board.processMove(ChessMove("d2xc1"))
board.processMove(ChessMove("c7-c8Q"))
board.processMove(ChessMove("d2xc1R"))
print("Should result in 2 errors")

print("Castling")
board.clear()
