from worlds.burnout_paradise_remastered.data.items.drivethrus import DriveThrus
from .cars import BurningRouteRewardCars, BurningCars, CarbonCars, ParadiseBikes, ToyCars, LegendaryCars, BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars
from .liveries import ParadiseCarsLivery, ParadiseBikesLivery
from ...data import ItemTypeEnum, OutOfLogic
from .blockers import Blockers
from .discoverables import Discoverables
from .events import RaceEvents, RoadRageEvents, MarkedManEvents, StuntRunEvents, BurningRideEvents, MidnightRideEvents, BigSurfIslandEvents
from .filler import Filler

all_items: list[ItemTypeEnum] = [
    *Blockers,
    *Discoverables,
    *BurningRouteRewardCars,
    *BurningCars,
    *CarbonCars,
    *ParadiseBikes,
    *ToyCars,
    *LegendaryCars,
    *BoostSpecialCars,
    *CopCars,
    *BigSurfIslandCars,
    *OnlineCars,
    *RaceEvents,
    *RoadRageEvents,
    *MarkedManEvents,
    *StuntRunEvents,
    *BigSurfIslandEvents,
    *BurningRideEvents,
    *MidnightRideEvents,
    *ParadiseCarsLivery,
    *ParadiseBikesLivery,
    *DriveThrus,
    *Filler,
    *OutOfLogic
]
