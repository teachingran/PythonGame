from enum import IntEnum
class GameStatus(IntEnum):
    RIVAL_WON = -1
    TIE = 0
    AGENT_WON = 1
    KEEP_PLAYING = 2

class Player (IntEnum):
    RIVAL = -1
    AGENT = 1
