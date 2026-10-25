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
    RACE_WINS = ("Unique Race Wins", 1, 40)
    STUNT_RUN_WINS = ("Unique Stunt Run Wins", 2, 14)
    ROAD_RAGE_WINS = ("Unique Road Rage Wins", 3, 16)
    MARKED_MAN_WINS = ("Unique Marked Man Wins", 4, 15)
    BURNING_RIDE_WINS = ("Unique Burning Ride Wins", 5, 19)
    MIDNIGHT_RIDE_WINS = ("Unique Midnight Ride Wins", 6, 19)
    BIG_SURF_ISLAND_WINS = ("Unique Big Surf Island Wins", 7, 15)

wintype_to_item_group = {
    WinType.BURNING_ROUTE_WINS.value:  "Burning Route Event",
    WinType.RACE_WINS.value:           "Race Event",
    WinType.STUNT_RUN_WINS.value:      "Stunt Run Event",
    WinType.ROAD_RAGE_WINS.value:      "Road Rage Event",
    WinType.MARKED_MAN_WINS.value:     "Marked Man Event",
    WinType.BIG_SURF_ISLAND_WINS.value:"Big Surf Island Event",
    WinType.BURNING_RIDE_WINS.value:   "Burning Ride Event",
    WinType.MIDNIGHT_RIDE_WINS.value:  "Midnight Ride Event",
}

event_type_to_wintype = {
    "Burning Route Event":  WinType.BURNING_ROUTE_WINS,
    "Race Event":           WinType.RACE_WINS,
    "Stunt Run Event":      WinType.STUNT_RUN_WINS,
    "Road Rage Event":      WinType.ROAD_RAGE_WINS,
    "Marked Man Event":     WinType.MARKED_MAN_WINS,
    "Big Surf Island Event":WinType.BIG_SURF_ISLAND_WINS,
    "Burning Ride Event":   WinType.BURNING_RIDE_WINS,
    "Midnight Ride Event":  WinType.MIDNIGHT_RIDE_WINS,
}

D_CLASS_WINS = 2
C_CLASS_WINS = 9
B_CLASS_WINS = 24
A_CLASS_WINS = 50
BURNOUT_WINS = 90
BURNOUT_ELITE_WINS = 210

D_CLASS_EVENTS = 2
C_CLASS_EVENTS = 7
B_CLASS_EVENTS = 15
A_CLASS_EVENTS = 26
BURNOUT_EVENTS = 40
BURNOUT_ELITE_EVENTS = 120

def highest_surpassed_threshold(total):
    thresholds = [
        ("BURNOUT_ELITE_EVENTS", BURNOUT_ELITE_EVENTS),
        ("BURNOUT_EVENTS", BURNOUT_EVENTS),
        ("A_CLASS_EVENTS", A_CLASS_EVENTS),
        ("B_CLASS_EVENTS", B_CLASS_EVENTS),
        ("C_CLASS_EVENTS", C_CLASS_EVENTS),
        ("D_CLASS_EVENTS", D_CLASS_EVENTS),
    ]
    for name, value in thresholds:
        if total >= value:
            return name, value
    return None

ITEMS_OFFSET_TRAPS = 5000
ITEMS_OFFSET_BLOCKERS = 1000
ITEMS_OFFSET_BREAKABLES = 1010
ITEMS_OFFSET_FILLER = 100

#locations
LOCATIONS_OFFSET_UNIQUE_CAR_WINS = 200
LOCATIONS_OFFSET_SPEED_CAR_WINS = 500
LOCATIONS_OFFSET_CRASH_CAR_WINS = 600
LOCATIONS_OFFSET_STUNT_CAR_WINS = 700
LOCATIONS_OFFSET_SPECIAL_CAR_WINS = 800
LOCATIONS_OFFSET_BIKE_WINS = 900
LOCATIONS_OFFSET_LICENSES = 1000
LOCATIONS_OFFSET_BURNING_ROUTE_WINS = 1100
LOCATIONS_OFFSET_RACE_WINS = 1200
LOCATIONS_OFFSET_STUNT_RUN_WINS = 1300
LOCATIONS_OFFSET_ROAD_RAGE_WINS = 1400
LOCATIONS_OFFSET_MARKED_MAN_WINS = 1500
LOCATIONS_OFFSET_BURNING_RIDE_WINS = 1600
LOCATIONS_OFFSET_MIDNIGHT_RIDE_WINS = 1700
LOCATIONS_OFFSET_BIG_SURF_ISLAND_WINS = 1800
LOCATIONS_OFFSET_BREAKABLES = 10000
