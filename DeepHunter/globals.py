class TYPE:P, N, B, R, Q, K = range(6)
class CASTLETYPE:K, Q = range(2)
class COLOR:WHITE, BLACK = range(2)
TypeIcons = "PNBRQKpnbrqk"

# I don't like this, refactor later
def TypeForIcon(icon):
    if(icon == 'P'):return TYPE.P
    if(icon == 'N'):return TYPE.N
    if(icon == 'B'):return TYPE.B
    if(icon == 'R'):return TYPE.R
    if(icon == 'Q'):return TYPE.Q
    if(icon == 'K'):return TYPE.K
    if(icon == 'p'):return TYPE.P
    if(icon == 'n'):return TYPE.N
    if(icon == 'b'):return TYPE.B
    if(icon == 'r'):return TYPE.R
    if(icon == 'q'):return TYPE.Q
    if(icon == 'k'):return TYPE.K

def ColorForIcon(icon):
    if(icon in "PNBRQK"):return COLOR.WHITE
    if(icon in "pnbrqk"):return COLOR.BLACK

class POSITION_METADATA:MOVEMENT, ATTACK, NOTHING = range(3)
FileNames = "abcdefgh"