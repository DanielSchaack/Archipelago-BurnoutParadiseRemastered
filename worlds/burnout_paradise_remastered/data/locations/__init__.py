from worlds.burnout_paradise_remastered.data.items.cars import count_boost_type
from worlds.burnout_paradise_remastered.data.regions.regions import Regions
from .breakables import get_locations_for_breakable, breakable_count_lookup, get_car_wins_locations_by_boost, get_event_wins_locations_by_type
from .cars import CarLocations, CarWinLocations, BurningCarWinLocations, CarbonCarWinLocations, OnlineCarWinLocations, ToyCarWinLocations, LegendaryCarWinLocations, BoostSpecialCarWinLocations, CopCarWinLocations, BigSurfIslandCarWinLocations, ParadiseBikesWinLocations
from .events import BurningRouteLocations, RaceLocations, StuntRunLocations, RoadRageLocations, MarkedManLocations, BigSurfIslandLocations
from .licenses import LicenseLocations
from .. import GeneratedLocationData, BoostType
from ...constants import AreaType, LOCATIONS_OFFSET_SPECIAL_CAR_WINS, LOCATIONS_OFFSET_STUNT_CAR_WINS, LOCATIONS_OFFSET_CRASH_CAR_WINS, LOCATIONS_OFFSET_SPEED_CAR_WINS, WinType, LOCATIONS_OFFSET_BURNING_ROUTE_WINS, LOCATIONS_OFFSET_RACE_WINS, LOCATIONS_OFFSET_STUNT_RUN_WINS, LOCATIONS_OFFSET_ROAD_RAGE_WINS, LOCATIONS_OFFSET_MARKED_MAN_WINS, LOCATIONS_OFFSET_BURNING_RIDE_WINS, LOCATIONS_OFFSET_MIDNIGHT_RIDE_WINS, LOCATIONS_OFFSET_BIKE_WINS, LOCATIONS_OFFSET_BIG_SURF_ISLAND_WINS
from ...data import LocationTypeEnum

all_enum_locations: list[LocationTypeEnum] = [
    *CarLocations,
    *BurningRouteLocations,
    *RaceLocations,
    *StuntRunLocations,
    *RoadRageLocations,
    *MarkedManLocations,
    *BigSurfIslandLocations,
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
    *get_car_wins_locations_by_boost(
        BoostType.BIKE, count_boost_type(BoostType.BIKE), Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_BIKE_WINS,
    ),
    *get_event_wins_locations_by_type(
        WinType.BURNING_ROUTE_WINS, WinType.BURNING_ROUTE_WINS.maximum, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_BURNING_ROUTE_WINS
    ),
    *get_event_wins_locations_by_type(
        WinType.RACE_WINS, WinType.RACE_WINS.maximum, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_RACE_WINS
    ),
    *get_event_wins_locations_by_type(
        WinType.STUNT_RUN_WINS, WinType.STUNT_RUN_WINS.maximum, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_STUNT_RUN_WINS
    ),
    *get_event_wins_locations_by_type(
        WinType.ROAD_RAGE_WINS, WinType.ROAD_RAGE_WINS.maximum, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_ROAD_RAGE_WINS
    ),
    *get_event_wins_locations_by_type(
        WinType.MARKED_MAN_WINS, WinType.MARKED_MAN_WINS.maximum, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_MARKED_MAN_WINS
    ),
    *get_event_wins_locations_by_type(
        WinType.BURNING_RIDE_WINS, WinType.BURNING_RIDE_WINS.maximum, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_BURNING_RIDE_WINS
    ),
    *get_event_wins_locations_by_type(
        WinType.MIDNIGHT_RIDE_WINS, WinType.MIDNIGHT_RIDE_WINS.maximum, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_MIDNIGHT_RIDE_WINS
    ),
    *get_event_wins_locations_by_type(
        WinType.BIG_SURF_ISLAND_WINS, WinType.BIG_SURF_ISLAND_WINS.maximum, Regions.DOWNTOWN_PARADISE, LOCATIONS_OFFSET_BIG_SURF_ISLAND_WINS
    ),
]
