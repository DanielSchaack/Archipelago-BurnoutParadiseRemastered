from .cars import Cars, BurningCars, CarbonCars, ParadiseBikes, ToyCars, LegendaryCars, BoostSpecialCars, CopCars, BigSurfIslandCars, OnlineCars
from .liveries import ParadiseCarsLivery, ParadiseBikesLivery
from ...data import ItemTypeEnum
from .blockers import Blockers
from .discoverables import Discoverables
from .events import Events
from .filler import Filler

all_items: list[ItemTypeEnum] = [
    *Blockers,
    *Discoverables,
    *Cars,
    *BurningCars,
    *CarbonCars,
    *ParadiseBikes,
    *ToyCars,
    *LegendaryCars,
    *BoostSpecialCars,
    *CopCars,
    *BigSurfIslandCars,
    *OnlineCars,
    *Events,
    *ParadiseCarsLivery,
    *ParadiseBikesLivery,
    *Filler
]
