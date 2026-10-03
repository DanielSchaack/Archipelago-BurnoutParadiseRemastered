from typing import TYPE_CHECKING

from BaseClasses import Item
from .options import BreakableLocks
from .constants import BURNOUT_PARADISE_REMASTERED
from .data import ItemTypeEnum, ItemData
from .data.items.blockers import Blockers
from .data.items.discoverables import Discoverables
from .data.items.cars import Cars, BurningCars, _BURNING_CARS_IN_ORDER, CarbonCars, ToyCars, LegendaryCars, BoostSpecialCars, CopCars, BigSurfIslandCars, ParadiseBikes
from .data.items.liveries import ParadiseCarsLivery, ParadiseBikesLivery
from .data.items.events import Events
from .data.items.filler import get_default_dict

if TYPE_CHECKING:
    from . import BurnoutParadiseRemasteredWorld

class BurnoutParadiseRemasteredItem(Item):
    game: str = BURNOUT_PARADISE_REMASTERED

def create_item(world: "BurnoutParadiseRemasteredWorld", item: ItemData):
    for _ in range(item.amount):
        world.itempool.append(world.create_item(item.type.value))


def create_single_item(world: "BurnoutParadiseRemasteredWorld", item_type: ItemTypeEnum):
    world.itempool.append(world.create_item(item_type.value))

def create_item_unchecked(world: "BurnoutParadiseRemasteredWorld", item_value: str):
    world.itempool.append(world.create_item(item_value))

def create_items(world: "BurnoutParadiseRemasteredWorld"):

    starting_items: list[Item] = []

    starter_car = _BURNING_CARS_IN_ORDER[world.options.starter_car.value]
    starting_items.append(world.create_item(starter_car.value))
    remaining_burning_cars = [c for c in BurningCars if c != starter_car]

    starting_events = list(world.random.sample(list(Events), world.options.starting_event_amount.value))
    starting_items.extend(world.create_item(e.value) for e in starting_events)

    remaining_events = [e for e in Events if e not in starting_events]
    for item_type in remaining_events:
        create_single_item(world, item_type)


    match world.options.breakable_locks:
        case BreakableLocks.option_locked_by_area:
            for item_type in Blockers:
                create_single_item(world, item_type)
        case BreakableLocks.option_locked_by_area_and_type:
            for item_type in Discoverables:
                create_single_item(world, item_type)

    for item_type in Cars:
        create_single_item(world, item_type)
    for item_type in remaining_burning_cars:
        create_single_item(world, item_type)
    for item_type in CarbonCars:
        create_single_item(world, item_type)
    for item_type in ToyCars:
        create_single_item(world, item_type)
    for item_type in LegendaryCars:
        create_single_item(world, item_type)
    for item_type in BoostSpecialCars:
        create_single_item(world, item_type)
    for item_type in CopCars:
        create_single_item(world, item_type)
    for item_type in BigSurfIslandCars:
        create_single_item(world, item_type)
    for item_type in ParadiseBikes:
        create_single_item(world, item_type)

    if world.options.add_livery_items.value:
        for item_type in ParadiseCarsLivery:
            create_single_item(world, item_type)
        for item_type in ParadiseBikesLivery:
            create_single_item(world, item_type)

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    _remaining = total_location_count - len(world.itempool)

    print(f"Starting item count: {len(starting_items)}")
    print(f"Item pool count: {len(world.itempool)}")
    print(f"Total location count: {total_location_count}")
    print(f"Remaining locations to fill count: {_remaining}")

    filler_items_distribution = world.options.filler_items_distribution.value.copy()
    if sum(filler_items_distribution.values()) == 0:
        filler_items_distribution = get_default_dict()

    for filler_name in create_random_items(world, filler_items_distribution, _remaining):
        create_item_unchecked(world, filler_name)

    world.multiworld.itempool += world.itempool

    return starting_items

def create_random_items(world: "BurnoutParadiseRemasteredWorld", weights: dict[str, int], count: int) -> list[str]:
    filler_pool = weights.copy()
    return world.random.choices(population=list(filler_pool.keys()),
                                weights=list(filler_pool.values()),
                                k=count)

