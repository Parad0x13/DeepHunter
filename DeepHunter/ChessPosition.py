from __future__ import print_function
import copy


class POSITION_METADATA:MOVEMENT, ATTACK, NOTHING = range(3)
FileNames = "abcdefgh"


class ChessPosition:

    def __init__(self, *args):
        if len(args) == 1:		# String such as "a3" or "h7"
            self.file = ord((args[0][0])) - ord('a')
            self.rank = (int)(args[0][1]) - 1
            self.metaData = POSITION_METADATA.NOTHING
        elif len(args) == 2:  # Index of file followed by index of row
            self.file = args[0]
            self.rank = args[1]

    def toParsableString(self):
        return FileNames[self.file] + str(self.rank + 1)

    def isOnBoard(self):
        if(self.file < 8 and self.file >= 0 and self.rank < 8 and self.rank >= 0):
            return True
        return False

    def isEqualTo(self, pos):
        if(self.file == pos.file and self.rank == pos.rank):
            return True
        return False

    def copy(self):
        return copy.deepcopy(self)

    def log(self):
        print(self.toParsableString())

    def affect(self, xDelta, yDelta):
        self.file += xDelta
        self.rank += yDelta
