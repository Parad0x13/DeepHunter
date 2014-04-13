from __future__ import print_function

from ChessSimulatorManager import *

simulatorManager = ChessSimulatorManager()

# Single white pawn on start
simulatorManager.board.clear()
piece = ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("b2"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.render()

input("Press Enter to continue...")

# Single white pawn moved forward
simulatorManager.board.clear()
piece = ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("b3"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.render()

input("Press Enter to continue...")

# Single black pawn on start
simulatorManager.board.clear()
piece = ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("b7"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.render()

input("Press Enter to continue...")

# Single black pawn moved forward
simulatorManager.board.clear()
piece = ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("b6"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.render()

input("Press Enter to continue...")

# White pawn attacking
simulatorManager.board.clear()
piece = ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("b2"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("a3")))
simulatorManager.board.render()

input("Press Enter to continue...")

# Black pawn attacking
simulatorManager.board.clear()
piece = ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("b7"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("c6")))
simulatorManager.board.render()

input("Press Enter to continue...")

# Knight
simulatorManager.board.clear()
piece = ChessPiece(TYPE.N, COLOR.WHITE, ChessPosition("d4"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("c2")))  # Should not move/attack
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("e6")))  # Should move/attack
simulatorManager.board.render()

input("Press Enter to continue...")

# Bishop
simulatorManager.board.clear()
piece = ChessPiece(TYPE.B, COLOR.WHITE, ChessPosition("d4"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("b6")))  # Should move/attack
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("g7")))  # Should not move/attack
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("b2")))  # Should not move/attack
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("g1")))  # Should move/attack
simulatorManager.board.render()

input("Press Enter to continue...")

# Rook
simulatorManager.board.clear()
piece = ChessPiece(TYPE.R, COLOR.WHITE, ChessPosition("d4"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("b4")))  # Should not move/attack
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("d7")))  # Should move/attack
simulatorManager.board.render()

input("Press Enter to continue...")

# Queen
simulatorManager.board.clear()
piece = ChessPiece(TYPE.Q, COLOR.WHITE, ChessPosition("d4"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.render()

input("Press Enter to continue...")

# King
simulatorManager.board.clear()
piece = ChessPiece(TYPE.K, COLOR.WHITE, ChessPosition("d4"))
simulatorManager.board.setOverlayTo(piece)
simulatorManager.board.pieces.append(piece)
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.WHITE, ChessPosition("e3")))  # Should not move/attack
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("c5")))  # Should move/attack
simulatorManager.board.pieces.append(ChessPiece(TYPE.P, COLOR.BLACK, ChessPosition("f6")))  # Should prevent movement
simulatorManager.board.render()

input("Press Enter to continue...")
