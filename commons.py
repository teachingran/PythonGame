from enum import IntEnum, Enum
class GameStatus(IntEnum):
    RIVAL_WON = -1
    TIE = 0
    AGENT_WON = 1
    KEEP_PLAYING = 2

class Player (IntEnum):
    RIVAL = -1
    AGENT = 1

class General():
    def get_gamma(status):
        if status == GameStatus.AGENT_WON:
            return 1, 0.9
        elif status == GameStatus.TIE:
            return 0.1, 0.1
        return 0, 0
    

    def get_sign(player):
        sign = 'X'
        if player == Player.RIVAL:
            sign = 'O'
        return sign
    
    def get_trained_file_name():
        return "trained.pkl"


