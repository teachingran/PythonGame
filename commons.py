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
            return 1, 0.97
        elif status == GameStatus.TIE:
            return 0.6, 0.6
        return 0.3, 0.3
    

    def get_sign(player):
        sign = 'X'
        if player == Player.RIVAL:
            sign = 'O'
        return sign
    
    def get_player(sign):
        if sign == 'X':
            return Player.AGENT
        elif sign == 'O':
            return Player.RIVAL
        else:
            raise Exception
    
    
    def get_trained_file_name():
        return "trained.pkl"


