from worlds.burnout_paradise_remastered.data.items.cars import count_boost_type
from worlds.burnout_paradise_remastered.data.regions.regions import Regions
from .breakables import get_locations_for_breakable, breakable_count_lookup, get_car_wins_locations_by_boost
from .cars import CarLocations, CarWinLocations, BurningCarWinLocations, CarbonCarWinLocations, OnlineCarWinLocations, ToyCarWinLocations, LegendaryCarWinLocations, BoostSpecialCarWinLocations, CopCarWinLocations, BigSurfIslandCarWinLocations, ParadiseBikesWinLocations
from .events import EventLocations
from .licenses import LicenseLocations
from .. import GeneratedLocationData, BoostType
from ...constants import AreaType, LOCATIONS_OFFSET_SPECIAL_CAR_WINS, LOCATIONS_OFFSET_STUNT_CAR_WINS, LOCATIONS_OFFSET_CRASH_CAR_WINS, LOCATIONS_OFFSET_SPEED_CAR_WINS
from ...data import LocationTypeEnum

all_enum_locations: list[LocationTypeEnum] = [
    *CarLocations,
    *EventLocations,
    *LicenseLocations,
    *CarWinLocations,
    *BurningCarWinLocations,
    *CarbonCarWinLocations,
    *OnlineCarWinLocations,
    *ToyCarWinLocations,
    *LegendaryCarWinLocations,
    *BoostSpecialCarWinLocations,
    *CopCarWinLocations,
    *BigSurfIslandCarWinLocations,
    *ParadiseBikesWinLocations,
]

all_generated_locations: list[GeneratedLocationData] = [
    *[
        location
        for area_name, breakables in breakable_count_lookup.items()
        for breakable_type, count in breakables.items()
        for location in get_locations_for_breakable(breakable_type, AreaType(area_name), count)
    ],
    *get_car_wins_locations_by_boost(
        BoostType.SPEED, count_boost_type(BoostType.SPEED), Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_SPEED_CAR_WINS
    ),
    *get_car_wins_locations_by_boost(
        BoostType.CRASH, count_boost_type(BoostType.CRASH), Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_CRASH_CAR_WINS
    ),
    *get_car_wins_locations_by_boost(
        BoostType.STUNT, count_boost_type(BoostType.STUNT), Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_STUNT_CAR_WINS
    ),
    *get_car_wins_locations_by_boost(
        BoostType.SPECIAL, count_boost_type(BoostType.SPECIAL), Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_SPECIAL_CAR_WINS,
    ),
]
