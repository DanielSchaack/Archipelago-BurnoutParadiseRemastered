from enum import IntEnum, Enum

BURNOUT_PARADISE_REMASTERED = "Burnout Paradise Remastered"

class BreakableType(IntEnum):
    SUPER_JUMP = 0
    SMASH = 1
    BILLBOARD = 2
    DRIVETHRU = 3
    ROADRULE_TIME = 4
    ROADRULE_SHOWTIME = 5
    ROADRULE_BIKES_DAY = 6
    ROADRULE_BIKES_NIGHT = 7

class AreaTypeEnum(Enum):
    def __new__(cls, value: str, index: int):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, value: str, index: int):
        self._value_ = value
        self.index = index

class AreaType(AreaTypeEnum):
    PALM_BAY_HEIGHTS = ("Palm Bay Heights", 0)
    SILVER_LAKE = ("Silver Lake", 1)
    HARBOR_TOWN = ("Harbor Town", 2)
    WHITE_MOUNTAIN = ("White Mountain", 3)
    DOWNTOWN_PARADISE = ("Downtown Paradise",4)
    BIG_SURF_ISLAND = ("Big Surf Island", 5)

class WinTypeEnum(Enum):
    def __new__(cls, value: str, index: int, maximum: int):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, value: str, index: int, maximum: int):
        self._value_ = value
        self.index = index
        self.maximum = maximum

class WinType(WinTypeEnum):
    BURNING_ROUTE_WINS = ("Unique Burning Route Wins", 0, 35)
    RACE_WINS = ("Unique Race Wins", 1, 41)
    STUNT_RUN_WINS = ("Unique Stunt Run Wins", 2, 14)
    ROAD_RAGE_WINS = ("Unique Road Rage Wins", 3, 16)
    MARKED_MAN_WINS = ("Unique Marked Man Wins", 4, 14)

D_CLASS_WINS = 2
C_CLASS_WINS = 9
B_CLASS_WINS = 24
A_CLASS_WINS = 50
BURNOUT_WINS = 90
BURNOUT_ELITE_WINS = 210

ITEMS_OFFSET_TRAPS = 5000
ITEMS_OFFSET_BLOCKERS = 1000
ITEMS_OFFSET_BREAKABLES = 1010
ITEMS_OFFSET_FILLER = 100

#locations
LOCATIONS_OFFSET_UNIQUE_WINS = 100
LOCATIONS_OFFSET_SPEED_CAR_WINS = 500
LOCATIONS_OFFSET_CRASH_CAR_WINS = 600
LOCATIONS_OFFSET_STUNT_CAR_WINS = 700
LOCATIONS_OFFSET_SPECIAL_CAR_WINS = 800
LOCATIONS_OFFSET_LICENSES = 1000
LOCATIONS_OFFSET_BREAKABLES = 10000
