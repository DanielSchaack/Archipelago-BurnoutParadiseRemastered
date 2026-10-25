from itertools import chain
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .options import BreakableLocks, filler_default_dict
from .constants import BURNOUT_PARADISE_REMASTERED, BreakableType, AreaType, ITEMS_OFFSET_BREAKABLES
from .data import ItemTypeEnum, BoostType
from .data.locations.cars import BURNING_CAR_TO_BURNING_ROUTE_UNLOCK
from .data.items.drivethrus import DriveThrus
from .data.items.blockers import Blockers
from .data.items.discoverables import Discoverables
from .data.items.cars import _BURNING_CARS_IN_ORDER, get_car_names, get_paradise_car_names, BurningCars
from .data.items.events import RaceEvents, StuntRunEvents, RoadRageEvents, MarkedManEvents
from .data.items.liveries import ParadiseCarsLivery, ParadiseBikesLivery

if TYPE_CHECKING:
    from . import BurnoutParadiseRemasteredWorld

class BurnoutParadiseRemasteredItem(Item):
    game: str = BURNOUT_PARADISE_REMASTERED

def create_item(world: "BurnoutParadiseRemasteredWorld", item: ItemTypeEnum):
    classification = item.classification
    if world.options.car_goal.value and item.value in get_paradise_car_names():
        classification = ItemClassification.progression
    if world.options.unique_car_wins.value and item.value in get_car_names():
        classification = ItemClassification.progression

    return BurnoutParadiseRemasteredItem(
        item.value,
        classification,
        item.item_id,
        world.player,
    )

def create_single_item(world: "BurnoutParadiseRemasteredWorld", item_type: ItemTypeEnum):
    world.itempool.append(world.create_item(item_type.value))

def create_item_unchecked(world: "BurnoutParadiseRemasteredWorld", item_value: str):
    world.itempool.append(world.create_item(item_value))

def create_items(world: "BurnoutParadiseRemasteredWorld"):

    starting_items: list[Item] = []

    starter_car = _BURNING_CARS_IN_ORDER[world.options.starter_car.value]
    starting_items.append(world.create_item(starter_car.value))

    paradise_city_events = [e for e in world.event_items if e != starter_car and e in chain(BurningCars, RaceEvents, StuntRunEvents, RoadRageEvents, MarkedManEvents)]
    starting_events = list(world.random.sample(paradise_city_events, world.options.starting_event_amount.value))
    starting_items.extend(world.create_item(e.value) for e in starting_events)

    for item_type in world.event_items:
        if item_type == starter_car or item_type in starting_events:
            continue
        create_single_item(world, item_type)

    for item_type in world.added_cars:
        create_single_item(world, item_type)

    o = world.options
    counts = {
        BreakableType.SMASH: o.smash_counts.value,
        BreakableType.BILLBOARD: o.billboard_counts.value,
        BreakableType.SUPER_JUMP: o.super_jump_counts.value,
        BreakableType.DRIVETHRU: o.drive_thru_counts.value,
        BreakableType.ROADRULE_TIME: o.road_rule_time_count.value,
        BreakableType.ROADRULE_SHOWTIME: o.road_rule_showtime_count.value,
        BreakableType.ROADRULE_BIKES_DAY: o.road_rule_bike_day_count.value,
        BreakableType.ROADRULE_BIKES_NIGHT: o.road_rule_bike_night_count.value,
    }

    match world.options.breakable_locks:
        case BreakableLocks.option_locked_by_area:
            for item_type in Blockers:
                area = AreaType[item_type.name].value
                # Only add if any counts within an area are configured
                if any(c.get(area, 0) > 0 for c in counts.values()):
                    create_single_item(world, item_type)

        case BreakableLocks.option_locked_by_area_and_type:
            for item_type in Discoverables:
                if item_type.name.endswith(("_ROADRULE_BIKES_DAY", "_ROADRULE_BIKES_NIGHT")) and not any(car.boosttype == BoostType.BIKE for car in world.added_cars):
                    continue

                # Only add if any counts are configured
                area_index, type_value = divmod(item_type.item_id - ITEMS_OFFSET_BREAKABLES, 10)
                area = next(a for a in AreaType if a.index == area_index).value
                if counts[BreakableType(type_value)].get(area, 0) > 0:
                    create_single_item(world, item_type)

    if world.options.add_livery_items.value:
        car_prefixes = tuple(car.value for car in world.added_cars)

        for item_type in chain(ParadiseCarsLivery, ParadiseBikesLivery):
            if item_type.value.startswith(car_prefixes):
                create_single_item(world, item_type)

    if world.options.add_drive_thru_jump_points.value:
        for item_type in DriveThrus:
            create_single_item(world, item_type)

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    _remaining = total_location_count - len(world.itempool)

    filler_items_distribution = world.options.filler_items_distribution.value.copy()
    if sum(filler_items_distribution.values()) == 0:
        filler_items_distribution = filler_default_dict.copy()

    for filler_name in create_random_items(world, filler_items_distribution, _remaining):
        create_item_unchecked(world, filler_name)

    world.multiworld.itempool += world.itempool

    return starting_items

def create_random_items(world: "BurnoutParadiseRemasteredWorld", weights: dict[str, int], count: int) -> list[str]:
    filler_pool = weights.copy()
    return world.random.choices(population=list(filler_pool.keys()),
                                weights=list(filler_pool.values()),
                                k=count)

